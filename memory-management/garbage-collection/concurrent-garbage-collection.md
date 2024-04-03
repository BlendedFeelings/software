---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/concurrent-garbage-collection.md
---

# Concurrent garbage collection 
is a technique designed to perform garbage collection in parallel with the execution of a program. The goal is to minimize pause times that affect the responsiveness of the application, which can be especially important for interactive or real-time systems. Concurrent garbage collectors aim to allow the program to continue running while most of the garbage collection work is being done, thus reducing the impact on the program's perceived performance.

Here's a general overview of how concurrent garbage collection works:

1. **Concurrent Marking**: The collector begins by marking reachable objects concurrently with the program's execution. This is done by starting at the root set (global variables, stack variables, CPU registers) and tracing all reachable objects. The marking phase is carefully managed to ensure that changes made by the program do not interfere with the garbage collector's ability to identify live objects.

2. **Write Barrier**: To handle changes in the object graph while the collector is running, a write barrier is used. This mechanism tracks updates to object references during the concurrent marking phase. When the program writes to a reference field of an object, the write barrier ensures that the referenced objects are marked or re-marked if necessary.

3. **Concurrent Sweeping**: After the marking phase is complete, the collector can sweep the heap to reclaim memory from dead objects. This phase can also be done concurrently, with the collector identifying and freeing unmarked objects while the program continues to run.

4. **Synchronization Points**: Although most of the work is done concurrently, there may still be brief synchronization points where the program must be paused. These pauses are typically much shorter than those required by non-concurrent collectors and are necessary to ensure a consistent view of the object graph for both the collector and the program.

5. **Finalization**: Some objects may require special handling before their memory can be reclaimed, such as invoking finalizers or destructors. This is often done during a separate phase that may require coordination with the running program.

Here's a simplified pseudocode representation of the concurrent collection process:

```pseudocode
function concurrentGarbageCollect()
    startConcurrentMarking()
    while programIsRunning
        if writeBarrierNeeded()
            applyWriteBarrier()
        if programChangesDetected()
            updateMarking()
    endConcurrentMarking()
    startConcurrentSweeping()
    while programIsRunning
        performConcurrentSweepingIncrement()
    handleFinalization()

function startConcurrentMarking()
    // Begin marking objects concurrently with program execution

function applyWriteBarrier()
    // Handle updates to object references

function updateMarking()
    // Re-mark objects as needed based on program changes

function endConcurrentMarking()
    // Finish the marking phase

function startConcurrentSweeping()
    // Begin sweeping unmarked objects concurrently

function performConcurrentSweepingIncrement()
    // Sweep a subset of objects and reclaim memory

function handleFinalization()
    // Finalize and reclaim objects that require special handling
```

Advantages of Concurrent GC:
- **Reduced Pause Times**: Concurrent garbage collection significantly reduces the length of pauses, improving the responsiveness of the application.
- **Smooth Performance**: By distributing the work of garbage collection over time, concurrent collectors can provide a smoother performance profile.

Disadvantages of Concurrent GC:
- **Complexity**: Implementing a concurrent garbage collector is complex due to the need to handle interactions between the collector and the running program.
- **CPU Overhead**: Running the garbage collector in parallel with the program can increase CPU usage, potentially affecting the program's performance.
- **Potential Memory Overhead**: To manage the concurrent collection, additional memory may be required for the write barrier and other bookkeeping structures.

Concurrent garbage collection is often used in modern high-performance systems, such as server environments and applications with stringent responsiveness requirements. It is a feature of advanced garbage collectors found in languages like Java (G1 GC, ZGC, Shenandoah) and .NET (Concurrent GC).