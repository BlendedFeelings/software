---
b: https://blendedfeelings.com/software/concurrent-programming/memory-barrier.md
---

# Memory barriers 
also known as memory fences, are mechanisms that provide ordering constraints on memory operations (loads and stores) in concurrent programming. They are crucial in multiprocessor systems where each processor may have its own cache, and memory operations can be seen in different orders by different processors due to various optimizations like out-of-order execution and caching strategies.

Memory barriers are used to ensure that memory operations are performed in the correct order, which is essential for the correctness of concurrent algorithms, especially those that use non-blocking synchronization techniques.

### Types of Memory Barriers:

1. **Load Barrier (Read Barrier)**: Ensures that all load operations issued before the barrier are completed before any load operations issued after the barrier.

2. **Store Barrier (Write Barrier)**: Ensures that all store operations issued before the barrier are completed before any store operations issued after the barrier.

3. **Full Barrier (Read-Write Barrier)**: Combines the effects of both load and store barriers. It ensures that all load and store operations issued before the barrier are completed before any operations (load or store) issued after the barrier.

### Purpose of Memory Barriers:

- **Data Consistency**: Memory barriers prevent the reordering of read and write operations to ensure data consistency across multiple threads.

- **Visibility**: They ensure that modifications made by one thread are visible to other threads in a timely manner.

- **Synchronization**: Memory barriers are often used alongside atomic operations in lock-free and wait-free algorithms to provide the necessary synchronization guarantees.

### How Memory Barriers Work:

- **Compiler Memory Barriers**: Instruct the compiler not to reorder the read and write operations across the barrier. This is important for ensuring the correct sequence of operations in the compiled machine code.

- **Hardware Memory Barriers**: Instruct the CPU to enforce an ordering constraint on memory operations. This is critical for multiprocessor systems where each processor may have its own view of memory.

### Memory Models and Memory Barriers:

Different programming languages and hardware platforms have different memory models, which define the behavior of memory operations in concurrent contexts. Some memory models, such as the x86 memory model, provide strong guarantees about operation ordering and may require fewer explicit memory barriers. In contrast, weaker memory models, like ARM and PowerPC, allow more aggressive reordering and typically require more explicit barriers to ensure correct operation ordering.

### Usage in Programming:

In high-level programming languages, memory barriers are often hidden behind abstractions like locks, condition variables, and atomic operations. However, when writing low-level concurrent code, especially in languages like C or C++, developers may need to use explicit memory barrier instructions provided by the language or the underlying hardware to ensure correct operation ordering.

In conclusion, memory barriers are a low-level synchronization primitive that play a critical role in the development of concurrent programs, particularly when using non-blocking synchronization mechanisms. They ensure that memory operations occur in the correct order, which is necessary for maintaining the consistency and correctness of shared data.