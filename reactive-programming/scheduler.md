---
b: https://blendedfeelings.com/software/reactive-programming/scheduler.md
---

# Schedulers in reactive programming 
are components that control the concurrency in reactive systems. They are responsible for deciding when and on which thread the execution of a task will take place. Schedulers are an essential part of reactive programming frameworks because they enable the creation of responsive, scalable, and efficient applications by managing asynchronous tasks and event handling.

Schedulers abstract away the details of thread management and provide a higher-level API for scheduling work. This allows developers to focus on the logic of their applications without worrying about the complexities of thread management.

Here are some common types of schedulers found in reactive programming frameworks like RxJava, RxJS, or Project Reactor:

1. **Immediate Scheduler**: Executes tasks synchronously on the current thread. This is useful for tasks that need to run immediately and complete quickly.

2. **Current Thread Scheduler**: Queues tasks on the current thread to be executed one after the other. This scheduler is useful for ensuring that tasks are executed in a predictable order.

3. **New Thread Scheduler**: Creates a new thread for each scheduled task. This is useful for long-running or CPU-intensive tasks that should not block the current thread.

4. **Computation Scheduler**: Optimized for CPU-bound tasks that require computation and processing. It typically maintains a fixed number of threads based on the number of available CPUs.

5. **IO Scheduler**: Optimized for I/O-bound work, such as reading from or writing to files, network calls, and database operations. It can create threads on-demand and is designed to handle asynchronous I/O operations efficiently.

6. **Event Loop Scheduler**: Similar to the event loop in JavaScript, this scheduler runs tasks in a loop on a single thread. It's useful for environments where a single-threaded event loop is the norm, such as client-side JavaScript.

7. **Test Scheduler**: Used for testing purposes, allowing the programmer to manually advance time and execute tasks in a controlled environment.

8. **Trampoline Scheduler**: Queues work on the current thread but ensures that tasks are executed in a non-recursive fashion to avoid stack overflow issues.

Schedulers can be chosen based on the nature of the task to be executed. For example, for a task that involves reading a file from disk, an IO Scheduler would be appropriate, as it can manage the waiting time efficiently without blocking other operations. On the other hand, for a task that involves heavy computation, a Computation Scheduler would be more suitable, as it can utilize multiple cores of the CPU to perform the computation in parallel.

In reactive programming, schedulers are typically used in conjunction with observables (streams of data/events). Developers can specify which scheduler to use when subscribing to an observable, or when an operator that involves asynchronous processing is applied. This gives fine-grained control over the execution context and helps in achieving better performance and responsiveness in reactive applications.