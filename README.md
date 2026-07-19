# AI_study_guide
Multi agent/Agentic AI study guide using langgraph

## I. Create a beginner-friendly study guide for this topic:

    The output should have exactly these sections:

    ### 1. Outline
    - Break the topic into 3 short study sections

    ### 2. Notes
    - Write short, clear study notes for each section
    - Keep the explanations concise and easy to understand

    ### 3. Review Questions
    - Write 3 short review questions based on the notes

    Return the result in clean Markdown.

## II. Python + Langchain - study_guide_v1.py.

    The Python + Langchain version uses three focused LLM calls or agents (planner, teacher, and quiz writer) coordinated by regular Python code .

    The ask() function sends a system prompt and user input to the model and returns the response text. The run_agent() function wraps that call and prints how long each step takes.

    Then the code defines three small agents with their own specific prompts:

    planner_agent() creates a 3-part outline for the topic.

    teacher_agent() turns that outline into short beginner-friendly notes.

    quiz_agent() creates 3 review questions from the notes.

    The build_study_guide() function runs those three agents in sequence, passing each output into the next step.

Source: [ Multi-Agent AI System in Python and LangGraph ](https://www.freecodecamp.org/news/how-to-build-your-first-multi-agent-ai-system-in-python-and-langgraph/)