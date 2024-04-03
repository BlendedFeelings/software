---
b: https://blendedfeelings.com/software/memory-management/segregated-free-lists.md
---

# Segregated free lists 
is a memory management technique used to reduce fragmentation and improve the efficiency of dynamic memory allocation. This approach involves maintaining multiple separate lists (or bins) of free memory blocks, with each list holding blocks of a specific size range. By segregating the free memory into different size classes, the allocator can quickly find a suitable block for an allocation request without having to search through blocks of all sizes.

Here's how segregated free lists generally work:

1. **Initialization**: The memory allocator initializes several free lists, each designated to hold blocks within a certain size range. For example, one list might hold blocks of size 16-31 bytes, another for 32-63 bytes, and so on.

2. **Allocation**: When a request for memory is made, the allocator determines which size class the request falls into and searches the corresponding free list for an available block. If a suitable block is found, it is removed from the free list and returned to the requester.

3. **Deallocation**: When a block is freed, the allocator determines the size class of the block and adds it to the corresponding free list. If the block can be coalesced with adjacent free blocks to form a larger block, this is done before adding it to the appropriate list.

4. **Splitting**: If a larger block is available but the allocation request is for a smaller size, the block may be split into two pieces. The piece that matches the request size is allocated, while the remainder is added back to the appropriate free list.

5. **Coalescing**: When a block is freed, the allocator may check adjacent blocks to see if they are also free. If so, it can merge (coalesce) them into a larger block to reduce fragmentation and then place the larger block in the appropriate size class list.

Here is a simplified example of segregated free lists in operation:

```
Free Lists:
[16-31 bytes]: [Block1] -> [Block2] -> ...
[32-63 bytes]: [Block3] -> [Block4] -> ...
...
```

Advantages of Segregated Free Lists:
- **Fast Allocation**: By maintaining separate lists for different size classes, the allocator can quickly find a free block without having to search through blocks of all sizes.
- **Reduced Fragmentation**: Segregating by size helps to reduce external fragmentation, as blocks are more likely to be closely matched to the size of the allocation request.
- **Scalability**: This technique can scale well with the number of allocation and deallocation operations, as operations within each list are relatively fast.

Disadvantages of Segregated Free Lists:
- **Potential for Internal Fragmentation**: If the allocator frequently has to split larger blocks to satisfy smaller requests, it can lead to internal fragmentation.
- **Complexity**: Managing multiple lists and determining the right size class for each block adds complexity to the allocator's implementation.

Segregated free lists are often used in conjunction with other memory management techniques, such as boundary tags and coalescing, to create efficient and scalable memory allocators. They are particularly useful in systems where there are many allocation and deallocation operations of varying sizes.