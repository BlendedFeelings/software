---
b: https://blendedfeelings.com/software/low-level/optimization/cache-thrashing.md
---

# Cache thrashing 
occurs when the working set of a program—the set of data it needs to access frequently—is larger than the cache size, causing constant eviction and reloading of cache lines. This results in a high rate of cache misses, poor cache utilization, and degraded overall performance due to the increased time spent accessing the slower main memory.

To avoid cache thrashing, consider the following strategies:

### 1. Reduce Working Set Size
- **Optimize Algorithms**: Use algorithms with smaller memory footprints or that operate on data in smaller chunks.
- **Data Compression**: Compress data to reduce its size, so that more of it fits into the cache. This is only beneficial if the cost of compression and decompression is less than the cost of cache misses.
- **Selective Data Structures**: Use data structures that store only the necessary data and avoid storing redundant or unnecessary information.

### 2. Increase Temporal and Spatial Locality
- **Loop Blocking (Tiling)**: Break down large loops into smaller blocks that fit into the cache, as previously discussed.
- **Loop Fusion**: Combine loops that access the same data, as previously discussed.
- **Loop Interchange**: Rearrange nested loops to access data in a memory-friendly order, as previously discussed.

### 3. Prefetch Data
- **Software Prefetching**: Insert prefetch instructions to load data into the cache before it is needed, as previously discussed.
- **Hardware Prefetching**: Take advantage of the CPU's hardware prefetching capabilities, which may require tuning the code to exhibit predictable access patterns.

### 4. Use Data Locality Optimizations
- **Data Layout**: Organize data in memory to improve spatial locality, such as using Structures of Arrays (SoA) instead of Arrays of Structures (AoS), as previously discussed.
- **Memory Alignment**: Align data structures to cache line boundaries to prevent cache line splits, as previously discussed.

### 5. Multithreading and Concurrency
- **Thread-Local Storage**: Use thread-local storage for data that is accessed frequently by each thread to prevent false sharing and reduce contention for shared data.
- **Parallel Algorithms**: Design algorithms that can run in parallel with minimal shared data, reducing the likelihood of cache contention between cores.

### 6. Cache-Friendly Data Access Patterns
- **Access Order**: Access data in the order it is laid out in memory to take advantage of the cache's loading mechanism.
- **Strided Access**: If strided access is necessary, ensure that the stride is a multiple of the cache line size to prevent loading unnecessary data into the cache.

### 7. Profile and Analyze
- **Profiling Tools**: Use profiling tools to identify cache bottlenecks and understand the program's memory access patterns.
- **Cache Simulators**: Employ cache simulators to experiment with different cache configurations and access patterns.

### 8. Hardware Considerations
- **Cache Size**: If possible, run the program on hardware with a larger cache to accommodate a larger working set.
- **Cache Architecture**: Understand the cache architecture of the target system, including the size of cache lines, the number of cache levels, and their sizes, to tailor optimizations accordingly.

Avoiding cache thrashing often requires a combination of these strategies. It's important to understand the specific memory access patterns of your program and the characteristics of the target hardware. Profiling and performance analysis are critical steps in identifying cache thrashing issues and verifying the effectiveness of the applied optimizations.