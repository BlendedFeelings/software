---
b: https://blendedfeelings.com/software/python/descriptor-protocol.md
---

# Descriptor 
is a protocol that allows you to customize the behavior of how attributes are accessed within an object. Descriptors are implemented using at least one of the methods in the descriptor protocol: `__get__`, `__set__`, and `__delete__`. These methods are used to manage the attributes of an object.

Here is a brief overview of the descriptor protocol methods:

- `__get__(self, instance, owner)`: This method is called to get the value of the attribute. `instance` is the instance of the owner class, and `owner` is the owner class itself.
- `__set__(self, instance, value)`: This method is called to set the value of the attribute on an instance. `instance` is the instance of the owner class, and `value` is the value to set.
- `__delete__(self, instance)`: This method is called to delete the attribute from an instance. `instance` is the instance of the owner class.

To create a descriptor, you define a class that implements any of these methods. Here's a simple example of a descriptor that implements the `__get__` and `__set__` methods:

```python
class RevealAccess:
    """A data descriptor that sets and returns values
       normally and prints a message logging their access."""
       
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print(f'Getting: {self.name}')
        return self.val

    def __set__(self, obj, val):
        print(f'Setting: {self.name} to {val}')
        self.val = val

class MyClass:
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
print(m.x)   # Accessing the value, triggers __get__
m.x = 20     # Assigning a value, triggers __set__
print(m.x)   # Accessing the updated value, triggers __get__
```

In this example, `RevealAccess` is a descriptor class that logs when its value is accessed or modified. The `MyClass` class has an attribute `x` that is an instance of `RevealAccess`. Accessing or modifying `m.x` will trigger the `__get__` and `__set__` methods of the descriptor, respectively.

Descriptors are a low-level mechanism that underpins properties, methods, static methods, class methods, and `super()`. They are a powerful feature of Python that enables advanced object-oriented programming techniques.