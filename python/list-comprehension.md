---
b: https://blendedfeelings.com/software/python/list-comprehension.md
---

# List comprehensions in Python
provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

A basic list comprehension looks like this:

```python
new_list = [expression for item in iterable]
```

Here's a breakdown of the list comprehension components:

- `new_list`: The new list that is being created.
- `expression`: The expression that defines how each item in the new list is calculated or transformed.
- `for item in iterable`: A `for` loop that iterates over each element in the iterable.

You can also add an optional condition at the end:

```python
new_list = [expression for item in iterable if condition]
```

Here, `condition` is a boolean expression that filters out items from the original iterable. Only items for which the condition is `True` are included in the new list.

Here are a few examples to illustrate list comprehensions:

1. Create a list of squares for numbers from 0 to 9:

```python
squares = [x**2 for x in range(10)]
```

2. Create a list of tuples (number, square) for numbers from 0 to 9:

```python
squares_tuples = [(x, x**2) for x in range(10)]
```

3. Filter a list to exclude negative numbers:

```python
numbers = [34, -2, -11, 29, 47, -5]
positive_numbers = [x for x in numbers if x >= 0]
```

4. Apply a function to all items in a list (e.g., converting strings to uppercase):

```python
strings = ["hello", "world", "python", "list"]
uppercase_strings = [s.upper() for s in strings]
```

5. Flatten a list of lists:

```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
```

List comprehensions can be a more readable and efficient way to create lists compared to using loops and the `append()` method.