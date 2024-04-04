---
b: https://blendedfeelings.com/software/python/garbage-collection.md
---

# Garbage collection in Python
is the process of automatically freeing up memory by deleting objects that are no longer in use by a program. Python uses a form of automatic memory management known as reference counting, as well as a cyclic garbage collector for collecting objects that contain circular references.

Here's a brief overview of how garbage collection works in Python:

1. **Reference Counting:** Each object in Python has a reference count, which is the number of references pointing to it. When an object is created, its reference count is set to one. When a new reference is created to the object, the count is incremented, and when a reference is deleted, the count is decremented. When an object's reference count reaches zero, meaning no references point to it, Python's memory manager automatically deallocates the object, freeing up the memory.

2. **Cyclic Garbage Collector:** Reference counting alone cannot handle circular references (where two or more objects reference each other, creating a loop). Python's cyclic garbage collector is used to detect these kinds of reference cycles and delete the objects involved, even if their reference counts are not zero. This collector runs periodically during program execution.

The `gc` module in Python provides an interface to the garbage collection facility. Some useful functions in the `gc` module are:

- `gc.collect()`: Forces a garbage collection process.
- `gc.get_objects()`: Returns a list of all objects tracked by the garbage collector.
- `gc.set_debug()`: Set the garbage collection debugging flags.
- `gc.get_stats()`: Returns a list of dictionaries containing per-generation statistics.

Here's an example of how to use the `gc` module:

```python
import gc

# Check if garbage collection is enabled
print(gc.isenabled())

# Disable garbage collection
gc.disable()

# Perform some memory-intensive operations
# ...

# Re-enable garbage collection
gc.enable()

# Force a garbage collection
gc.collect()

# Get information about objects tracked by the garbage collector
for obj in gc.get_objects():
    print(type(obj), id(obj))
```

It's important to note that in most Python programs, garbage collection works seamlessly without the need for explicit intervention by the programmer. However, understanding how it works can be useful, especially when dealing with large data sets or when optimizing performance.