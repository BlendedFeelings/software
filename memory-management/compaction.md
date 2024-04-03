---
b: https://blendedfeelings.com/software/memory-management/compaction.md
---

# Compaction 
is a memory management technique used in computing to overcome the problem of external fragmentation in dynamic memory allocation. External fragmentation occurs when free memory is scattered in small blocks throughout the heap, making it difficult to allocate larger blocks of memory, even when there is enough total free memory available.

Compaction involves moving allocated memory blocks to one end of the memory space or to contiguous locations, thus consolidating free memory into a single large block or into fewer larger blocks. This process can reduce or eliminate external fragmentation, making it easier to satisfy larger allocation requests.

Here is how compaction generally works:

1. **Identify Free Blocks**: The memory manager identifies all the free blocks in the heap.

2. **Shift Allocated Blocks**: Allocated blocks are moved towards one end of the memory space. This can be done by either shifting blocks one by one or by copying them to a new location in a more organized fashion.

3. **Update References**: As allocated blocks are moved, any references to these blocks must be updated to point to the new locations. This is a critical step, as failing to update references can lead to program errors and crashes.

4. **Consolidate Free Space**: The free space left behind by the moved blocks is merged into a larger free block, reducing fragmentation.

5. **Allocation**: After compaction, new allocation requests can be more easily satisfied because there is a larger contiguous free block available.

Compaction can be visualized as follows:

```
Before Compaction:  [A][ ][B][ ][ ][C][ ][ ][D]
After Compaction:   [A][B][C][D][ ][ ][ ][ ][ ]
```
Here, `[A]`, `[B]`, `[C]`, and `[D]` represent allocated blocks, and `[ ]` represents free space.

Advantages of Compaction:
- **Reduces Fragmentation**: Compaction reduces external fragmentation by consolidating free memory.
- **Simplifies Allocation**: A single large free block makes it easier to allocate memory for larger objects without needing to search for suitable space.

Disadvantages of Compaction:
- **Performance Overhead**: Compaction can be time-consuming because it involves moving memory blocks and updating references, which can lead to delays in program execution.
- **Complexity**: Keeping track of all references to moved objects can be complex, especially in systems with many pointers or references.
- **Disruption**: During compaction, the system may need to pause other operations, which can affect real-time performance.

Compaction is not commonly used in most modern general-purpose allocators due to its overhead and complexity. Instead, other strategies, such as the use of segregated free lists, buddy systems, and slab allocation, are employed to reduce fragmentation. However, compaction may still be used in certain specialized or constrained environments where the benefits outweigh the costs.