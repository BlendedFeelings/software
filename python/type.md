---
b: https://blendedfeelings.com/software/python/type.md
---

# Types in Python 
refer to the classification of data items. It signifies the kind of value that tells what operations can be performed on a particular data. Here are the commonly used types in Python:

1. **int** - Integer type for whole numbers, e.g., `5`, `100`, `-3`.
2. **float** - Floating-point number, which is a number with a decimal point, e.g., `3.14159`, `-0.001`.
3. **str** - String type for text, e.g., `'hello'`, `"world"`.
4. **bool** - Boolean type with two possible values: `True` or `False`.
5. **list** - A mutable ordered collection of items, e.g., `[1, 2, 3]`, `['a', 'b', 'c']`.
6. **tuple** - An immutable ordered collection of items, e.g., `(1, 2, 3)`, `('a', 'b', 'c')`.
7. **dict** - Dictionary, a mutable collection of key-value pairs, e.g., `{'key1': 'value1', 'key2': 'value2'}`.
8. **set** - An unordered collection of unique items, e.g., `{1, 2, 3}`.

Python also supports more complex types such as:

- **complex** - For complex numbers, e.g., `1 + 2j`.
- **bytes** - Immutable sequence of bytes, e.g., `b'hello'`.
- **bytearray** - Mutable sequence of bytes.
- **memoryview** - A memory view object created from a bytearray or other binary sequence.

Python is a dynamically typed language, which means you do not need to explicitly declare the type of a variable when you create one. However, Python is also strongly typed, meaning that operations are type-specific and Python will not implicitly convert from one type to another.

Starting from Python 3.5, type hints can be used (PEP 484), which allows for the specification of expected types for variables, function arguments, and return values. This can help with static type checking, code readability, and maintenance.

For example:
```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

In this function, `a` and `b` are expected to be integers, and the function is expected to return an integer.

In Python, data types are categorized into two classes: mutable and immutable. Understanding the difference between these two types is crucial because it affects how you work with objects and how changes to data are handled within your code.

### Immutable Types:
Immutable objects cannot be changed after they are created. This means that any operation that tries to modify an immutable object will instead create a new object with the modified value.

Common immutable types in Python include:

- **int**: Integer numbers, e.g., `1`, `42`, `-10`
- **float**: Floating-point numbers, e.g., `3.14`, `-0.001`
- **complex**: Complex numbers, e.g., `2 + 3j`
- **bool**: Boolean values, `True` or `False`
- **str**: String objects, e.g., `"Hello, World!"`
- **tuple**: A sequence of objects, e.g., `(1, 2, 3)`
- **frozenset**: An immutable version of a set
- **bytes**: Immutable sequence of bytes, e.g., `b'hello'`

When you manipulate an immutable object, such as concatenating strings or adding to a number, you are actually creating a new object with the new value.

### Mutable Types:
Mutable objects can be changed after they are created. You can make modifications to parts of the object without creating a new one.

Common mutable types in Python include:

- **list**: An ordered collection of objects, e.g., `[1, 2, 3]`
- **set**: An unordered collection of unique objects, e.g., `{1, 2, 3}`
- **dict**: A collection of key-value pairs, e.g., `{'a': 1, 'b': 2}`
- **bytearray**: A mutable sequence of bytes, e.g., `bytearray(b'hello')`

With mutable types, you can change the contents (e.g., add, remove, or modify elements) without creating a new object. For example, if you append an element to a list, the list itself is updated and no new list is created.

Understanding the mutability of Python types is essential for writing efficient code and avoiding unintended side effects, especially when dealing with complex data structures or when passing objects as arguments to functions.