---
b: https://blendedfeelings.com/software/concurrent-programming/false-sharing.md
---

# False sharing 
is a performance-degrading phenomenon that can occur in multi-threaded environments when threads on different processors modify variables that reside on the same cache line. This situation is problematic because it can cause excessive and unnecessary cache coherency traffic, leading to significant performance penalties.

In modern multi-core processors, each core typically has its own cache (L1, and sometimes L2), and there is a larger shared cache (L3) that is common to all cores. To optimize the speed of data access, these caches are organized into blocks of memory known as cache lines. When a processor core reads or writes to a memory location, the entire cache line containing that memory address is fetched into the core's cache.

Here's why false sharing is an issue:

- When a thread on one core modifies a variable, the cache line containing that variable is marked as dirty.
- If another core has accessed a different variable that happens to be on the same cache line, it will have its copy of that cache line invalidated due to the modification from the first core.
- The second core must then fetch the updated cache line from main memory or another cache where the modified cache line was stored, even if the actual data it needs hasn't changed.
- This invalidation and subsequent cache line transfer happen repeatedly if multiple cores frequently write to different variables on the same cache line, causing significant delays due to the overhead of maintaining cache coherence.

To mitigate false sharing:

- Structure the data to ensure that commonly accessed shared variables are not on the same cache line. This can be achieved by padding data structures or aligning them to cache line boundaries.
- Use thread-local storage for variables that are frequently written by threads, thus avoiding sharing them altogether.
- Be mindful of the size of the cache line in the target architecture (commonly 64 bytes on x86_64 architectures) when designing data structures for multi-threaded applications.

Here's a simple example in C++ that demonstrates padding to avoid false sharing:

```cpp
struct alignas(64) PaddedCounter {
    volatile long value;
    char padding[64 - sizeof(long)]; // Padding to fill out the rest of the cache line
};

struct Counter {
    volatile long value;
};

PaddedCounter paddedCounter1, paddedCounter2;
Counter counter1, counter2; // This might cause false sharing

// Thread 1
void incrementCounter1() {
    for (int i = 0; i < 1000000; ++i) {
        ++paddedCounter1.value;
    }
}

// Thread 2
void incrementCounter2() {
    for (int i = 0; i < 1000000; ++i) {
        ++paddedCounter2.value;
    }
}

// ... Code to launch threads and measure performance ...
```

In the above example, `PaddedCounter` structures are aligned to 64-byte boundaries, which is the typical size of a cache line on x86_64 processors. This alignment ensures that `paddedCounter1` and `paddedCounter2` do not share a cache line, thus preventing false sharing. On the other hand, `Counter` structures without padding might end up on the same cache line, leading to potential false sharing and degraded performance when accessed from different threads.