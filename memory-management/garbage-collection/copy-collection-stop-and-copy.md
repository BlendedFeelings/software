---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/copy-collection-stop-and-copy.md
---

# Copy Collection, often referred to as Stop-and-Copy garbage collection
is a technique that manages memory by copying live objects to a new space and leaving behind the space occupied by dead objects. This algorithm typically divides the available memory into two equal-sized spaces: the from-space and the to-space.

Here's how the Stop-and-Copy garbage collection algorithm works:

1. **Allocation**: Initially, all allocations are made in the from-space. The to-space remains empty.

2. **Garbage Collection Trigger**: Once the from-space is filled up, or a certain threshold is reached, the garbage collection process is triggered.

3. **Stop-the-World**: The algorithm typically requires a "stop-the-world" event, where the execution of the program is paused so that the garbage collection can occur without interference.

4. **Copying Live Objects**: The garbage collector starts at the root set (a set of pointers to live objects, such as global variables, stack frames, etc.) and copies each live object it finds from the from-space to the to-space. It also updates any references to the copied objects to point to the new locations.

5. **Updating References**: As objects are copied, references to them within other objects must be updated to point to the new location in the to-space.

6. **Transitive Closure**: The garbage collector recursively follows all references from the copied objects to find and copy all reachable objects. This process is known as computing the transitive closure of the live object graph.

7. **Swap Spaces**: Once all live objects have been copied and all references have been updated, the roles of the from-space and to-space are swapped. The new to-space (formerly the from-space) is now empty and ready for new allocations, while the old from-space (now the to-space) contains all the live objects.

8. **Resume Execution**: The program's execution is resumed with memory allocations now occurring in the new from-space.

Here's a simplified pseudocode representation of the Stop-and-Copy algorithm:

```pseudocode
function garbageCollect(rootSet)
    swap(fromSpace, toSpace)
    toSpacePointer = startOf(toSpace)

    for each pointer in rootSet
        if pointer points to fromSpace
            copyObject(pointer)

function copyObject(pointer)
    if object has not been copied
        newLocation = toSpacePointer
        toSpacePointer += sizeOf(object)
        copy object to newLocation
        update pointer to point to newLocation
        for each reference in object
            copyObject(reference)
```

Advantages of Stop-and-Copy GC:
- **Compaction**: As objects are copied, they are compacted in the to-space, which helps to reduce memory fragmentation and can improve cache performance.
- **Simplicity**: The algorithm is relatively simple and can be efficient for managing small to medium-sized heaps.

Disadvantages of Stop-and-Copy GC:
- **Memory Overhead**: The technique requires the heap to be divided into two halves, effectively reducing the available memory for the program by half.
- **Stop-the-World Pauses**: The entire program must be paused during the collection, which can lead to noticeable delays in program execution, especially if the heap is large.
- **Copying Overhead**: There is a cost associated with copying all live objects, which can be significant if there are many live objects or if the objects are large.