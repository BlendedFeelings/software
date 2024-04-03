---
b: https://blendedfeelings.com/software/low-level/optimization/prefetching.md
---

# Prefetching 
is an optimization technique used to improve the performance of computer programs by reducing memory access latency. It involves proactively loading data into the cache before it is actually needed by the processor. By doing so, the likelihood of cache misses is reduced, and the processor can access the data with less delay when it is needed.

Prefetching can be done at various levels, including hardware prefetching by the CPU itself, software prefetching through specific instructions in the program code, or at the compiler level where the compiler inserts prefetching instructions based on its analysis of the code.

### Hardware Prefetching
Modern processors often include hardware prefetchers that automatically fetch data into the cache based on observed access patterns. These prefetchers can be quite sophisticated, using algorithms to predict which memory locations are likely to be accessed in the near future. Hardware prefetching is transparent to the programmer and requires no changes to the program code.

### Software Prefetching
Software prefetching is done by manually inserting prefetch instructions into the code. This gives the programmer more control over what data is prefetched and when. However, it requires an understanding of the memory access patterns and the behavior of the target architecture's memory subsystem.

Here's an example of how you might use software prefetching in C:

```c
#define PREFETCH_DISTANCE 64

void process_data(double *data, int size) {
    for (int i = 0; i < size; ++i) {
        // Prefetch data that will be needed in the future
        __builtin_prefetch(&data[i + PREFETCH_DISTANCE], 0, 1);
        
        // Perform computations on the current data
        data[i] *= 2;
    }
}
```

In the above code, the `__builtin_prefetch` function is a built-in function provided by GCC to insert prefetch instructions. The first argument is the address to prefetch, the second argument specifies whether the prefetch is for a read (0) or a write (1), and the third argument is the temporal locality hint (0 for no temporal locality, 3 for high temporal locality).

### Compiler Prefetching
Some compilers can automatically insert prefetch instructions when they compile the code, especially if the programmer uses compiler hints or pragmas to indicate which loops or data structures are good candidates for prefetching. Compiler prefetching can be easier to maintain than manual software prefetching and can adapt to different target architectures.

### Considerations for Prefetching
- **Access Patterns**: Prefetching is most effective when access patterns are regular and predictable, such as iterating over arrays.
- **Prefetch Distance**: The distance ahead to prefetch (how many iterations ahead) must be chosen to match the memory latency; prefetching too early or too late can reduce effectiveness.
- **Cache Pollution**: Prefetching data that is not used can evict useful data from the cache, leading to cache pollution.
- **Resource Usage**: Prefetching uses memory bandwidth and can compete with other memory operations, potentially causing contention.

Prefetching is a powerful optimization, but it should be used judiciously. It's important to profile the application and understand the memory access patterns to determine where prefetching might be beneficial. Overuse of prefetching, or prefetching the wrong data, can lead to performance degradation instead of improvement.