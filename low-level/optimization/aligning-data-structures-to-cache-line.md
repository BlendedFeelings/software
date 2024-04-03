---
b: https://blendedfeelings.com/software/low-level/optimization/aligning-data-structures-to-cache-line.md
---

# Aligning data structures to cache line boundaries 
is a technique used to optimize performance by ensuring that the data structure fits within a single cache line or starts at the beginning of a cache line. This can prevent cache line splits, where a data structure straddles two cache lines, leading to increased cache misses and reduced performance. It can also help to avoid false sharing in multi-threaded programs, where two threads modify variables that, while logically independent, are located on the same cache line.

Cache lines are typically 64 bytes on modern processors, but this size can vary. To align data structures to cache line boundaries, you can use compiler-specific directives or language features.

Here's an example in C using the `aligned` attribute in GCC to align a structure to a 64-byte boundary, which is a common cache line size:

```c
#define CACHE_LINE_SIZE 64

struct __attribute__((aligned(CACHE_LINE_SIZE))) AlignedStruct {
    int a;
    // ... other members
};

int main() {
    struct AlignedStruct myData;
    // Use myData
    return 0;
}
```

In C++, you can use the `alignas` specifier introduced in C++11:

```c++
#include <iostream>

constexpr size_t CACHE_LINE_SIZE = 64;

struct alignas(CACHE_LINE_SIZE) AlignedStruct {
    int a;
    // ... other members
};

int main() {
    AlignedStruct myData;
    std::cout << "Address of myData: " << &myData << std::endl;
    std::cout << "Alignment of AlignedStruct: " << alignof(AlignedStruct) << std::endl;
    // Use myData
    return 0;
}
```

When aligning data structures, consider the following:

- **Size of the Data Structure**: Ensure that the entire data structure fits within a cache line to prevent it from spanning multiple cache lines.
- **Memory Overhead**: Over-aligning data structures can lead to increased memory usage due to padding. This trade-off between performance and memory usage should be carefully considered.
- **Access Patterns**: Align data structures based on how they are accessed. If a data structure is frequently accessed as a whole, aligning it to a cache line boundary can be beneficial.
- **False Sharing**: In multi-threaded applications, ensure that each thread accesses data that is on separate cache lines to prevent false sharing, which can degrade performance.

It's important to profile and measure the performance impact of any alignment changes, as the benefits can vary depending on the specific use case and hardware. Additionally, the optimal alignment strategy may differ between single-threaded and multi-threaded applications.