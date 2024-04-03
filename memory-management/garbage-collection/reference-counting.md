---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/reference-counting.md
---

# Reference counting 
is a straightforward garbage collection technique that keeps track of the number of references to each object in memory. Here's how it works:

1. **Reference Count Initialization**: When an object is created, its reference count is initialized to 1.

2. **Incrementing the Reference Count**: Each time a new reference to the object is made (for example, when an object is assigned to a new variable or added to a data structure), the reference count is incremented.

3. **Decrementing the Reference Count**: When a reference to an object is removed (for example, when a variable goes out of scope or is reassigned to another object), the reference count is decremented.

4. **Deallocating the Object**: If the reference count of an object reaches zero, it means that there are no more references to the object, and it can be safely deallocated.

Here's a simple example in pseudocode to illustrate reference counting:

```pseudocode
class Object
    refCount = 0

function createObject()
    obj = new Object
    obj.refCount = 1
    return obj

function addReference(obj)
    obj.refCount += 1

function removeReference(obj)
    obj.refCount -= 1
    if obj.refCount == 0
        deallocate(obj)

function deallocate(obj)
    // Free the memory used by the object
```

Pros of Reference Counting:
- **Simple**: The concept is easy to understand and implement.
- **Immediate Reclamation**: Memory is reclaimed as soon as the last reference to an object is removed, which can be beneficial in managing memory in a predictable way.

Cons of Reference Counting:
- **Overhead**: Each object requires additional space to store the reference count, and there's a runtime cost to updating the reference count on every assignment or removal of a reference.
- **Cyclic References**: Reference counting cannot handle cyclic references where two or more objects reference each other but are no longer accessible from the root set. These objects will never have a reference count of zero, and thus will not be deallocated.
- **Fragmentation**: Since objects are deallocated individually, memory fragmentation can occur over time.

To address the issue of cyclic references, some systems that use reference counting also incorporate a cycle detection algorithm that runs periodically to identify and clean up these cycles. However, this adds complexity and overhead to the system.