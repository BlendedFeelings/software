---
b: https://blendedfeelings.com/software/python/class-dict.md
---

# Class __dict__ in Python 
is a special attribute that is a dictionary or other mapping object used to store an object’s (writable) attributes.

Here's a simple example to illustrate the use of `__dict__`:

```python
class ExampleClass:
    def __init__(self, value):
        self.value = value

# Create an instance of ExampleClass
example = ExampleClass(10)

# Access the __dict__ attribute
print(example.__dict__)
```

The output of this code would be:

```
{'value': 10}
```

This shows that the `example` object has an attribute `value`, which is stored in its `__dict__` with the corresponding value of `10`.

Instances of custom classes have a `__dict__` attribute by default. However, built-in types like lists and integers do not have a `__dict__` attribute because their attributes are stored in a more compact way that cannot be modified at runtime.

You can also use `__dict__` to dynamically add or modify attributes of an object:

```python
# Add a new attribute to example using __dict__
example.__dict__['new_attribute'] = 'New Value'

print(example.new_attribute)  # Output: New Value
```

Keep in mind that direct manipulation of `__dict__` is not common practice and should be done with care, as it can lead to unexpected behavior if not handled properly. It's generally better to use the built-in functions `getattr`, `setattr`, and `delattr` to get, set, and delete attributes, respectively.