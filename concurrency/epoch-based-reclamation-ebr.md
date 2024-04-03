---
b: https://blendedfeelings.com/software/concurrency/epoch-based-reclamation-ebr.md
---

# Epoch-Based Reclamation (EBR) 
is a memory reclamation scheme used in concurrent programming to safely reclaim memory that is no longer in use by any thread. It is particularly useful in lock-free and wait-free data structures where it can be difficult to determine when it is safe to free memory because multiple threads may be accessing the data structure concurrently.

The basic idea behind EBR is to use epochs, which are essentially global counters, to track the progress of threads through critical sections of code. Here's how it generally works:

1. **Global Epoch Counter:** There is a global epoch counter that is incremented periodically.

2. **Per-Thread Epochs:** Each thread has a local epoch that indicates which epoch it is currently operating in.

3. **Entering a Critical Section:** When a thread wants to enter a critical section (e.g., to access a shared data structure), it first copies the global epoch to its local epoch. This signals that it is active and potentially accessing shared data.

4. **Exiting a Critical Section:** When the thread exits the critical section, it clears its local epoch, indicating it is no longer accessing shared data.

5. **Memory Reclamation:** When a thread wants to reclaim memory (i.e., free it), it can only do so if all active threads have a local epoch that is greater than the epoch in which the memory was allocated. This ensures that no active thread can still be accessing the memory.

6. **Retirement Lists:** To facilitate memory reclamation, threads maintain lists of retired memory that they want to free. This memory can only be reclaimed once it is safe to do so, as determined by the epochs.

7. **Quiescent States:** Threads periodically enter quiescent states where they update their local epochs to the current global epoch. This helps in advancing the system's state and making it possible to reclaim memory.

EBR is advantageous because it is relatively simple and has low overhead. However, it requires that threads periodically synchronize with the global epoch, which can be a challenge in some systems. Additionally, if threads are delayed or do not regularly enter quiescent states, memory reclamation can be stalled, leading to potential memory bloat.

EBR is one of several memory reclamation schemes, with others including hazard pointers, reference counting, and garbage collection. The choice of which to use depends on the specific requirements and constraints of the system being developed.