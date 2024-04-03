---
b: https://blendedfeelings.com/software/memory-management/fragmentation.md
---

# Fragmentation 
refers to a situation where available memory is divided into small, non-contiguous blocks, making it difficult or impossible to allocate large contiguous segments of memory. Fragmentation can occur in both the heap and the file system, and it can lead to inefficient use of memory or storage, as well as degraded performance. There are two main types of fragmentation: external fragmentation and internal fragmentation.

### External Fragmentation
External fragmentation occurs in the heap when free memory is scattered in small blocks between allocated memory segments. Over time, as memory is allocated and deallocated, the free memory becomes fragmented. Even if there is enough total free memory to satisfy an allocation request, the lack of a large enough contiguous block can prevent the allocation from succeeding.

In the context of a file system, external fragmentation happens when a file is not stored in a contiguous block of space, leading to increased seek times as the disk head must move to different locations to access the entire file.

### Internal Fragmentation
Internal fragmentation occurs when memory is allocated in blocks that are larger than the actual amount of memory requested. For example, if a memory allocator only provides memory in fixed-size blocks (e.g., 64 bytes), and a program requests 50 bytes, the remaining 14 bytes in the allocated block are wasted. This is known as internal fragmentation because the wasted space is inside the allocated blocks.

In a file system, internal fragmentation can occur when the storage blocks (or clusters) are larger than the actual size of the files stored in them, resulting in wasted space within each block.

### Mitigation Strategies
Various strategies are employed to mitigate the effects of fragmentation:

- **Compaction**: In memory management, compaction involves moving allocated memory blocks to create larger contiguous free spaces. This can be a costly operation as it requires updating references to moved objects.

- **Garbage Collection**: Some garbage collectors, especially those using copying or compacting algorithms, can reduce external fragmentation by moving objects to consolidate free space.

- **Slab Allocation**: This memory management technique pre-allocates memory chunks for specific object sizes, reducing internal fragmentation for frequently used object sizes.

- **Buddy System**: A buddy memory allocation system allocates memory in blocks that are powers of two. This can reduce external fragmentation by splitting and coalescing blocks more efficiently.

- **Best Fit, Worst Fit, First Fit**: These are different strategies for choosing the free block in which to place a new allocation. Each has its own trade-offs in terms of fragmentation and allocation speed.

- **Defragmentation Tools**: For file systems, defragmentation tools can reorganize files to store them in contiguous blocks, improving access times.

Understanding and managing fragmentation is important for system performance, especially in long-running or memory-intensive applications. It requires a balance between the overhead of managing fragmentation and the need for efficient memory and storage usage.