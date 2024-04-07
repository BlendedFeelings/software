---
b: https://blendedfeelings.com/software/concurrent-programming/obstruction-free-algorithm.md
---

# Obstruction-free algorithms 
are the weakest form of non-blocking algorithms in terms of progress guarantees. They ensure that any thread will make progress if it eventually executes in isolation, meaning that if all other threads are paused or stop interfering, the single running thread will complete its operation in a finite number of steps. This type of algorithm is designed to handle situations where contention is low, and it is unlikely that multiple threads will compete for the same resources simultaneously.

### Characteristics of Obstruction-Free Algorithms:

- **Single-Thread Progress**: A thread is guaranteed to complete its operation if it does not face interference from other threads.

- **Non-Blocking**: Obstruction-free algorithms do not use locks, thus avoiding issues such as deadlocks and priority inversion.

- **Low Contention Optimization**: These algorithms are optimized for scenarios with low contention, where conflicts between threads are rare.

### Common Techniques in Obstruction-Free Algorithms:

- **Atomic Operations**: Similar to lock-free and wait-free algorithms, obstruction-free algorithms use atomic operations to ensure consistency when accessing shared data.

- **Optimistic Concurrency Control**: Threads assume that they will not face contention and proceed with their operations optimistically. If contention is detected, they roll back their changes and retry.

- **Versioning or Timestamps**: These are often used to detect interference. A thread can check if the shared data has changed since it began its operation to determine if it should retry.

### Examples of Obstruction-Free Data Structures:

- **Software Transactional Memory (STM)**: An obstruction-free implementation of STM allows threads to execute memory transactions optimistically, with the system rolling back transactions that encounter conflicts.

- **Obstruction-Free Stack**: An implementation of a stack that allows threads to push and pop elements optimistically, with rollback mechanisms in place if interference is detected.

### Challenges of Obstruction-Free Algorithms:

- **Contention Handling**: Obstruction-free algorithms do not inherently handle contention well. If contention becomes common, performance can degrade significantly due to repeated rollbacks and retries.

- **Complexity**: Implementing rollback mechanisms and ensuring correctness in the face of interference can be complex.

- **Starvation**: A thread may suffer from starvation if it consistently faces interference from other threads, as there is no guarantee of progress in the presence of contention.

- **Memory Reclamation**: As with other non-blocking algorithms, safely reclaiming memory in the presence of concurrent operations is a challenge.

Obstruction-free algorithms are particularly useful when contention is expected to be low, or when the overhead of stronger non-blocking guarantees (like those provided by lock-free or wait-free algorithms) is not justified. They provide a good balance between performance and complexity in scenarios where the system can tolerate occasional delays due to contention but still benefits from the absence of locks. However, in high-contention scenarios, obstruction-free algorithms may not perform as well as lock-free or wait-free alternatives.