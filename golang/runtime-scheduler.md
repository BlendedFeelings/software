# Runtime scheduler 
is a sophisticated component of the Go runtime that manages the execution of goroutines, which are lightweight threads managed by the Go runtime rather than the operating system. The scheduler's role is to distribute goroutines across available CPU cores for execution, enabling efficient concurrency in Go programs.

Here are some key points about the Go runtime scheduler:

1. **M:N Scheduling**: The Go scheduler implements an M:N scheduling model, where M goroutines are multiplexed onto N OS threads. This allows for the creation of thousands of goroutines with minimal overhead, as they are not directly mapped to OS threads.

2. **Goroutines**: Goroutines are the basic unit of execution in Go. They are more lightweight than OS threads and are managed by the Go runtime. The scheduler is responsible for scheduling these goroutines onto threads for execution.

3. **G, M, P**: The scheduler uses three main concepts:
   - G (goroutine): Represents an individual goroutine.
   - M (machine): Represents an OS thread that can execute goroutines.
   - P (processor): Represents a context for scheduling that holds a queue of runnable goroutines and is bound to an M when executing goroutines.

4. **Work Stealing**: To balance the workload across threads, the scheduler employs a work-stealing algorithm. If one P's local run queue is empty, it can steal half of the goroutines from another P's run queue.

5. **Cooperative Scheduling**: Goroutines are cooperatively scheduled, which means that the scheduler relies on goroutines to yield control at certain points, such as when making a blocking system call or when explicitly calling runtime.Gosched(). This differs from preemptive scheduling, where the scheduler forcibly takes control from running threads at any point.

6. **Preemption**: Starting from Go 1.14, the scheduler has the ability to preempt long-running goroutines to ensure that other goroutines get a chance to run, improving fairness and latency. This is done by sending a signal to the running goroutine, which then checks whether it should yield.

7. **Syscall and Network Poller**: The Go scheduler is tightly integrated with the Go runtime's network poller and system call handling. When a goroutine makes a blocking syscall or waits for I/O, it is descheduled, and the M is released to run other goroutines until the operation completes.

8. **Scalability**: The scheduler is designed to scale with the number of CPU cores, allowing Go programs to take advantage of multicore processors without the complexity of traditional thread-based concurrency.

The Go scheduler is a critical part of the language's concurrency model and enables developers to write highly concurrent programs without dealing with the low-level intricacies of thread management. The scheduler is constantly being improved with each new release of Go, with enhancements aimed at increasing performance and reducing latency.