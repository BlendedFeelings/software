---
b: https://blendedfeelings.com/software/python/metaclass.md
---

# Metaclass in Python
is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A metaclass in Python is most commonly used for creating APIs, enforcing coding standards, or adding new class behavior.

The default metaclass in Python is `type`. However, you can define your own metaclass by subclassing `type` and then using it to create new classes.

Here's an example of how to create a metaclass and use it:

```python
# Define a metaclass
class MyMeta(type):
    # A metaclass can define methods like a normal class
    def __new__(cls, name, bases, dct):
        # This is the method that actually creates the class
        # You can modify the class dictionary before the class is created
        dct['class_created_by'] = 'MyMeta'
        return super().__new__(cls, name, bases, dct)

    def __init__(self, name, bases, dct):
        # This method is called after the class is created
        super().__init__(name, bases, dct)

# Use the metaclass to create a class
class MyClass(metaclass=MyMeta):
    pass

# The MyClass is now an instance of MyMeta, and it has an attribute set by the metaclass
print(MyClass.class_created_by)  # Output: MyMeta
```

In the above example, `MyMeta` is a metaclass that inherits from `type`. It overrides the `__new__` method to add a new attribute to the class dictionary before the class is created. When `MyClass` is defined with `metaclass=MyMeta`, Python uses `MyMeta` to create `MyClass`.

Metaclasses are an advanced feature of Python and should be used with care. They can make the code more complex and harder to understand, so they are generally only used in cases where the benefits outweigh these downsides.