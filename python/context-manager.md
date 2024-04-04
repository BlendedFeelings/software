---
b: https://blendedfeelings.com/software/python/context-manager.md
---

# Context manager in Python
is a simple way to manage resources, ensuring that they are properly acquired and released. The most common use of a context manager is with the `with` statement, which is designed to make the setup and teardown of resources conveniently automatic.

A context manager is implemented by creating a class with `__enter__` and `__exit__` methods or by using the `contextlib` module which provides utilities like `contextmanager` decorator for a simpler way to create context managers without needing to create a class.

Here's an example of a context manager using a class:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        # Return an object if needed, otherwise return self or nothing
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Handle any exception that occurred within the block
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
            # Return True to suppress the exception, False otherwise
            return False

# Using the context manager
with MyContextManager():
    print("Inside the with block")

# Output:
# Entering the context
# Inside the with block
# Exiting the context
```

And here's an example using the `contextlib` module with a generator function:

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")

# Using the context manager
with my_context():
    print("Inside the with block")

# Output:
# Entering the context
# Inside the with block
# Exiting the context
```

In both examples, the code inside the `with` block is executed between the `__enter__` and `__exit__` methods or between the `yield` in the generator function. If an exception occurs inside the `with` block, it is passed to the `__exit__` method or the exception is handled in the `finally` block of the generator function. The context manager can then decide whether to handle the exception or let it propagate.