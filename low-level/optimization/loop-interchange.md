---
b: https://blendedfeelings.com/software/low-level/optimization/loop-interchange.md
---

# Loop interchange 
is an optimization technique that involves swapping the nesting order of two or more loops in a nested loop structure. This can improve performance by enhancing data locality, particularly spatial locality, and making better use of the cache hierarchy in modern processors.

When dealing with multi-dimensional arrays, the layout of the data in memory can have a significant impact on the cache performance of the program. Most programming languages use row-major order for multi-dimensional arrays, meaning that consecutive elements of a row are stored next to each other in memory. By interchanging loops, you can ensure that the innermost loop iterates over elements that are contiguous in memory, which can lead to better spatial locality and fewer cache misses.

Here's an example of loop interchange. Consider the following code that transposes a matrix:

```c
#define N 1024
void transpose(int src[N][N], int dst[N][N]) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            dst[j][i] = src[i][j];
        }
    }
}
```

In the above code, `src` and `dst` are two-dimensional arrays. The code accesses `src` row-wise but writes to `dst` column-wise, which is not optimal for spatial locality because `dst[j][i]` accesses are not contiguous in memory.

To improve spatial locality, you can interchange the loops like this:

```c
#define N 1024
void transpose_optimized(int src[N][N], int dst[N][N]) {
    for (int j = 0; j < N; ++j) {
        for (int i = 0; i < N; ++i) {
            dst[j][i] = src[i][j];
        }
    }
}
```

Now, both `src` and `dst` are accessed in a row-major fashion, which is the order they are stored in memory. This change can lead to a significant improvement in performance due to better cache utilization.

However, loop interchange is not always legal or beneficial. It's important to consider data dependencies within the loops to ensure that interchanging the loops does not change the semantics of the program. Additionally, the performance gains from loop interchange can vary depending on the specifics of the processor's cache architecture and the size of the data structures involved. It's always a good idea to profile the code before and after making such changes to confirm the performance impact.