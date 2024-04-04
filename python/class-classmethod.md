---
b: https://blendedfeelings.com/software/python/class-classmethod.md
---

# Class @classmethod 
is a method that's bound to the class and not the instance of the class. This means that a class method can be called on the class itself, rather than on an instance of the class. It receives the class as the implicit first argument, conventionally named `cls`, just as an instance method receives the instance as the first argument, conventionally named `self`.

To define a class method, you use the `@classmethod` decorator. Here's an example:

```python
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Usage
print(MyClass.get_count())  # Outputs: 0
instance = MyClass()
print(MyClass.get_count())  # Outputs: 1
```

In this example, `get_count` is a class method that returns the value of the class variable `count`. Notice how we can call `get_count` using the class name `MyClass` directly, without needing to create an instance of the class. When we do create an instance, the `__init__` method increments the `count`, and we can see the updated count by calling the class method again.

Class methods are often used as factory methods that can create class instances with different initial configurations, or to implement alternative constructors. They can also be useful for creating singleton patterns, modifying class state, or working with class variables.