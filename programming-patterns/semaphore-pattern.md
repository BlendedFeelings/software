---
b: https://blendedfeelings.com/software/programming-patterns/semaphore-pattern.md
---

# Semaphore Pattern
is a synchronization construct that can be used to control access to a common resource by multiple processes in a concurrent system such as a multitasking operating system. A semaphore manages access to a resource by using a counter that represents the number of wake-ups pending for an object if the resource is already locked.

The semaphore pattern is often used to guard resources where the resource can only be used by a limited number of processes at a time. It is particularly useful in the case of limited resources, such as a pool of database connections or a limited number of licenses for a software application.

There are two main types of semaphores:

1. **Counting Semaphore**: This type of semaphore allows an arbitrary resource count. It can be used to control access to a pool of resources. The semaphore count indicates the number of resources available. When a process requests a resource, it performs a 'wait' operation that decrements the semaphore count. When a process releases a resource, it performs a 'signal' operation that increments the semaphore count.

2. **Binary Semaphore (or Mutex)**: This is a simplified version of a counting semaphore where the count is restricted to the values 0 and 1, which makes it essentially a lock. It can only be used for controlling access to a single shared resource. A binary semaphore is often referred to as a mutex (mutual exclusion object).

```java
class Semaphore
{
    int count = 5;
    Lock lock = new Lock();
    internal cv = new ConditionVariable(lock);

    void Acquire() {
        // Acquire a resource from the semaphore
        lock.Acquire()
        while count == 0:
            Wait()
        count -= 1
        lock.Release()
    }
    void Release() {
        // Release a resource back to the semaphore
        lock.Acquire()
        count += 1
        lock.Release()
    }
}
```