---
b: https://blendedfeelings.com/software/python/slicing.md
---

# Slicing in Python 
is a feature that allows you to extract a portion of a sequence by specifying a start, stop, and step index. Slicing can be used on sequences such as strings, lists, tuples, and other objects that support the sequence protocol.

Here's the general syntax for slicing:

```python
sequence[start:stop:step]
```

- `start` (optional): The starting index of the slice. It defaults to `0`. This is the index of the first item to include in the slice.
- `stop` (optional): The ending index of the slice. It defaults to the length of the sequence. This is the index of the first item not to include in the slice.
- `step` (optional): The step size of the slice. It defaults to `1`. This determines the increment between each index in the slice.

Here are some examples using slicing on a Python list:

```python
# A sample list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get a slice from index 2 to 5
slice1 = my_list[2:6]  # Output: [2, 3, 4, 5]

# Get a slice from the beginning to index 5
slice2 = my_list[:6]   # Output: [0, 1, 2, 3, 4, 5]

# Get a slice from index 3 to the end
slice3 = my_list[3:]   # Output: [3, 4, 5, 6, 7, 8, 9]

# Get a slice of the whole list
slice4 = my_list[:]    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get a slice with a step of 2
slice5 = my_list[::2]  # Output: [0, 2, 4, 6, 8]

# Get a slice in reverse
slice6 = my_list[::-1] # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Get a slice with negative indices
slice7 = my_list[-5:-2] # Output: [5, 6, 7]
```

Negative indices count from the end of the sequence, with `-1` being the last item, `-2` the second to last, and so on.

Remember that slicing a sequence in Python creates a new object that is a shallow copy of the portion of the original sequence.