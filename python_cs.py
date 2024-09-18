# Import Specific Function:
# Comment: Imports a specific function from a module.
# Syntax: from module_name import function_name

from math import sqrt  # Importing the sqrt function from the math module

# Install Package:
# Syntax: pip install package_name
# Comment: Installs a package from the Python Package Index (PyPI).

# Install Requests Package:
# Command to run in the terminal
# pip install requests

# Import Entire Module:
# Comment: Imports an entire module.
# Syntax: import module_name

import math  # Importing the entire math module

# Import with Alias:
# Comment: Imports a module with a custom alias.
# Syntax: import module_name as alias

import pandas as pd  # Importing pandas module as pd

# Define a Function:
# Comment: Defines a function with parameters and return value.
# Syntax: def function_name(parameters): return value

def greet(name):
    return f"Hello, {name}!"

# Call a Function:
# Comment: Calls a function with arguments.
# Syntax: function_name(arguments)

print(greet("Alice"))  # Calls the greet function with the argument "Alice"

# List Comprehension:
# Comment: Creates a new list by applying an expression to each item in an existing list.
# Syntax: [expression for item in iterable]

squares = [x**2 for x in range(10)]  # List comprehension to get squares of numbers from 0 to 9

# Lambda Function:
# Comment: Creates an anonymous function.
# Syntax: lambda parameters: expression

add = lambda x, y: x + y  # Lambda function to add two numbers

# Dictionary Comprehension:
# Comment: Creates a new dictionary by applying an expression to each item in an existing iterable.
# Syntax: {key_expression: value_expression for item in iterable}

squares_dict = {x: x**2 for x in range(10)}  # Dictionary comprehension for squares

# Try-Except Block:
# Comment: Catches and handles exceptions.
# Syntax:
# try:
#     code_block
# except ExceptionType as e:
#     handle_exception

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero!")

# File Handling:
# Comment: Opens, reads, and writes to files.
# Syntax:
# open('file_name', 'mode') as file:
#     file_operation

with open('example.txt', 'w') as file:  # Open file for writing
    file.write("Hello, world!")  # Write to the file

with open('example.txt', 'r') as file:  # Open file for reading
    content = file.read()  # Read the content of the file
    print(content)  # Print the content

# List Operations:
# Comment: Operations on lists such as append, remove, and slicing.
# Syntax:
# list.append(item)  # Adds item to the end of the list
# list.remove(item)  # Removes first occurrence of item from the list
# list[start:end]  # Slices the list from start to end

numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Appends 6 to the list
numbers.remove(3)  # Removes first occurrence of 3 from the list
sublist = numbers[1:4]  # Slices the list from index 1 to 3

# String Formatting:
# Comment: Formats strings using f-strings or format method.
# Syntax: f"string {variable}" or "string {}".format(variable)

name = "Alice"
greeting = f"Hello, {name}!"  # Using f-string
print(greeting)

greeting = "Hello, {}!".format(name)  # Using format method
print(greeting)

# Regular Expressions:
# Comment: Pattern matching using the re module.
# Syntax:
# import re
# re.match(pattern, string)
# re.search(pattern, string)
# re.findall(pattern, string)

import re

pattern = r'\d+'  # Regular expression pattern to match digits
text = 'There are 24 apples and 13 oranges.'

matches = re.findall(pattern, text)  # Finds all occurrences of the pattern
print(matches)  # Prints ['24', '13']

# Class Definition:
# Comment: Defines a class with attributes and methods.
# Syntax:
# class ClassName:
#     def __init__(self, attributes):
#         self.attribute = attribute
#     def method(self):
#         pass

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")  # Create an instance of Dog
print(my_dog.bark())  # Call the bark method

# Handling JSON Data:
# Comment: Parse and manipulate JSON data using the json module.
# Syntax:
# import json
# json.loads(json_string)
# json.dumps(data)

import json

json_data = '{"name": "Alice", "age": 30}'
data = json.loads(json_data)  # Parse JSON data
print(data["name"])  # Accessing value from parsed JSON

data["age"] = 31  # Modify data
json_string = json.dumps(data)  # Convert data back to JSON string
print(json_string)

# Web Requests:
# Comment: Send HTTP requests using the requests library.
# Syntax:
# import requests
# response = requests.get('url')
# response.json()  # For JSON response
# response.text  # For plain text response

import requests

response = requests.get('https://api.github.com')
print(response.json())  # Print JSON response from the URL

# Multithreading:
# Comment: Run multiple threads for concurrent execution using the threading module.
# Syntax:
# import threading
# def thread_function():
#     pass
# thread = threading.Thread(target=thread_function)
# thread.start()
# thread.join()

import threading

def print_hello():
    print("Hello from thread!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()  # Wait for thread to finish

# Debugging:
# Comment: Use the pdb module to debug code.
# Syntax:
# import pdb
# pdb.set_trace()

import pdb

def divide(a, b):
    pdb.set_trace()  # Set a breakpoint
    return a / b

result = divide(10, 2)  # Call the function to debug
print(result)


# -------------------------------------------------------------------------


# List Operations:
# Comment: Common list operations.
# Syntax:
# list.append(item)  # Adds item to the end
# list.insert(index, item)  # Inserts item at the specified index
# list.pop(index)  # Removes and returns item at index
# list.sort()  # Sorts the list in place
# list.reverse()  # Reverses the list in place

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 0)  # Inserts 0 at the beginning
last_item = numbers.pop()  # Removes and returns the last item
numbers.sort(reverse=True)  # Sorts the list in descending order
numbers.reverse()  # Reverses the list

