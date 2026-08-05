"""
===========================================================
            PYTHON DECORATORS - PRACTICAL EXAMPLES
===========================================================

Author      : Niharika Angore
Course      : B.Tech CSE (AI & Analytics) - Second Year
University  : MIT ADT University, Pune

Description:
This program demonstrates six different uses of decorators in Python.

Examples Included:
1. Logging Decorator
2. Execution Time Decorator
3. Authentication Decorator
4. Decorator with Function Arguments
5. Decorator on Class Method
6. Repeat Function Decorator

===========================================================
"""

import time

# =========================================================
# Example 1 : Logging Decorator
# =========================================================

print("\n========== Example 1 : Logging Decorator ==========\n")

def logger(func):
    """Prints a message before and after function execution."""

    def wrapper():
        print(">> Function Started")
        func()
        print(">> Function Finished\n")

    return wrapper


@logger
def greet():
    print("Hello! Welcome to Python Decorators.")


greet()


# =========================================================
# Example 2 : Execution Time Decorator
# =========================================================

print("\n========== Example 2 : Execution Time Decorator ==========\n")

def calculate_time(func):
    """Calculates the execution time of a function."""

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print(f"Execution Time : {end-start:.6f} seconds\n")

    return wrapper


@calculate_time
def large_loop():

    for i in range(1000000):
        pass


large_loop()


# =========================================================
# Example 3 : Authentication Decorator
# =========================================================

print("\n========== Example 3 : Authentication Decorator ==========\n")

logged_in = True


def authenticate(func):
    """Checks whether the user is authenticated."""

    def wrapper():

        if logged_in:
            func()
        else:
            print("Access Denied!\n")

    return wrapper


@authenticate
def dashboard():
    print("Welcome to Student Dashboard\n")


dashboard()


# =========================================================
# Example 4 : Decorator with Function Arguments
# =========================================================

print("\n========== Example 4 : Decorator with Arguments ==========\n")

def uppercase(func):
    """Converts the returned string into uppercase."""

    def wrapper(name):

        result = func(name)

        return result.upper()

    return wrapper


@uppercase
def welcome(name):
    return f"Hello {name}"


print(welcome("Niharika"))


# =========================================================
# Example 5 : Decorator on Class Method
# =========================================================

print("\n========== Example 5 : Class Method Decorator ==========\n")

def message(func):
    """Prints a message before and after executing a class method."""

    def wrapper(self):

        print("Before Display Method")

        func(self)

        print("After Display Method\n")

    return wrapper


class Student:

    @message
    def display(self):
        print("Student Name : Niharika")
        print("Course       : CSE AI & Analytics")


student = Student()
student.display()


# =========================================================
# Example 6 : Repeat Function Decorator
# =========================================================

print("\n========== Example 6 : Repeat Function Decorator ==========\n")

def repeat(func):
    """Executes the decorated function three times."""

    def wrapper():

        for i in range(3):
            func()

    return wrapper


@repeat
def hello():
    print("Learning Python Decorators")


hello()


# =========================================================
# End of Program
# =========================================================

print("\nAll six decorator examples executed successfully.")