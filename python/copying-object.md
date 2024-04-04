---
b: https://blendedfeelings.com/software/python/copying-object.md
---

# Copying object in Python
can be done in two ways: shallow copy and deep copy. These concepts are important when dealing with mutable objects (like lists, dictionaries, etc.) where you want to duplicate the objects without affecting the original one.

### Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements. So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy of the object itself is created, but the elements within the object are not copied; they are referenced to the original object.

You can create a shallow copy using the `copy` module's `copy()` function:

```python
import copy

original_list = [1, 2, [3, 4], 5]
shallow_copied_list = copy.copy(original_list)
```

In this example, modifying `shallow_copied_list[2][0]` would also change `original_list[2][0]` because the inner list `[3, 4]` is not copied but referenced.

### Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements. Thus, the copied object has no reference to the original object.

You can create a deep copy using the `copy` module's `deepcopy()` function:

```python
import copy

original_list = [1, 2, [3, 4], 5]
deep_copied_list = copy.deepcopy(original_list)
```

In this example, modifying `deep_copied_list[2][0]` would not affect `original_list[2][0]` because a deep copy creates a new list `[3, 4]` with no references to the original inner list.

### When to Use Shallow vs Deep Copy
- Use a **shallow copy** when you want to create a new collection object and you are fine with having references to the objects found in the original.
- Use a **deep copy** when you want to copy an object along with all of the objects to which it refers recursively.

Keep in mind that deep copying an object can be slower and may require more memory. It is also not always possible to deep copy an object if it contains non-copyable objects like file handles, sockets, etc.