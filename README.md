Python Decorators in Python 



What is a Decorator?

A **decorator** is a function that takes another function as input, adds extra functionality to it, and returns the modified function. Decorators are represented using the **`@`** symbol.

Basic Syntax

```python
def decorator(function):

    def wrapper():
        # Additional functionality
        function()

    return wrapper

@decorator
def display():
    print("Hello")
```

---

 1. Logging Decorator


The Logging Decorator** prints a message before and after executing a function. It helps developers monitor the execution flow of a program and is commonly used for debugging and logging.

Purpose

* Tracks function execution.
* Helps in debugging.
* Improves code monitoring.



 2. Execution Time Decorator
Description

The Execution Time Decorator** measures the amount of time a function takes to execute. It is useful when optimizing programs or comparing algorithm performance.


* Measures execution speed.
* Identifies slow functions.
* Helps optimize program performance.



#3. Authentication Decorator

Description

The Authentication Decorator** verifies whether a user has permission to execute a function before allowing access.

Purpose

* Protects sensitive functions.
* Restricts unauthorized access.
* Improves application security.



4. Decorator with Function Arguments
Description

This decorator demonstrates how decorators can work with functions that accept parameters. In the example, the returned string is converted to uppercase before being displayed.

Purpose

* Modifies returned values.
* Works with parameterized functions.
* Enhances output formatting.



5. Decorator on Class Methods

Description

Decorators are not limited to normal functions—they can also be applied to methods inside classes. This example prints a message before and after executing a class method.

Purpose

* Enhances object-oriented programs.
* Adds functionality to class methods.
* Improves modular programming.


6. Repeat Function Decorator

Description

The Repeat Function Decorator** executes the same function multiple times automatically. This reduces code repetition and improves readability.

### Purpose

* Executes a function repeatedly.
* Eliminates duplicate code.
* Simplifies repetitive operations.



Advantages of Decorators

* Improves code reusability.
* Keeps the original function unchanged.
* Makes programs modular and maintainable.
* Reduces duplicate code.
* Separates additional functionality from business logic.
* Widely used in Python frameworks such as Django and Flask.




Decorators are one of Python's most powerful features. They allow developers to add extra functionality to functions and methods in a clean, reusable, and efficient way. Understanding decorators is an essential step toward writing modular, maintainable, and professional Python applications.


Author:Niharika Angore
Course:B.Tech CSE (AI & Analytics) – Second Year
University:MIT ADT University, Pune
