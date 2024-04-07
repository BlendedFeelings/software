---
b: https://blendedfeelings.com/software/concurrent-programming/semaphore.md
---

# Semaphore 
are synchronization primitives used in concurrent programming to control access to shared resources by multiple processes or threads. A semaphore manages an internal counter that is decremented when a process or thread acquires the semaphore (often referred to as a "P" operation or "wait") and is incremented when the semaphore is released ("V" operation or "signal"). The value of the counter represents the number of resources or slots available.

There are two main types of semaphores:

### Binary Semaphore (or Mutex):
- Acts similarly to a mutex and is used to ensure mutual exclusion.
- The internal counter can only be 0 or 1, indicating whether the resource is available.
- When a thread acquires the semaphore, the counter is set to 0, and when the thread releases the semaphore, the counter is set to 1.

### Counting Semaphore:
- Allows multiple threads to access a finite pool of resources.
- The internal counter represents the number of available resources.
- Threads can acquire the semaphore if the counter is greater than 0, and each acquisition decreases the counter by one.
- When a thread releases the semaphore, the counter is incremented, signaling that a resource has become available.

### How Semaphores Work:
1. **Initialization**: A semaphore is initialized with a specific count representing the number of resources available.
2. **Acquisition (Wait, P operation)**: A thread performs a wait operation to acquire the semaphore. If the semaphore's count is greater than zero, the count is decremented, and the thread proceeds. If the count is zero, the thread blocks until a resource becomes available.
3. **Release (Signal, V operation)**: A thread performs a signal operation to release the semaphore, incrementing the count. If other threads are waiting, one of them will be unblocked and allowed to acquire the semaphore.

### Example Usage:
In many programming languages, semaphores are provided as part of the standard library or through external libraries. Here's an example in C using POSIX semaphores:

```c
#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>

sem_t semaphore;

void* threadFunction(void* arg) {
    sem_wait(&semaphore); // P operation (wait)
    // Critical section begins
    printf("Thread %ld is in the critical section.\n", (long)arg);
    // Critical section ends
    sem_post(&semaphore); // V operation (signal)
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 3); // Initialize semaphore with 3 resources

    pthread_t threads[5];
    for (long i = 0; i < 5; ++i) {
        pthread_create(&threads[i], NULL, threadFunction, (void*)i);
    }

    for (int i = 0; i < 5; ++i) {
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&semaphore); // Destroy the semaphore
    return 0;
}
```

In this example, the semaphore is initialized with a count of 3, allowing up to three threads to enter the critical section simultaneously. When a thread enters the critical section, it calls `sem_wait` to decrement the semaphore. When it leaves the critical section, it calls `sem_post` to increment the semaphore.

### Advantages of Semaphores:
- **Flexibility**: Counting semaphores can manage access to a specific number of identical resources, allowing for more complex synchronization patterns than mutexes.
- **Applicability**: Useful in a variety of scenarios, including producer-consumer problems, reader-writer problems, and more.

### Disadvantages of Semaphores:
- **Complexity**: Semaphores can be more complex to use correctly compared to other synchronization mechanisms like mutexes or monitors.
- **Risk of Deadlocks**: Improper use of semaphores can lead to deadlocks, especially when multiple semaphores are used.
- **Error-Prone**: Programmers must ensure that semaphores are correctly initialized, waited on, and signaled, which can be error-prone.

Semaphores are a powerful tool in concurrent programming for coordinating access to shared resources and implementing various synchronization patterns. However, they require careful management to prevent issues such as deadlocks and ensure the correct functioning of concurrent applications.