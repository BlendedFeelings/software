---
b: https://blendedfeelings.com/software/python/generator.md
---

# Generators in Python
are a simple way of creating iterators. A generator is a function that returns an iterator object which we can iterate over (one value at a time). The main feature that distinguishes a generator from a normal function is the presence of `yield` expressions.

Here's how a generator works:

1. When the generator function is called, it doesn't execute the function body immediately. Instead, it returns a generator object.
2. When the `__next__()` method of the generator object is called (which happens automatically in a `for` loop), the function body executes up to the next `yield` statement and produces a value.
3. When the function body executes a `yield` statement, the state of the generator function is "frozen," and the value to the right of the `yield` is returned to the caller.
4. On subsequent calls, execution resumes from the state it was left in (all local variables retain their information), and continues until it hits another `yield` statement.
5. This process continues until the function body terminates, at which point the generator raises a `StopIteration` exception, signaling that all values have been generated.

Here is an example of a simple generator function:

```python
def count_up_to(max_count):
    count = 1
    while count <= max_count:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)
```

When you run this code, you'll get the following output:

```
1
2
3
4
5
```

Each call to `next()` on the generator object returned by `count_up_to(5)` will execute the loop body until it hits the `yield` statement, at which point it will return the current value of `count` and pause. When `next()` is called again, it will resume where it left off and continue this process until `count` exceeds `max_count`.

Generators are particularly useful for large datasets because they allow you to iterate over data without the need to load the entire dataset into memory. This is known as "lazy evaluation."