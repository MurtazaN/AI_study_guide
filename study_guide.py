from typing import TypedDict
import time

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

# Local Ollama model used by all nodes.
# MODEL = ChatOllama(model="gemma4:e4b", temperature=0)

MODEL = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed",
    model="microsoft/phi-4-mini-reasoning", 
    temperature=0.7
)


# Shared state passed between nodes.
# A kind of "schema" or "blueprint" for the data that will flow between nodes.
class StudyState(TypedDict):
    topic: str
    outline: str
    notes: str
    quiz: str


def ask(system: str, user: str) -> str:
    ''' The system role is meant for behavioral instructions (e.g., "You are a helpful assistant. Be concise.").
        The user role is meant for questions or tasks.
    '''
    response = MODEL.invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ])
    return response.content


def run_node(name: str, system: str, user: str) -> str:
    print(f"Calling node {name}...")
    start = time.time()
    result = ask(system, user)
    print(f"Finished {name} in {time.time() - start:.1f}s")
    return result


# Node 1: create the outline
def planner(state: StudyState) -> dict:
    return {
        "outline": run_node(
            "planner",
            "Break this topic into 3 short study sections.",
            state["topic"],
        )
    }


# Node 2: write notes from the outline
def teacher(state: StudyState) -> dict:
    return {
        "notes": run_node(
            "teacher",
            "Write short beginner-friendly notes using the outline. Keep it concise.",
            f"Topic: {state['topic']}\n\nOutline:\n{state['outline']}",
        )
    }


# Node 3: write review questions from the notes
def quiz_writer(state: StudyState) -> dict:
    return {
        "quiz": run_node(
            "quiz_writer",
            "Write 3 short review questions based on the notes.",
            f"Topic: {state['topic']}\n\nNotes:\n{state['notes']}",
        )
    }


def build_graph():
    # 1. Create empty graph bound to StudyState schema
    graph = StateGraph(StudyState)

    # 2. Register each node with a string name (the label) and the function (the worker)
    graph.add_node("planner", planner)
    graph.add_node("teacher", teacher)
    graph.add_node("quiz_writer", quiz_writer)

    # 3. Define the flow/order of execution i.e edges to define execution order
    graph.add_edge(START, "planner")
    graph.add_edge("planner", "teacher")
    graph.add_edge("teacher", "quiz_writer")
    graph.add_edge("quiz_writer", END)

    # 4. Compile the graph into an executable/runnable app
    return graph.compile()

def save_study_guide(content: str, topic: str) -> str:
    filename = f"study_guide_{topic.replace(' ', '_')}.md"
    with open(filename, "w") as f:
        f.write(content)
    return filename

if __name__ == "__main__":
    print("Warming up model...")
    # Warm Up the Model
    MODEL.invoke("Say ready.")
    print("Model ready.\n")

    # Compiles the graph into an executable app. Done once, reused for every topic.
    app = build_graph()

    # Ask the user for a study topic
    topic = input("Enter a study topic: ").strip()

    # Initialize the state for the graph and invoke the app with the topic.
    result = app.invoke({
        "topic": topic,
        "outline": "",
        "notes": "",
        "quiz": "",
    })
    # The result dict contains the final values of outline, notes, and quiz - all populated by the graph run

    # Format the study guide content into Markdown
    content = (
        f"# Study Guide: {topic}\n\n"
        f"## Outline\n{result['outline']}\n\n"
        f"## Notes\n{result['notes']}\n\n"
        f"## Review Questions\n{result['quiz']}\n"
    )

    # Save the study guide to a Markdown file
    filename = save_study_guide(content, topic)
    print(f"Study guide saved to {filename}")