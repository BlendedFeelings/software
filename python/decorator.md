---
b: https://blendedfeelings.com/software/python/decorator.md
---

# Decorators in Python
are a powerful feature that allows you to modify the behavior of a function or a class. A decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

Here's how decorators work in Python:

1. **Simple Decorator**: A decorator is a callable that returns a callable. Typically, the callable is a function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# This will print:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
say_hello()
```

2. **Decorators with Arguments**: If you want your decorator to take arguments, you need to add another layer of functions.

```python
def decorator_with_args(arg1, arg2):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Arguments for the decorator: {arg1}, {arg2}")
            func(*args, **kwargs)
        return wrapper
    return my_decorator

@decorator_with_args("hello", "world")
def say_greetings(greeting):
    print(greeting)

# This will print:
# Arguments for the decorator: hello, world
# greetings
say_greetings("greetings")
```

3. **Class Decorators**: You can also write decorators using classes. The class needs to implement `__call__` method.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class decorator running before the function call")
        self.func(*args, **kwargs)
        print("Class decorator running after the function call")

@MyDecorator
def say_bye():
    print("Bye!")

# This will print:
# Class decorator running before the function call
# Bye!
# Class decorator running after the function call
say_bye()
```

4. **Multiple Decorators**: You can apply multiple decorators to a function by stacking them on top of each other.

```python
@decorator_one
@decorator_two
def my_function():
    pass
```

The order in which the decorators are applied matters. `decorator_two` will be applied to the function first, and then `decorator_one` will be applied to the result of `decorator_two`.

Decorators are a form of metaprogramming and can be used to easily add functionality to existing functions or methods in a clean, readable way. They are widely used in web frameworks like Flask and Django for routing URLs to view functions, authentication, logging, and more.