---
b: https://blendedfeelings.com/software/python/class-property.md
---

# Class properties
are a way of customizing access to instance attributes. They are created with the `property` decorator, which allows you to define methods in a class that can be accessed like attributes, but with additional logic for getting, setting, or deleting the value.

Here's a basic example of how to define and use properties in a Python class:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be non-negative")

    @radius.deleter
    def radius(self):
        del self._radius

# Usage
c = Circle(5)
print(c.radius)  # This calls the radius getter

c.radius = 10   # This calls the radius setter and updates the value
print(c.radius)

# c.radius = -1  # This would raise a ValueError due to the setter's validation

# del c.radius   # This calls the radius deleter
```

In this example, `_radius` is a private attribute that should not be modified directly outside the class. The `radius` property allows controlled access to this attribute:

- The `@property` decorator is used to define the getter method, which simply returns the value of `_radius`.
- The `@radius.setter` decorator is used to define the setter method, which includes validation to ensure the radius is non-negative before setting the `_radius` attribute.
- The `@radius.deleter` decorator is used to define the deleter method, which allows for the deletion of the `_radius` attribute.