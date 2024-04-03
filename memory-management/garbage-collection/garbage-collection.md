---
b: https://blendedfeelings.com/software/memory-management/garbage-collection/garbage-collection.md
---

# Garbage collection (GC) 
is the process of automatically reclaiming memory that is no longer in use by the program. This helps to prevent memory leaks and other memory-related problems. There are several algorithms used for garbage collection, each with its own set of trade-offs. Here are some of the most commonly used garbage collector algorithms:

1. **Reference Counting**: This is one of the simplest forms of garbage collection. Each object has a reference count which is incremented when a reference to it is created and decremented when a reference is removed. When the reference count drops to zero, the object can be safely deallocated. However, reference counting can't handle cyclic references where two or more objects reference each other but are no longer in use.

2. **Mark-and-Sweep**: This algorithm consists of two phases. In the "mark" phase, the garbage collector traverses the object graph starting from the root set (objects known to be in use) and marks all reachable objects. In the "sweep" phase, it scans the memory for unmarked objects and deallocates them. This method can handle cyclic references but can cause program pauses.

3. **Copy Collection (Stop-and-Copy)**: The memory is divided into two halves, and at any time, only one half is used. When garbage collection occurs, live objects are copied from the current half to the other half, compacting them in the process. After copying, the roles of the halves are switched. This algorithm is simple and can lead to better cache performance due to compaction but wastes half of the memory.

4. **Generational Collection**: This is based on the observation that most objects die young. Memory is divided into generations, typically a young generation and an old generation. New objects are allocated in the young generation, and objects that survive several collections are promoted to the old generation. Collecting the young generation is fast and happens frequently, while collecting the old generation is more expensive and happens less often.

5. **Incremental Collection**: This approach aims to reduce the pause time caused by garbage collection by breaking up the work into smaller increments. The garbage collector does a little bit of work at a time, interleaved with the program's execution.

6. **Concurrent Collection**: Concurrent garbage collectors run in parallel with the program, reducing pause times. They are designed to work without stopping the application, making them suitable for real-time systems.

7. **Region-Based Collection**: Memory is divided into regions, and objects are allocated within these regions. Regions that contain only unreachable objects can be reclaimed entirely, which can be more efficient than dealing with individual objects.

Each garbage collection algorithm has its strengths and weaknesses, and the choice of which to use depends on the requirements of the application and the environment in which it runs. For example, real-time systems may prefer concurrent collectors to avoid pauses, while batch processing systems might opt for a simple mark-and-sweep or generational collector.