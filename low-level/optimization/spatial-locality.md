---
b: https://blendedfeelings.com/software/low-level/optimization/spatial-locality.md
---

# Spatial locality 
refers to the tendency for execution to involve a number of memory locations that are clustered closely together in address space. It is based on the principle that if a particular storage location is accessed, it is highly likely that nearby memory locations will be accessed in the near future.

This concept is leveraged by the design of cache memories in computer systems, which are organised into blocks or lines. When a processor accesses memory and experiences a cache miss, an entire block of memory that includes the requested address is fetched from main memory and stored in the cache. This block usually contains both the requested data and adjacent data. If the program then accesses nearby locations, those accesses will result in cache hits, greatly speeding up execution.

To exploit spatial locality in your code, you can:

- **Access Data in Arrays Sequentially**: This is the most common pattern that takes advantage of spatial locality, as contiguous elements are stored next to each other in memory.

- **Use Data Structures that are Locality-Friendly**: For example, when dealing with matrices, it might be more cache-friendly to use a single-dimensional array that represents a 2D matrix in row-major or column-major order, rather than an array of pointers to arrays.

- **Structure Data Appropriately**: Organise data structures so that related data is stored close together. For instance, using an array of structures (AoS) can be beneficial if you will be accessing many or all of the structure's fields at once. Conversely, a structure of arrays (SoA) can be more efficient if you only need to process a few fields at a time.

- **Block Algorithms (Loop Tiling)**: For algorithms that process large matrices or multi-dimensional arrays, restructure loops to process data in small blocks that fit into the cache.

Here's an example of code that exhibits good spatial locality:

```c
#define SIZE 1024
int sum_matrix(int matrix[SIZE][SIZE]) {
    int sum = 0;
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            sum += matrix[i][j]; // Accessing matrix elements in row-major order
        }
    }
    return sum;
}
```

In the above code, the `matrix` is accessed in row-major order, which means that the elements of any given row are stored contiguously in memory. As the inner loop progresses, it accesses memory locations that are close to each other, thus benefiting from spatial locality.

Improving spatial locality can significantly enhance performance by increasing the cache hit rate. This is particularly important for applications that process large datasets or involve operations on large arrays or matrices, where the cost of accessing main memory can be a significant bottleneck.