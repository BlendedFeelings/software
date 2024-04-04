---
b: https://blendedfeelings.com/software/python/function.md
---

# Functions in Python
are defined using the `def` keyword, followed by the function name and a set of parentheses `()` which can enclose parameters. The body of the function is indented under the `def` line. Functions can take arguments and can also return values using the `return` statement. Here is an example of a simple Python function:

```python
def greet(name):
    """This function greets the person whose name is passed as a parameter"""
    return f"Hello, {name}!"

# Usage
print(greet("Alice"))  # Output: Hello, Alice!
```

Functions can be more complex, involving multiple parameters, default values for parameters, variable-length argument lists, keyword arguments, and more. Here are a few examples demonstrating these features:

```python
# Function with default parameter value
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))  # Output: Hello, Bob!
print(greet("Bob", greeting="Hi"))  # Output: Hi, Bob!

# Function with variable-length arguments (*args)
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 2, 3))  # Output: 6

# Function with keyword arguments (**kwargs)
def person_details(**details):
    return f"Name: {details['name']}, Age: {details['age']}"

print(person_details(name="Charlie", age=30))  # Output: Name: Charlie, Age: 30
```

Python also supports anonymous functions, known as lambda functions, which are defined using the `lambda` keyword:

```python
# Lambda function to add two numbers
add = lambda x, y: x + y

print(add(5, 3))  # Output: 8
```

These are some of the basic concepts of functions in Python. Functions are a fundamental part of Python programming and are used to encapsulate reusable code blocks that can be called from multiple places within a program.