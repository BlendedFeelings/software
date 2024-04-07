---
b: https://blendedfeelings.com/software/concurrent-programming/mutex.md
---

# Mutexes (short for mutual exclusions) 
are synchronization primitives used in concurrent programming to protect shared resources from being accessed by multiple threads simultaneously, which could lead to race conditions and inconsistent states.

### Characteristics of Mutexes:
- **Ownership**: Mutexes have the concept of ownership; that is, a thread must acquire a mutex before it can enter the critical section, and it must release the mutex when it leaves the critical section.
- **Blocking**: If a thread attempts to acquire a mutex that is already held by another thread, it will block (wait) until the mutex is released.
- **Non-shareable**: A mutex is a non-shareable resource, meaning that only one thread can hold it at a time.
- **Reentrancy**: Some mutexes are reentrant or recursive, allowing the same thread to acquire the mutex multiple times without causing a deadlock, provided that the thread releases the mutex an equal number of times.

### How Mutexes Work:
1. **Locking**: A thread attempts to lock the mutex before entering a critical section. If the mutex is already locked by another thread, the requesting thread will block until the mutex becomes available.
2. **Critical Section**: Once the mutex is locked, the thread enters the critical section where it can safely access or modify shared resources.
3. **Unlocking**: After the thread has finished executing the critical section, it unlocks the mutex, allowing other threads to acquire it and enter the critical section.

### Example Usage:
Mutexes are often used in various programming languages to ensure safe access to shared resources. Here's an example in C++ using the Standard Library:

```cpp
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx; // Mutex for critical section

void printNumbers() {
    mtx.lock(); // Acquire the mutex
    for (int i = 0; i < 5; ++i) {
        std::cout << i << std::endl;
    }
    mtx.unlock(); // Release the mutex
}

int main() {
    std::thread t1(printNumbers);
    std::thread t2(printNumbers);
    t1.join();
    t2.join();
    return 0;
}
```

In this example, the `mtx` mutex ensures that the `printNumbers` function is not executed by `t1` and `t2` simultaneously, thus preventing a race condition.

### Advantages of Mutexes:
- **Simplicity**: Mutexes provide a simple and clear way to protect critical sections.
- **Safety**: When used correctly, mutexes prevent concurrent access to shared resources.
- **Flexibility**: Mutexes can be used in various scenarios, from protecting simple data structures to coordinating complex interactions between threads.

### Disadvantages of Mutexes:
- **Deadlock**: Incorrect use of mutexes can lead to deadlocks, especially if multiple mutexes are acquired in different orders by concurrent threads.
- **Performance**: Overuse of mutexes can lead to performance bottlenecks due to threads spending time waiting to acquire locks.
- **Error-Prone**: Programmers must ensure that mutexes are correctly locked and unlocked, which can be error-prone in complex systems.

Mutexes are a fundamental tool in multithreaded programming for ensuring that only one thread at a time can access a particular piece of data or code. Proper use of mutexes can help prevent data corruption and ensure the integrity of shared resources in concurrent applications.