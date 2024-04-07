---
b: https://blendedfeelings.com/software/concurrent-programming/context-switching.md
---

# Context switching 
is a fundamental feature of modern multitasking operating systems. It allows a single CPU to be shared among multiple processes or threads by switching the CPU's attention from one process to another. This creates the illusion of parallelism and enables the concurrent execution of multiple tasks.

Here's how context switching works and its implications in concurrent programming:

### How Context Switching Works

1. **Saving State**: When the operating system decides to perform a context switch, it first saves the state (context) of the currently running process or thread. This state typically includes the CPU registers, program counter, stack pointer, and other processor state information.

2. **Selecting a New Process**: The scheduler, a component of the operating system, selects a new process or thread to run. The selection is based on scheduling algorithms, which can consider factors like priority, fairness, and process behavior.

3. **Restoring State**: The state of the new process or thread is then restored. This means loading its previously saved context into the CPU registers and other relevant areas so that execution can resume where it left off.

4. **Resuming Execution**: Once the new context is loaded, the CPU begins executing the new process or thread.

### Implications in Concurrent Programming

- **Overhead**: Context switching is not free; it incurs overhead because of the time taken to save and restore states, as well as the potential for cache and memory performance penalties. This overhead can affect the performance of a system, especially if context switches occur frequently.

- **Concurrency Management**: Developers must design software with the understanding that context switches can happen at almost any time. This requires careful management of shared resources to avoid race conditions, deadlocks, and other concurrency issues.

- **Synchronization**: Synchronization primitives such as mutexes, semaphores, and condition variables are used to manage access to shared resources and ensure that context switches do not lead to inconsistent states.

- **Non-Determinism**: The non-deterministic nature of context switching, due to its dependency on the scheduler and system load, can make debugging and testing concurrent programs more challenging.

- **Real-Time Considerations**: In real-time systems, the timing of context switches is critical. Real-time operating systems often provide guarantees about the maximum time it will take to switch contexts, which is important for meeting timing constraints.

- **Thread vs. Process Switching**: Context switching between threads of the same process is generally faster than between processes, as threads share the same memory space and therefore require less state to be saved and restored.

- **User vs. Kernel Mode**: Context switches can also occur when transitioning between user mode and kernel mode within a single process, such as when a system call is made.

In summary, context switching is a key mechanism that enables concurrent programming by allowing multiple processes or threads to share a single CPU. However, it introduces complexity in the form of overhead and the need for careful synchronization to ensure correct program behavior.