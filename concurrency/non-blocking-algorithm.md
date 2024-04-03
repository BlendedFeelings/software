---
b: https://blendedfeelings.com/software/concurrency/non-blocking-algorithm.md
---

# Non-blocking algorithms 
are a class of algorithms that implement data structures or operations without the need for locks. This is particularly useful in concurrent programming, where threads can operate on shared data without the overhead and potential deadlocks associated with traditional locking mechanisms. Non-blocking algorithms are designed to allow multiple threads to make progress without interfering with each other, and they are typically classified into the following types:

1. **Lock-Free Algorithms**: These guarantee that at least one thread will make progress in a finite number of steps, even if other threads are delayed indefinitely. They do not ensure that every thread will make progress, but they prevent the system from getting completely stuck. Lock-free data structures are often implemented using atomic operations provided by the hardware, such as compare-and-swap (CAS).

2. **Wait-Free Algorithms**: These provide a stronger guarantee than lock-free algorithms. Every thread will make progress in a finite number of steps, regardless of the execution of other threads. Wait-free algorithms are usually more complex and can be more expensive to implement than lock-free algorithms.

3. **Obstruction-Free Algorithms**: These guarantee progress for any thread that eventually executes in isolation, meaning that if all other threads are paused, the single running thread will complete its operation in a finite number of steps. Obstruction-free algorithms are weaker than lock-free algorithms because they do not guarantee global progress when multiple threads are running.

Non-blocking algorithms are widely used in high-performance computing and real-time systems where predictability and low latency are critical. They are also beneficial in avoiding common concurrency issues such as deadlocks, priority inversion, and convoying. However, designing and implementing non-blocking algorithms can be challenging and requires a deep understanding of concurrency and memory models.

Here are some key concepts and techniques often used in non-blocking algorithms:

- **Atomic Operations**: Operations that are completed in a single step from the point of view of other threads. Examples include atomic read, write, increment, and compare-and-swap (CAS).

- **Compare-And-Swap (CAS)**: An atomic operation that updates a variable only if it has an expected value. CAS is a building block for many non-blocking algorithms.

- **Memory Barriers**: Also known as memory fences, these are used to ensure memory operations occur in the correct order, which is crucial for the correctness of non-blocking algorithms.

- **Backoff Strategies**: Techniques used to reduce contention between threads, such as exponential backoff, where a thread waits for a random or increasing amount of time before retrying an operation.

- **Hazard Pointers**: A technique for safe memory reclamation in lock-free data structures, used to prevent the "ABA problem," where a memory location is updated from value A to B and back to A, potentially causing issues in concurrent operations.

Non-blocking algorithms are an advanced topic in computer science and require careful consideration to ensure correctness and performance. They are most often used in low-level system libraries and high-performance applications where the benefits outweigh the complexity of implementation.