# Tuple Operations:
# Comment: Operations with tuples, which are immutable sequences.
# Syntax:
# tuple_name = (item1, item2, ...)
# tuple_name[index]  # Access item at index
# tuple_name.count(item)  # Count occurrences of item
# tuple_name.index(item)  # Find index of first occurrence of item

coordinates = (10.0, 20.0)
x = coordinates[0]  # Access first item
y = coordinates[1]  # Access second item

# Set Operations:
# Comment: Operations with sets, which are unordered collections of unique elements.
# Syntax:
# set_name = {item1, item2, ...}
# set_name.add(item)  # Adds item to the set
# set_name.remove(item)  # Removes item from the set
# set_name.union(other_set)  # Union of two sets
# set_name.intersection(other_set)  # Intersection of two sets
# set_name.difference(other_set)  # Difference between two sets

fruits = {'apple', 'banana', 'cherry'}
fruits.add('date')  # Adds 'date' to the set
fruits.remove('banana')  # Removes 'banana' from the set

# Dictionary Operations:
# Comment: Common dictionary operations.
# Syntax:
# dict_name = {'key1': value1, 'key2': value2, ...}
# dict_name[key]  # Access value by key
# dict_name.get(key)  # Get value by key with default option
# dict_name.keys()  # Get all keys
# dict_name.values()  # Get all values
# dict_name.items()  # Get all key-value pairs
# dict_name.update(new_dict)  # Update dictionary with new key-value pairs

person = {'name': 'Alice', 'age': 30}
person['age'] = 31  # Update value for 'age'
name = person.get('name')  # Get value for 'name'
keys = person.keys()  # Get all keys

# Generators:
# Comment: Create iterators with generator functions or expressions.
# Syntax:
# def generator_function():
#     yield value
# generator_expression = (expression for item in iterable)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):  # Use the generator
    print(number)

# Regular Expressions - Advanced:
# Comment: More advanced usage of regex.
# Syntax:
# re.sub(pattern, replacement, string)  # Replace occurrences of pattern with replacement
# re.findall(pattern, string)  # Find all matches
# re.search(pattern, string)  # Search for the first match

text = 'The price is $42.00 and $35.00'
amounts = re.findall(r'\$\d+\.\d+', text)  # Find all dollar amounts
print(amounts)

# Decorators:
# Comment: Modify or extend the behavior of a function or method.
# Syntax:
# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         # Code before
#         result = func(*args, **kwargs)
#         # Code after
#         return result
#     return wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))

# Context Managers:
# Comment: Manage resources using the `with` statement.
# Syntax:
# with open('file_name', 'mode') as file:
#     file_operation

# Custom Context Manager:
# Syntax:
# class ContextManager:
#     def __enter__(self):
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         pass

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager() as manager:
    print("Inside the context")

# Coroutines:
# Comment: Handle asynchronous tasks using coroutines.
# Syntax:
# async def coroutine_function():
#     await async_operation()

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())  # Run the coroutine

# Exception Handling - Custom Exceptions:
# Comment: Define and raise custom exceptions.
# Syntax:
# class CustomError(Exception):
#     pass

class CustomError(Exception):
    pass

def risky_function(x):
    if x < 0:
        raise CustomError("Negative value error!")
    return x

try:
    result = risky_function(-1)
except CustomError as e:
    print(e)

# Asyncio - Tasks:
# Comment: Run multiple coroutines concurrently using tasks.
# Syntax:
# task = asyncio.create_task(coroutine_function())
# await task

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    task1_instance = asyncio.create_task(task1())
    task2_instance = asyncio.create_task(task2())
    await task1_instance
    await task2_instance

asyncio.run(main())  # Run the main coroutine

# Unit Testing:
# Comment: Write unit tests using the unittest module.
# Syntax:
# import unittest
# class TestClass(unittest.TestCase):
#     def test_method(self):
#         self.assertEqual(result, expected)

import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == "__main__":
    unittest.main()

# Data Classes:
# Comment: Define classes that primarily store data.
# Syntax:
# from dataclasses import dataclass
# @dataclass
# class DataClass:
#     attribute1: type
#     attribute2: type

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person(name="Alice", age=30)
print(person)

# Named Tuples:
# Comment: Create immutable objects with named fields.
# Syntax:
# from collections import namedtuple
# NamedTuple = namedtuple('NamedTuple', 'field1 field2')
# instance = NamedTuple(field1=value1, field2=value2)

from collections import namedtuple

Point = namedtuple('Point', 'x y')
p = Point(x=10, y=20)
print(p.x, p.y)

# Itertools - Combinations and Permutations:
# Comment: Generate combinations and permutations using itertools.
# Syntax:
# from itertools import combinations, permutations
# combinations(iterable, r)
# permutations(iterable, r)

from itertools import combinations, permutations

items = ['A', 'B', 'C']
comb = list(combinations(items, 2))  # All 2-element combinations
perm = list(permutations(items, 2))  # All 2-element permutations

print("Combinations:", comb)
print("Permutations:", perm)

# Profiling:
# Comment: Measure the performance of your code using the cProfile module.
# Syntax:
# import cProfile
# cProfile.run('code_to_profile')

import cProfile

def test_function():
    sum(range(10000))

cProfile.run('test_function()')

# Memoization:
# Comment: Cache results of expensive function calls using functools.lru_cache.
# Syntax:
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def expensive_function(x):
#     pass

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))  # Example of using memoization to optimize Fibonacci calculation
