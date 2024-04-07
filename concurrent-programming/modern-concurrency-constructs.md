---
b: https://blendedfeelings.com/software/concurrent-programming/modern-concurrency-constructs.md
---

# Modern concurrency constructs 
are designed to take advantage of multicore processors, allowing for parallel execution of code to improve performance and responsiveness in applications. Here are some key concurrency constructs and paradigms that are commonly used in modern programming:

1. **Threads**: Threads are the smallest sequence of programmed instructions that can be managed independently by a scheduler, which is usually a part of the operating system. Each thread can run on a separate core, enabling true parallelism.

2. **Tasks**: Tasks represent asynchronous operations. Task-based programming models, like the Task Parallel Library (TPL) in .NET, abstract the thread management and provide a higher-level API for concurrency.

3. **Async/Await**: Introduced in languages like C# and JavaScript, the async/await pattern allows for writing asynchronous code that is as easy to read and write as synchronous code. It's built on top of tasks and promises, respectively, and helps manage asynchronous flows without blocking threads.

4. **Parallel Loops and Libraries**: Constructs like `Parallel.For` and `Parallel.ForEach` in .NET, or the `concurrent.futures` module in Python, allow for easy parallelization of loops where iterations can be executed in parallel.

5. **Actor Model**: The actor model is a conceptual model that treats "actors" as the fundamental units of computation. In this model, actors can run concurrently and communicate with each other through message passing. Frameworks like Akka implement this model.

6. **Futures and Promises**: These are constructs used for synchronization in concurrent programming. A future is a read-only placeholder view of a variable, while a promise is a writable, single-assignment container which sets the value of the future.

7. **Software Transactional Memory (STM)**: STM is a concurrency control mechanism analogous to database transactions for controlling access to shared memory. It allows for composing sequences of operations that should appear atomic.

8. **Locks and Synchronization Primitives**: Mutexes, semaphores, and condition variables are low-level synchronization constructs that control access to resources and ensure that only one thread can access the resource at a time.

9. **Coroutines**: Coroutines are computer-program components that generalize subroutines for non-preemptive multitasking. They allow for cooperative multitasking and concurrency, and are used in languages like Python (`asyncio`) and Kotlin.

10. **Data Parallelism**: This involves running the same function on different pieces of distributed data simultaneously. It's particularly useful for large data sets and can be implemented using frameworks like Hadoop or Spark.

11. **Message Passing Interface (MPI)**: MPI is a standardized and portable message-passing system designed to function on parallel computing architectures.

12. **GPU Computing**: With the rise of GPGPU (General-Purpose computing on Graphics Processing Units), APIs like CUDA and OpenCL allow for writing programs that execute across GPUs, which can perform computations in parallel at a much larger scale than CPUs.

13. **Functional Programming Constructs**: Languages that support functional programming, like Haskell or Scala, often include concurrency constructs that are based on functional paradigms, such as immutability and higher-order functions, which can simplify concurrent programming.

14. **Reactive Programming**: Frameworks like RxJava or Reactive Extensions (Rx.NET) implement the observer pattern to support asynchronous data streams and its transformation, which can be very useful in concurrent programming.

Each of these constructs is suited to different types of concurrency problems, and modern programming often involves a combination of these to achieve the best performance and maintainability. It's important to understand the concurrency model of the language or framework you're using to make the most out of multicore processors.