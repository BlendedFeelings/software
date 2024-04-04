---
b: https://blendedfeelings.com/software/python/iterable.md
---

# Iterables in Python
are objects that can be iterated over. An iterable can be a collection of items, such as a list, tuple, dictionary, set, or string. Anything that can be looped over with a `for` loop is an iterable. Iterables can also be objects that are not collections but still can return one item at a time in the context of an iteration, such as generators and file objects.

Here are some examples of iterables in Python:

### Lists
```python
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
```

### Tuples
```python
my_tuple = (1, 2, 3, 4)
for item in my_tuple:
    print(item)
```

### Dictionaries
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)  # Prints the keys
for value in my_dict.values():
    print(value)  # Prints the values
for key, value in my_dict.items():
    print(key, value)  # Prints keys and values
```

### Sets
```python
my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)
```

### Strings
```python
my_string = "Hello"
for char in my_string:
    print(char)
```

### Generators
Generators are a special type of iterator that generate values on the fly and can be iterated over once.
```python
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
```

### Files
Files in Python are also iterables, and you can iterate over each line in a file.
```python
with open('my_file.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Prints each line without newline characters
```

To check if an object is iterable, you can use the `iter()` function. If `iter(obj)` does not raise a `TypeError`, then the object is iterable.

```python
obj = [1, 2, 3]
try:
    iterator = iter(obj)
    print("The object is iterable")
except TypeError:
    print("The object is not iterable")
```

Iterables are a core concept in Python and are widely used throughout the language and its standard library.