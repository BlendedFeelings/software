---
b: https://blendedfeelings.com/software/concurrency/quiescent-state-based-reclamation-qsbr.md
---

# Quiescent State Based Reclamation (QSBR) 
is a technique used in concurrent programming to safely reclaim memory that may be accessed by multiple threads without the need for explicit synchronization mechanisms such as locks or atomic operations. This method is particularly useful in read-mostly data structures where the overhead of synchronization can significantly affect performance.

The basic idea of QSBR is to delay the reclamation of memory until it is safe to assume that no threads are accessing the old version of the data. To achieve this, the system must ensure that all threads have passed through a quiescent state—a point where they are guaranteed not to hold any references to the objects that are to be reclaimed.

Here's an overview of how QSBR typically works:

1. **Update Phase**: When a thread wants to update a shared data structure, it makes a new version of the relevant part of the data structure. This ensures that readers can still access the old version while the update is taking place.

2. **Publishing**: The new version is then published, often by updating a pointer, so that subsequent readers will see the new version.

3. **Quiescent States**: Threads periodically enter quiescent states. A quiescent state is a point in a thread's execution where it is known not to be accessing any shared data structures that are subject to reclamation. For example, a thread might enter a quiescent state when it is idle, or after it has finished processing a batch of work.

4. **Reclamation**: Once all threads have passed through a quiescent state since the last update was published, it is safe to reclaim the memory used by the old version of the data structure. This is because no thread can be accessing the old version anymore.

5. **Grace Period**: The period between the publication of a new version and the reclamation of the old version is known as the grace period. The system must track when threads enter and exit quiescent states to determine when the grace period has ended.

QSBR is often used in conjunction with epoch-based reclamation systems, where the system keeps track of "epochs" to know which objects are safe to reclaim. Each thread maintains its current epoch, and when a thread enters a quiescent state, it updates its epoch to the global one.

One of the challenges of QSBR is ensuring that all threads frequently enter quiescent states. If a thread is delayed or fails to enter a quiescent state, it can prevent the reclamation of memory, leading to memory leaks. Therefore, it's important for the system to handle cases where threads are preempted or otherwise delayed for long periods.

QSBR is a low-overhead method for memory reclamation that is particularly well-suited for read-heavy workloads. However, it requires careful design to ensure that quiescent states are reached regularly and that the system can handle edge cases appropriately.