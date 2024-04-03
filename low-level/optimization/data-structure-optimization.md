---
b: https://blendedfeelings.com/software/low-level/optimization/data-structure-optimization.md
---

# Data structure optimization 
involves choosing and organizing data structures in a program to make the best use of the hardware, particularly the memory hierarchy, to improve performance. The goal is to minimize memory access times and make efficient use of caches and registers, which are much faster than main memory.

Here are some key strategies for optimizing data structures:

### 1. Choose the Right Data Structure
Selecting the appropriate data structure for a given task is crucial. For example, an array may be more cache-friendly than a linked list for sequential access patterns due to better spatial locality.

### 2. Structure of Arrays (SoA) vs. Array of Structures (AoS)
An SoA layout can be more cache-efficient than an AoS layout for certain access patterns, especially when you only need to process a few fields of a complex object at a time. In contrast, AoS can be more efficient when you need to access multiple fields of the same object simultaneously.

### 3. Padding and Alignment
Properly aligning data structures in memory can avoid cache line splits and make better use of the available bandwidth. Padding can also be used to ensure that frequently accessed data does not share a cache line with other data (false sharing), which can cause unnecessary cache evictions in multi-threaded environments.

### 4. Compactness
Reducing the size of data structures can lower memory requirements and increase the chance that the data will fit in the cache. This can be achieved by using smaller data types where possible or by compressing data.

### 5. Avoid Indirection
Indirection, such as pointers in linked lists or trees, can lead to poor cache utilization due to the non-contiguous nature of the data. Using arrays or other contiguous data structures can improve spatial locality.

### 6. Data Access Patterns
Organize data structures to match the expected access patterns. For example, if you frequently access several related variables together, store them close to each other in memory.

### 7. Precompute Results
Store precomputed results in the data structure if they will be used frequently. This can avoid repeated calculations at the expense of increased memory usage.

### 8. Cache-Conscious Data Structures
Design data structures that are aware of cache line sizes and the cache hierarchy. For example, B-trees can be optimized to fit nodes within cache lines to reduce memory accesses.

### 9. Hot and Cold Data Splitting
Separate frequently accessed data (hot) from infrequently accessed data (cold) so that the cache is not wasted on data that is rarely used.

### 10. Use of Memory Pools
Allocate memory from pools to ensure that related objects are allocated close to each other in memory, improving spatial locality.

Here's an example comparing AoS and SoA:

```c
// Array of Structures (AoS)
struct PointAoS {
    float x, y, z;
};

PointAoS pointsAoS[N];

// Accessing all x-coordinates (poor spatial locality)
for (int i = 0; i < N; ++i) {
    do_something(pointsAoS[i].x);
}

// Structure of Arrays (SoA)
struct PointsSoA {
    float x[N], y[N], z[N];
};

PointsSoA pointsSoA;

// Accessing all x-coordinates (good spatial locality)
for (int i = 0; i < N; ++i) {
    do_something(pointsSoA.x[i]);
}
```

In the AoS example, accessing all `x` coordinates involves jumping over `y` and `z` in memory, which is not efficient for spatial locality. In the SoA example, all `x` coordinates are stored contiguously, which is much more cache-friendly.

Optimizing data structures is a balance between memory usage, access speed, and the complexity of code. Profiling and benchmarking are essential to determine the impact of any changes on performance.