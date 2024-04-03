---
b: https://blendedfeelings.com/software/low-level/optimization/temporal-locality.md
---

# Temporal locality 
refers to the tendency of a processor to access the same memory locations repeatedly over a short period of time. When a program exhibits high temporal locality, it means that data or instructions that have been accessed recently are likely to be accessed again soon.

This concept is crucial for the efficiency of cache memory. Caches are designed to take advantage of temporal locality by keeping recently accessed data close to the processor. When the processor needs to access data, it first checks the cache. If the data is found in the cache (a cache hit), the processor can quickly use it without having to access the slower main memory. If the data is not in the cache (a cache miss), it must be fetched from main memory, which is a much slower process.

To exploit temporal locality in your programs, you can:

- **Use Variables Efficiently**: Keep frequently used variables, such as loop counters and heavily used data, in registers or at least ensure they remain in the cache by accessing them frequently.

- **Design Functions for Reuse**: Write functions that operate on data in a way that encourages repeated access to the same data within a short time frame.

- **Reuse Intermediate Results**: Store the results of expensive computations if they will be used again soon, rather than recomputing them.

- **Minimize Recalculation**: Avoid recalculating values that have already been computed and can be stored for reuse.

Here's an example of code that has good temporal locality:

```c
int sum_array(int *array, int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += array[i]; // Accessing array[i] repeatedly in a loop exhibits temporal locality
    }
    return sum;
}
```

In the above code, the `sum` variable has high temporal locality because it's being accessed and updated repeatedly in every iteration of the loop. The array elements also exhibit some degree of temporal locality, especially if the array is small enough to fit into the cache.

Improving temporal locality can lead to significant performance gains, especially in applications that process large amounts of data or perform complex calculations. By writing code that accesses data in a temporally local manner, you can reduce cache misses and make better use of the fast cache memory, leading to faster program execution.