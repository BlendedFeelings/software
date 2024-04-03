---
b: https://blendedfeelings.com/software/concurrency/readers-writers-problem.md
---

# Readers-Writers problem 
is a classic synchronization problem in concurrent programming. It addresses the situation where a shared resource can be accessed by multiple threads for reading or writing. The challenge is to allow multiple readers to read from the shared resource at the same time, without a writer modifying it, while also allowing writers to have exclusive access when they need to update the resource.

### Problem Statement
The problem arises from the conflict between readers and writers:
- **Readers**: Want concurrent access to the resource when no writer is present.
- **Writers**: Require exclusive access to the resource, with no readers or other writers present.

### Objectives
- Maximize concurrency: Allow as many readers as possible to read concurrently.
- Ensure data consistency: Prevent readers from reading inconsistent or stale data.
- Prevent starvation: Ensure that both readers and writers get a chance to access the resource without waiting indefinitely.

### Solutions
There are several solutions to the Readers-Writers problem, each with its trade-offs. The two most common variants are:

1. **Readers Preference**: This solution prioritizes readers over writers. Writers can only write if there are no readers currently reading or waiting to read. The downside is that writers can starve if there is a continuous stream of readers.

2. **Writers Preference**: This solution prioritizes writers over readers. Once a writer is ready, no new readers are allowed to start reading; they must wait until the writer has finished. This can lead to readers starvation if there are many writers.

### Implementation Considerations
- **Mutexes/Semaphores**: These synchronization primitives can be used to control access to the shared resource.
- **Readers Counter**: A common approach is to use a counter to keep track of the number of readers currently accessing the resource.
- **Condition Variables**: These can be used to block and wake up reader and writer threads appropriately to manage access to the resource.

### Example Pseudocode
Here's a simple pseudocode example illustrating a readers-writers solution with readers preference:

```pseudo
initialize mutex, readCount, resourceSemaphore
readCount = 0

writer():
    wait(resourceSemaphore)
    write_data()
    signal(resourceSemaphore)

reader():
    wait(mutex)
    readCount++
    if readCount == 1:
        wait(resourceSemaphore)
    signal(mutex)

    read_data()

    wait(mutex)
    readCount--
    if readCount == 0:
        signal(resourceSemaphore)
    signal(mutex)
```

In this pseudocode:
- `mutex` protects the `readCount` variable.
- `readCount` keeps track of the number of readers currently reading.
- `resourceSemaphore` provides exclusive access to the resource for writers and is also used to prevent new readers from starting when a writer is waiting.

### Conclusion
The Readers-Writers problem is a fundamental issue in concurrent programming that requires careful synchronization to ensure data consistency while maximizing concurrency. The choice of solution (readers preference, writers preference, or a fair approach) depends on the specific requirements of the application and the desired balance between reader and writer throughput.