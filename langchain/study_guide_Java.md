# Study Guide: Java

## Outline
Since Java is a massive topic, these three sections are designed to take you from absolute beginner to a solid intermediate understanding, building knowledge logically.

***

### 📚 Section 1: The Fundamentals (Syntax and Basics)

This section is about learning the grammar and vocabulary of the Java language. You must master these concepts before moving on to complex programming structures.

*   **Core Syntax:** Understanding the basic structure of a Java program (classes, methods, `main` function).
*   **Data Types:** Mastering primitive types (`int`, `boolean`, `double`, etc.) and understanding how they store values.
*   **Variables and Operators:** How to declare, initialize, and manipulate variables using arithmetic, relational, and logical operators.
*   **Control Flow:** Learning how to make decisions and repeat actions:
    *   **Conditionals:** `if`/`else if`/`else` statements (making decisions).
    *   **Loops:** `for` loops, `while` loops, and `do-while` loops (repeating actions).
*   **Arrays:** Storing fixed-size collections of the same data type.

***

### 🧱 Section 2: Object-Oriented Programming (OOP)

This is the most critical section. Java is an OOP language, meaning you must learn to *think* in terms of objects and classes. This section teaches you the core philosophy.

*   **Classes and Objects:** Understanding the difference between a blueprint (the Class) and the actual instance (the Object).
*   **The Four Pillars of OOP:**
    1.  **Encapsulation:** Bundling data (variables) and methods (functions) together, and using access modifiers (`private`, `public`) to protect data.
    2.  **Abstraction:** Showing only essential information and hiding complex implementation details (e.g., using an interface).
    3.  **Inheritance:** Allowing a new class (child) to acquire properties and methods from an existing class (parent).
    4.  **Polymorphism:** The ability of an object to take many forms (e.g., using method overriding).
*   **Constructors:** Special methods used to initialize a new object.
*   **Strings:** Handling text data efficiently (understanding `String` immutability).

***

### 🚀 Section 3: Advanced Concepts and Application

Once you understand OOP, this section teaches you how to write robust, scalable, and efficient code that interacts with the outside world.

*   **Collections Framework:** Learning how to manage dynamic groups of data that can change size:
    *   `ArrayList` (for ordered lists).
    *   `HashMap` (for key-value pairs).
    *   `Set` (for unique items).
*   **Exception Handling:** Writing code that doesn't crash when things go wrong. Mastering `try-catch-finally` blocks.
*   **File I/O (Input/Output):** Reading data from and writing data to files on the operating system.
*   **Generics:** Writing code that works with various data types while maintaining type safety (e.g., `List<String>`).
*   **Concurrency (Multithreading):** Understanding how to run multiple tasks simultaneously to improve performance (e.g., using `Thread` or `ExecutorService`).

## Notes
# ☕ Java Learning Roadmap: Beginner to Intermediate

These notes are designed to guide you through Java, building knowledge step-by-step.

***

## 📚 Section 1: The Fundamentals (The Grammar)

This is where you learn the basic vocabulary and structure of the language.

*   **Core Syntax:** Every Java program needs a structure: a **Class** (the container) and a **`main` method** (where the program starts running).
*   **Data Types:** These are containers for values.
    *   **Primitives:** Basic types like `int` (whole numbers), `boolean` (true/false), and `double` (decimals).
    *   **Goal:** Know which type to use for the data you are storing.
*   **Variables & Operators:**
    *   **Variables:** Named containers used to store data (e.g., `age = 30`).
    *   **Operators:** Symbols used to perform actions (e.g., `+` for addition, `==` for comparison).
*   **Control Flow (Decision Making):**
    *   **Conditionals (`if`/`else`):** Allows your code to make decisions. *("If this is true, do X; otherwise, do Y.")*
    *   **Loops (`for`, `while`):** Allows you to repeat actions without rewriting code. *("Do this 10 times," or "Keep doing this until the condition is false.")*
*   **Arrays:** Used to store a fixed list of items of the same type (e.g., a list of 5 student scores).

***

## 🧱 Section 2: Object-Oriented Programming (The Philosophy)

This is the most important section. Java is an OOP language, meaning you must learn to *think* in terms of objects.

*   **Class vs. Object:**
    *   **Class:** The **blueprint** (the design). It defines what something *is* (e.g., the blueprint for a "Car").
    *   **Object:** The actual **instance** built from the blueprint (e.g., *your* specific red Honda).
*   **The Four Pillars of OOP:**
    1.  **Encapsulation:** Bundling data (variables) and the functions that use that data (methods) together. It also means **protecting** data using access modifiers (`private`).
    2.  **Abstraction:** Hiding the complex details and only showing the user what they need to know. *("You just press the gas pedal; you don't need to know how the engine works.")*
    3.  **Inheritance:** Allowing a new class (Child) to automatically get all the properties and methods of an existing class (Parent). *("A 'Truck' is a type of 'Vehicle,' so it automatically gets all 'Vehicle' features.")*
    4.  **Polymorphism:** The ability for different objects to respond to the same command in their own unique way. *("If you tell a 'Dog' and a 'Cat' to 'make sound,' they will bark and meow, respectively.")*
*   **Constructors:** Special methods that run automatically when you create a new object, used to set up the object's initial state.
*   **Strings:** Java's way of handling text. Remember that `String` data is **immutable** (it cannot be changed once created).

***

## 🚀 Section 3: Advanced Concepts (Real-World Code)

These tools help you write code that is stable, flexible, and powerful.

*   **Collections Framework:** Used when you need data structures that can **change size** (unlike fixed-size Arrays).
    *   **`ArrayList`:** The most common list; keeps items in order.
    *   **`HashMap`:** Stores data as **Key-Value pairs** (like a dictionary: `Name` $\rightarrow$ `Value`).
    *   **`Set`:** Stores only **unique** items (no duplicates allowed).
*   **Exception Handling:** How to prevent your program from crashing when something unexpected happens (like a user entering text when a number is expected).
    *   **`try-catch-finally`:** The structure used to "try" risky code, "catch" the error if it happens, and "finally" run cleanup code regardless of success or failure.
*   **File I/O (Input/Output):** The ability to read data from, and write data to, external files on your computer.
*   **Generics:** A way to write code that works with *any* data type while still keeping the code safe and type-checked (e.g., `List<String>` ensures the list only holds strings).
*   **Concurrency (Multithreading):** The ability to run multiple tasks or calculations *at the same time*. This is crucial for making applications fast and responsive.

## Review Questions
Here are 3 short review questions designed to test understanding across the major sections of the notes:

1.  **OOP Concept:** In Java, what is the fundamental difference between a **Class** and an **Object**? Furthermore, which OOP pillar is responsible for *protecting* the data within an object?
    *(Tests: Class vs. Object, Encapsulation)*

2.  **Data Structures:** When should you use a `HashMap` instead of an `ArrayList`? What specific data structure relationship does the `HashMap` utilize?
    *(Tests: Collections Framework, Key-Value pairs)*

3.  **Error Handling:** If your program might crash because a user inputs text when a number is expected, what specific Java structure (`try-catch-finally`) must you use to prevent the program from failing and to ensure cleanup code runs?
    *(Tests: Exception Handling, Control Flow)*
