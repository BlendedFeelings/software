---
b: https://blendedfeelings.com/software/concurrent-programming/monitor.md
---

# Monitors 
are a synchronization construct used in concurrent programming to control access to shared resources. They are designed to ensure that only one thread can execute a particular section of code at a time, thus preventing race conditions and ensuring data integrity.

### Characteristics of Monitors:
- **Mutual Exclusion**: Monitors enforce mutual exclusion by allowing only one thread at a time to execute any one of the monitor's methods.
- **Automatic Locking**: When a thread calls a method within a monitor, the monitor automatically locks, preventing other threads from entering any of the monitor's methods until the lock is released.
- **Condition Variables**: Monitors often provide condition variables, which allow threads to wait for certain conditions within the monitor to be true before continuing execution.
- **Signaling**: Threads can signal other threads waiting on a condition variable to wake up and recheck the condition.

### How Monitors Work:
1. **Entry**: When a thread attempts to execute a method within a monitor, it must first acquire the monitor's lock.
2. **Execution**: If the lock is available, the thread enters the method, and the monitor is considered occupied by that thread.
3. **Waiting (if necessary)**: If the thread cannot proceed due to some condition not being met, it can wait on a condition variable, releasing the lock temporarily.
4. **Signaling (if necessary)**: Another thread may signal the condition variable to wake up the waiting thread after changing the condition.
5. **Exit**: Once the thread has finished executing the method, it releases the lock, allowing other threads to enter the monitor.

### Example Usage:
Monitors are often used in object-oriented programming languages. For instance, in Java, the `synchronized` keyword can be used to turn a method into a monitor method:

```java
public class SharedResource {
    public synchronized void accessResource() {
        // Only one thread can execute this method at a time
    }
}
```

In this example, the `accessResource` method is a monitor method. When a thread calls this method, it acquires a lock associated with the `SharedResource` object. No other thread can call `accessResource` or any other `synchronized` method on the same object until the lock is released.

### Advantages of Monitors:
- **Simplicity**: Monitors provide a high-level abstraction that simplifies the synchronization of access to shared resources.
- **Safety**: By automatically handling the locking and unlocking, monitors can reduce the risk of programming errors such as forgetting to release a lock.
- **Encapsulation**: Monitors encapsulate both the shared resource and the synchronization mechanism, promoting good software design principles.

### Disadvantages of Monitors:
- **Limited Flexibility**: Monitors can be less flexible than other synchronization mechanisms, such as semaphores, which can handle more complex synchronization patterns.
- **Potential for Deadlock**: Incorrect use of monitors and condition variables can still lead to deadlocks if the signaling and waiting are not properly designed.

Monitors are a powerful tool for managing concurrency in shared-memory programming environments. They provide a structured way to ensure that only one thread can access a resource at a time, thus preventing concurrent access issues.