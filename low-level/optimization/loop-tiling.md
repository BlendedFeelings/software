---
b: https://blendedfeelings.com/software/low-level/optimization/loop-tiling.md
---

# Loop tiling 
also known as loop blocking or loop chunking, is a loop transformation technique that restructures loops to process data in small blocks or tiles that fit into the cache. By doing so, it enhances data locality and reduces the number of cache misses, which can lead to significant performance improvements, especially for operations on large data sets such as matrices.

The idea behind loop tiling is to divide a large iteration space into smaller, more manageable blocks. When a block is small enough to fit entirely within the cache, the processor can perform all the necessary computations on that block without having to fetch data from the slower main memory repeatedly.

Loop tiling is particularly effective for nested loops that access array elements in a regular pattern, such as matrix multiplication, convolution, or any operation that involves multi-dimensional arrays.

Here's an example of loop tiling applied to matrix multiplication:

```c
#define N 1024
#define TILE_SIZE 32 // Tile size should be chosen based on cache size and properties
void matrix_multiply_tiled(int a[N][N], int b[N][N], int result[N][N]) {
    int i, j, k, ii, jj, kk;
    for (ii = 0; ii < N; ii += TILE_SIZE) {
        for (jj = 0; jj < N; jj += TILE_SIZE) {
            for (kk = 0; kk < N; kk += TILE_SIZE) {
                for (i = ii; i < ii + TILE_SIZE && i < N; ++i) {
                    for (j = jj; j < jj + TILE_SIZE && j < N; ++j) {
                        int sum = result[i][j];
                        for (k = kk; k < kk + TILE_SIZE && k < N; ++k) {
                            sum += a[i][k] * b[k][j];
                        }
                        result[i][j] = sum;
                    }
                }
            }
        }
    }
}
```

In the above code, the original matrix multiplication loops have been split into two levels: the outer loops iterate over the tiles, and the inner loops iterate over the elements within a tile. The `TILE_SIZE` is chosen based on the size of the cache and the properties of the cache lines to ensure that each tile fits well within the cache.

By processing the matrix in tiles, the data required for each small computation is more likely to be in the cache, reducing the need to access main memory and improving the overall performance of the matrix multiplication.

Choosing the right tile size is crucial for the effectiveness of loop tiling. If the tile size is too small, the overhead of the loop control might outweigh the benefits of improved cache usage. If the tile size is too large, the tiles might not fit into the cache, leading to cache evictions and reduced performance. The optimal tile size can be determined through profiling and experimentation, taking into consideration the specific cache architecture of the target processor.