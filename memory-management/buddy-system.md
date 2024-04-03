---
b: https://blendedfeelings.com/software/memory-management/buddy-system.md
---

# Buddy system 
is a memory allocation algorithm that divides memory into partitions to try to satisfy a memory request as suitably as possible. This system is intended to avoid fragmentation and reduce the overhead of memory allocation. It works by maintaining memory blocks in powers of two.

Here's how the buddy system works:

1. **Initialization**: The entire memory space is initially considered as a single block of size \(2^N\), where \(N\) is chosen such that the size is large enough to accommodate all possible allocations.

2. **Allocation**: When a request for memory is made, the system finds the smallest block of memory (a buddy block) that is large enough to satisfy the request. If no such block is free, a larger block is split into two "buddies" of half the size, and the splitting continues recursively until a block of suitable size is found. The allocated block is then marked as used.

3. **Deallocation**: When a block is freed, the system checks if its buddy (the adjacent block of the same size) is also free. If so, the two buddies are merged to form a larger block. This merging can continue recursively if the larger block's buddy is also free, up to the maximum block size.

4. **Buddy Identification**: Each block's buddy can be easily identified using bitwise operations on the block's starting address. Due to the power-of-two alignment, buddies have addresses that differ by the size of the block.

Here's a simplified example of the buddy system in operation:

```csharp
// Allocation example
MemoryBlock Allocate(int size) {
    int blockSize = FindSmallestPowerOfTwoBlockSize(size);
    MemoryBlock block = FindFreeBlock(blockSize);
    if (block == null) {
        block = SplitLargerBlock(blockSize);
    }
    MarkBlockAsUsed(block);
    return block;
}

// Deallocation example
void Deallocate(MemoryBlock block) {
    MarkBlockAsFree(block);
    while (CanMergeWithBuddy(block)) {
        block = MergeWithBuddy(block);
    }
}
```

Advantages of the Buddy System:
- **Efficient Merging**: The buddy system allows efficient coalescing of free blocks, which can help to minimize external fragmentation.
- **Fast Allocation and Deallocation**: Due to the structured nature of the system, allocation and deallocation operations can be performed quickly using bitwise operations.

Disadvantages of the Buddy System:
- **Internal Fragmentation**: Since block sizes are powers of two, there may be internal fragmentation if the requested size does not exactly match a block size.
- **Overhead**: The system requires maintaining a complex data structure to track the sizes and states of blocks, which can introduce some overhead.

The buddy system is often used in systems where memory allocation and deallocation are frequent and where the overhead of managing a more complex allocator is justified by the benefits of reduced fragmentation and fast coalescence.