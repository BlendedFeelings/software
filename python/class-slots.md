---
b: https://blendedfeelings.com/software/python/class-slots.md
---

# Class __slots__ in Python 
is a special attribute that you can define in a class to declare a fixed set of attributes. Using `__slots__` can lead to performance improvements and memory savings because it prevents the creation of a `__dict__` for each instance of the class, which is the usual mechanism for storing an object's attributes.

When you define `__slots__`, you are effectively telling Python not to use a dynamic dictionary, and instead to use a static, more compact array-like structure for attribute storage. This can be particularly useful when you are creating a large number of instances of a class and each instance only has a small number of attributes.

Here's an example of how to use `__slots__` in a Python class:

```python
class Point:
    __slots__ = ('x', 'y')  # Declare allowed attributes

    def __init__(self, x, y):
        self.x = x  # Assign value to 'x' slot
        self.y = y  # Assign value to 'y' slot

# Create an instance of Point
p = Point(1, 2)
print(p.x, p.y)  # Outputs: 1 2

# Trying to add a new attribute will raise an AttributeError
# p.z = 3  # Uncommenting this line will cause an error
```

A few things to keep in mind when using `__slots__`:

1. You can only assign values to the names defined in `__slots__`. Attempting to assign a value to an undeclared name will raise an `AttributeError`.
2. If you inherit from a class without `__slots__`, the derived class will still have a `__dict__` attribute unless it also defines `__slots__`.
3. Special methods like `__dict__` and `__weakref__` are not created for instances of the class. If you need these, you must include them in the `__slots__` declaration.
4. When using `__slots__`, you should be aware that it may complicate class inheritance and the use of certain Python features like dynamic attribute assignment and multiple inheritance. Use it when you clearly understand the trade-offs and when the benefits outweigh the limitations.