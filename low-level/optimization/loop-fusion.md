---
b: https://blendedfeelings.com/software/low-level/optimization/loop-fusion.md
---

# Loop fusion
also known as loop jamming or loop merging, is an optimization technique that combines two or more adjacent loops that iterate over the same range into a single loop. This can improve performance by reducing the overhead of loop control, increasing data locality, and making more efficient use of the cache.

By fusing loops, you can reduce the number of times the loop's index variables are incremented, the number of conditional branch instructions, and the number of times data is loaded into cache. This is particularly beneficial when the loops access the same data or data that is located close together in memory.

However, loop fusion is only applicable when there are no data dependencies between the statements in the loops that would prevent them from being safely combined.

Here's an example of loop fusion. Consider the following two loops that initialize two separate arrays:

```c
#define N 1024
void initialize_arrays(int a[N], int b[N]) {
    for (int i = 0; i < N; ++i) {
        a[i] = 0; // First loop
    }
    
    for (int i = 0; i < N; ++i) {
        b[i] = 1; // Second loop
    }
}
```

These loops can be fused into a single loop:

```c
#define N 1024
void initialize_arrays_fused(int a[N], int b[N]) {
    for (int i = 0; i < N; ++i) {
        a[i] = 0; // Combined loop
        b[i] = 1; // Combined loop
    }
}
```

By combining the loops, the initialization of both arrays is done in the same iteration, improving spatial locality because `a[i]` and `b[i]` are likely to be in the same or adjacent cache lines. This reduces the number of times the loop index is incremented and the number of iterations, which can lead to better performance.

It's important to verify that loop fusion does not change the program's semantics, particularly when there are dependencies between the loops that might be affected by merging them. As with any optimization, it's also a good idea to profile the performance before and after applying loop fusion to ensure it has the desired effect.