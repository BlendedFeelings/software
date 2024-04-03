---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/mark-and-sweep.md
---

# Mark-and-Sweep algorithm 
is a fundamental garbage collection technique that is used to identify and free unused objects in dynamic memory management. This algorithm operates in two distinct phases: the "mark" phase and the "sweep" phase.

Here's a step-by-step explanation of how the Mark-and-Sweep algorithm works:

1. **Mark Phase**:
   - The garbage collector starts at the root set, which includes global variables, stack variables, and CPU registers that can reference objects in the heap.
   - It traverses all reachable objects starting from the root set, following each object's references to other objects recursively. This is known as tracing the object graph.
   - As each object is reached, it is marked to indicate that it is in use and should not be collected.

2. **Sweep Phase**:
   - After all reachable objects have been marked, the garbage collector scans through the entire heap.
   - It looks for objects that have not been marked, which means they are not reachable and therefore can be considered garbage.
   - The memory occupied by these unmarked objects is then reclaimed, and the objects are effectively deleted.
   - The marks on the reachable objects are cleared in preparation for the next garbage collection cycle.

Here is a simplified pseudocode representation of the Mark-and-Sweep algorithm:

```pseudocode
function markAndSweep(rootSet)
    // Mark phase
    for each object in rootSet
        mark(object)
    
    // Sweep phase
    for each object in heap
        if not marked(object)
            reclaim(object)
        else
            unmark(object)

function mark(object)
    if not marked(object)
        setMark(object)
        for each child in references(object)
            mark(child)

function reclaim(object)
    // Free the memory used by the object
```

Advantages of Mark-and-Sweep GC:
- **No Memory Overhead**: Unlike the Stop-and-Copy algorithm, Mark-and-Sweep does not require dividing the heap into multiple regions, so there is no memory wasted on an unused space.
- **Handles Cycles**: The algorithm can handle cyclic references, which can be problematic for reference counting algorithms.
- **No Object Movement**: Objects are not moved in memory, which means that there is no need to update references to moved objects.

Disadvantages of Mark-and-Sweep GC:
- **Stop-the-World**: The algorithm typically requires stopping the program execution while the garbage collection is in progress, which can lead to pauses that affect the responsiveness of the application.
- **Memory Fragmentation**: Since objects are not moved, memory can become fragmented over time, which might lead to inefficient use of memory and the inability to allocate large objects even if there is enough free memory in total.
- **Overhead**: The process of marking and sweeping all objects can be time-consuming, especially for large heaps with many objects.

The Mark-and-Sweep algorithm has been refined and improved over the years. Modern garbage collectors often use variations of this algorithm, such as generational collectors and concurrent collectors, to mitigate the disadvantages and improve performance.