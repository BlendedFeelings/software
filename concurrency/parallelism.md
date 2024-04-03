---
b: https://blendedfeelings.com/software/concurrency/parallelism.md
---

# Parallelism in computing 
refers to the execution of multiple tasks or processes simultaneously on different processing units or cores within a computer system. This concept leverages the physical architecture of multi-core processors, multiprocessors, or distributed systems to perform several operations at the exact same time, thereby increasing computational speed and throughput.

Check: [concurrency vs parallelism](concurrency-and-parallelism.md)

Key aspects of parallelism include:

- **Simultaneous Execution:** Parallelism involves tasks running at the same time on separate processing units. For example, a quad-core processor can potentially execute four tasks simultaneously, one on each core.

- **Hardware Dependency:** Parallelism is inherently dependent on the hardware capabilities of a system. A system with a single processing unit cannot achieve true parallelism but can simulate concurrency through time-slicing.

- **Scalability:** Parallel systems can often be scaled up by adding more processing units to handle an increased load or to perform more complex computations in less time.

- **Efficiency:** Parallelism can significantly improve the efficiency of computational tasks, especially for workloads that can be divided into independent sub-tasks. This is commonly seen in scientific computing, image processing, and large-scale data analysis.

- **Complexity:** Designing parallel algorithms and managing parallel execution can be complex. It requires careful consideration to divide tasks into sub-tasks that can be executed without interfering with each other and to aggregate results from parallel computations.

- **Determinism:** Unlike concurrency, parallelism can be deterministic if the parallel tasks are designed to be independent and free from side effects. However, when tasks need to interact or share state, parallel programs can face similar challenges to concurrent ones, such as race conditions and synchronization issues.

Parallelism is a key strategy for improving the performance of software applications and is widely used in high-performance computing, real-time systems, and applications that require large-scale data processing. It is important to distinguish parallelism from concurrency, as the former requires hardware with multiple processing units, while the latter is a broader concept that can be applied even in single-processor systems to manage the execution of multiple tasks.