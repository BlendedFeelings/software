---
b: https://blendedfeelings.com/software/memory-management/slab-allocation.md
---

# Slab allocation 
is a memory management mechanism designed to reduce the overhead and fragmentation that can occur in a system that frequently allocates and deallocates objects of the same size or type. It is commonly used in operating system kernels for managing the memory of kernel objects such as process descriptors, file objects, and network buffers.

The slab allocator groups objects into caches, where each cache is a collection of one or more slabs. Each slab is a contiguous block of memory that is divided into chunks of a fixed size, suitable for holding objects of the same type or size.

Here's how slab allocation works:

1. **Cache Initialization**: When the system is initialized, or when a new type of object is first used, a cache is created for objects of that type. The cache is populated with one or more slabs.

2. **Slab Creation**: A slab is a contiguous block of memory that is divided into equal-sized chunks. Each chunk is large enough to hold one instance of the object type.

3. **Object Allocation**: When the kernel needs to allocate a new object, it looks for a free chunk within the slabs of the appropriate cache. If a free chunk is available, it is marked as used, and a pointer to it is returned.

4. **Object Deallocation**: When an object is no longer needed, the chunk of memory it occupies is marked as free. There is no need to return the memory to the global pool immediately, as it can be reused for the next allocation request of the same type.

5. **Slab Reclaiming**: If a slab becomes completely empty (all objects within it are freed), the slab can be returned to the global memory pool or kept in the cache for future allocations.

6. **Coloring**: To reduce cache-line contention, slab allocation often uses a technique called "coloring," which involves offsetting the starting address of objects within a slab by a small amount. This helps to distribute objects of the same type across different cache lines, improving cache utilization.

Advantages of Slab Allocation:
- **Speed**: Allocation and deallocation are fast because objects of the same size are grouped together and the allocator does not have to search for a suitable block of memory each time.
- **Reduced Fragmentation**: Since objects are allocated from slabs dedicated to a particular size or type, there is less external fragmentation.
- **Readiness**: Objects in a slab can be pre-initialized to a certain extent, reducing the initialization time for each allocation.

Disadvantages of Slab Allocation:
- **Memory Overhead**: If not all objects in a slab are in use, there can be internal fragmentation, leading to wasted memory.
- **Complexity**: The slab allocator is more complex than general-purpose allocators, making it more suited to environments like kernel memory management rather than application-level memory allocation.

Slab allocation is particularly effective in systems where the allocation and deallocation patterns are predictable and where objects have a uniform size, which is often the case in kernel-level operations.