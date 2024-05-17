---
b: https://blendedfeelings.com/software/concurrent-programming/busy-waiting.md
---

# Busy-waiting 
(also known as spinning) refers to a technique where a thread repeatedly checks for a condition to become true without relinquishing control of the processor. This means that the thread is actively using CPU cycles while it waits, as opposed to yielding its time slice and allowing the system to switch to another thread or process.

Busy-waiting is generally considered an inefficient use of CPU resources because it does not allow the system to perform other tasks that could be using the CPU while the waiting thread has nothing productive to do. However, there are some scenarios where busy-waiting may be used:

- When the wait time is expected to be very short, and the overhead of context switching (the process of storing and restoring the state of a thread so that execution can be resumed from the same point later) is greater than the time spent busy-waiting.
- In real-time systems where a predictable response time is more important than CPU efficiency.
- On systems with multiple processors or cores, where one thread can busy-wait without hindering the progress of other threads significantly.

In general, it's preferable to use other synchronization mechanisms provided by the concurrent programming framework or the operating system, such as mutexes, semaphores, events, or condition variables. These constructs are designed to allow threads to wait for conditions without consuming CPU cycles, by putting the waiting thread in a non-runnable state until the condition is met.

Here's a simple example of busy-waiting in pseudocode:

```plaintext
while not condition:
    // Do nothing, just loop
```

In this example, the thread will continue to check the `condition` in a loop without doing anything else. This will use CPU cycles until the condition becomes true.

A better approach in many cases would be to use a synchronization construct like a condition variable:

```plaintext
lock.acquire()
while not condition:
    condition_variable.wait(lock)  // Release lock and wait to be notified
lock.release()
```

In this example, the thread will release the lock and suspend execution, allowing other threads to run, until it is notified that the condition may be true, at which point it will re-acquire the lock and check the condition again. This is a more efficient use of CPU resources.