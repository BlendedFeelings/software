---
b: https://blendedfeelings.com/software/concurrency/concurrency.md
---

# Concurrency 
refers to the ability of a system to manage multiple tasks or processes at the same time. In the context of computing, it involves executing multiple sequences of operations or tasks in overlapping time periods, rather than strictly sequentially. Concurrency is a property of systems where several computations are executing simultaneously, and potentially interacting with each other.

Check: [concurrency vs parallelism](concurrency-and-parallelism.md)

Key aspects of concurrency include:

- **Overlapping Execution:** Concurrency allows different parts of a task or multiple tasks to be executed out-of-order or in partial order, without affecting the final outcome. This overlapping is often logical rather than physical, meaning that tasks may not actually be running at the same instant but are interleaved in a way that simulates simultaneous execution.

- **Interleaving:** In a concurrent system, tasks are interleaved in a way that gives the illusion of parallelism. A single processor might switch between different tasks, advancing each a little at a time (time-slicing), effectively managing concurrency on a single processing unit.

- **Shared Resources:** Concurrency often involves managing access to shared resources to prevent conflicts and ensure data consistency. This requires synchronization mechanisms to coordinate the execution of concurrent tasks.

- **Non-determinism:** Concurrency introduces non-determinism in program execution. The exact order in which operations occur may vary from one execution to another due to the interleaving of tasks, which can make debugging and testing more challenging.

- **Independence:** Concurrent tasks can often be executed independently, with minimal coordination or communication. However, when tasks need to cooperate or share data, careful synchronization is necessary to avoid issues such as race conditions.

Concurrency is a fundamental concept in computer science and is used extensively in various domains, including operating systems, databases, network servers, and real-time systems. It is a critical aspect of designing systems that are efficient, responsive, and able to handle multiple operations or users at the same time. Concurrency is different from parallelism, which refers to the actual simultaneous execution of multiple tasks, typically using multiple processors or cores.