---
b: https://blendedfeelings.com/software/low-level/optimization/cpu-l1-l2-l3.md
---

# L1, L2, and L3 cache in CPU 
is a smaller, faster type of memory that stores copies of the data from the most frequently used main memory locations. Having multiple levels of cache helps improve the efficiency and performance of the CPU by reducing the time needed to access data.

Here's a brief overview of each level:

- **L1 Cache (Level 1 Cache):** This is the fastest and smallest cache level, integrated directly into the CPU chip. It has the shortest latency, which means it can be accessed the quickest, but it has a limited capacity, typically ranging from 2 KB to 64 KB per core. It is used to store instructions and data that the CPU is most likely to need next.

- **L2 Cache (Level 2 Cache):** L2 cache is larger than L1 and is also quite fast, but it has a slightly higher latency than L1 cache. It can be located on the CPU chip or on a separate chip close to the CPU. The size of L2 cache is larger than L1, typically ranging from 256 KB to 2 MB per core, and it serves as an intermediary storage area between the L1 cache and the larger, slower L3 cache.

- **L3 Cache (Level 3 Cache):** This cache level is even larger and is shared across all the cores of the CPU. It has a higher latency than L1 and L2 caches but is still much faster than accessing the main RAM (Random Access Memory). The size of L3 cache can range from 2 MB to tens of MBs per processor package. It helps improve the efficiency of L1 and L2 caches by holding data that is frequently accessed by multiple cores.

The presence of these caches is crucial for a CPU's performance because they reduce the average time to access data from the main memory. When the CPU needs to read or write data, it first checks the L1 cache, then the L2, and finally the L3 cache before it goes to the slower main memory. This hierarchy allows the CPU to work more efficiently by significantly reducing the wait time for data.

When the CPU has to read data from the main memory (often referred to as a cache miss), the data is typically brought into all levels of the cache hierarchy, although the exact behavior can depend on the CPU's architecture and cache organization. Here's a general description of the process:

1. **L1 Cache:** The requested data is loaded into the L1 cache because this is the first level of cache that the CPU will check the next time it needs this data. The L1 cache operates at the speed of the CPU, so it's essential for quick access.

2. **L2 Cache:** At the same time or shortly after the data is loaded into L1, it is also loaded into the L2 cache. This level acts as a bridge between the fast L1 cache and the larger L3 cache. If the data is evicted from the L1 cache (due to its small size and replacement policies), it can still be quickly retrieved from the L2 cache if needed again soon.

3. **L3 Cache:** The data is also loaded into the L3 cache, which is shared across all CPU cores. This level of cache can store more data due to its larger size. If the data is frequently accessed by multiple cores, having it in the L3 cache can reduce the need for those cores to reach out to the slower main memory.

The process of loading data into the cache is known as "cache line fill" or "cache line fetch." When a cache line is fetched from the main memory, it fills the corresponding level of cache and often fills the higher levels of the cache hierarchy as well. This way, if the data is needed again, it can be accessed much more quickly from the cache.

Modern CPUs use sophisticated algorithms to manage cache contents, including which data to load into the cache and when to replace existing data. These algorithms aim to predict which data will be needed soon, maximizing cache hits and minimizing cache misses. The specific strategies used can vary between different CPU designs and manufacturers.