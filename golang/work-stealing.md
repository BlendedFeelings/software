---
b: https://blendedfeelings.com/software/golang/work-stealing.md
---

# Work-stealing algorithm in Go's scheduler
is used to efficiently distribute goroutines across multiple threads (referred to as M's in Go's runtime). The goal of work-stealing is to keep all threads busy by redistributing work from overloaded threads to those that are idle or less busy. Here's a high-level overview of how work stealing works in the Go scheduler:

1. **Local Run Queue (LRQ):** Each thread (M) has a local run queue of goroutines that are ready to run. This is where a thread looks first when it needs more work.

2. **Global Run Queue (GRQ):** There is also a global run queue that holds goroutines that are not yet assigned to any specific thread's local run queue. When a new goroutine is created, it is initially placed in the global run queue.

3. **Work Stealing:** When a thread runs out of work (its local run queue is empty), it attempts to steal work from other threads. It does this by randomly selecting another thread and trying to take (steal) half of the goroutines from its local run queue. If successful, the stealing thread moves the stolen goroutines to its own local run queue and starts executing them.

4. **Fallback to Global Run Queue:** If a thread is unable to steal work from another thread (perhaps because all other threads are also out of work), it will then check the global run queue for any available goroutines. If it finds work there, it will take some goroutines from the global run queue and place them in its local run queue.

5. **Idle Threads (P's):** If there is no work available in either the local run queues or the global run queue, the thread may go into an idle state. The scheduler keeps a list of idle threads (referred to as P's) that can be quickly woken up when new work becomes available.

6. **Netpoller Integration:** The Go scheduler is also integrated with the network poller, which allows threads to wait for I/O events without blocking. When a goroutine performs a blocking I/O operation, it is descheduled, and the thread that was running it can execute other goroutines. Once the I/O operation completes, the goroutine is placed back into the run queue.

7. **Synchronization with System Threads:** Go's runtime is also responsible for managing interactions with the operating system's threads. The scheduler ensures that the number of threads (M's) does not exceed the number of logical processors available, as specified by the `GOMAXPROCS` environment variable.

The work-stealing algorithm in Go's scheduler is designed to balance the load across threads efficiently and to reduce contention by allowing threads to operate on their local run queues most of the time. This approach helps Go programs to scale well on multi-core systems, providing efficient concurrency with minimal overhead.