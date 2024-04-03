---
b: https://blendedfeelings.com/software/concurrency/concurrency-and-parallelism.md
---

# Concurrency and parallelism 
are two terms that are often used in the context of multitasking in computing, but they refer to different concepts.

### Concurrency:

Concurrency is the concept of managing multiple tasks at the same time. It involves the ability of a system to deal with multiple tasks by switching between them so quickly that it gives the illusion of simultaneous execution. The tasks could be executed out of order or in partial order, without affecting the final outcome.

**Concurrency without Parallelism Example:**
A single-core CPU can be an example of concurrency without parallelism. Even though the processor can only execute one task at a time, it can switch between tasks (context switching) to handle multiple tasks seemingly at once. For instance, a single-core machine running a web server could handle multiple web requests concurrently by rapidly switching between them, but it is not processing them in parallel since there's only one core.

### Parallelism:

Parallelism, on the other hand, refers to the simultaneous execution of multiple tasks. This usually requires multiple processors or cores. With parallelism, tasks are literally running at the same time, not just seemingly so.

**Parallelism without Concurrency Example:**
A multi-core processor running a single, multi-threaded task can serve as an example of parallelism without concurrency. If a program is designed to perform a large, complex calculation by dividing it into smaller independent tasks that can run simultaneously, and the system dedicates all of its resources to this single program, then it is achieving parallelism. However, it's not concurrently handling other tasks; it's fully focused on executing the parts of this one task in parallel.

### Similarities:

- Both concurrency and parallelism are related to the way a system handles tasks.
- They both aim to improve the efficiency and performance of a system.
- They often require the tasks to be broken down into smaller, manageable parts that can be executed independently.

### Differences:

- Concurrency is about dealing with multiple tasks at once and is more about the structure of the system (how it handles task management), whereas parallelism is about doing multiple tasks at once and is more about the execution (actually running tasks simultaneously).
- Concurrency can be achieved on a single processor through task switching, while parallelism requires multiple processors or cores.
- Concurrency emphasizes the composition of independently executing processes, while parallelism requires tasks to be executed simultaneously.

Understanding these concepts is crucial for software developers, especially when working on high-performance applications or systems that require efficient multitasking capabilities.