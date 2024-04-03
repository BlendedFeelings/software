---
b: https://blendedfeelings.com/software/low-level/optimization/alignment.md
---

# Alignment in computing 
refers to arranging data in memory at address boundaries that match the size of the data type or the preferred word size of the processor. Proper alignment is important for performance reasons and, in some cases, is required for correct program execution on certain architectures.

Here are some key points about alignment:

### Why Alignment Matters
- **Performance**: Many processors access memory most efficiently when the data is aligned. Misaligned data can lead to slower memory access, as it might require multiple memory operations to retrieve or store a single piece of data.
- **Hardware Requirements**: Some processors require data to be aligned. Accessing misaligned data on such processors can result in exceptions or faults.
- **Atomic Operations**: For multi-threaded applications, certain atomic operations may require variables to be aligned on specific boundaries to guarantee atomicity.

### How Alignment Works
- **Data Types**: Each data type has a natural alignment, usually the size of the type. For example, a 4-byte integer (on most systems) should be aligned on a 4-byte boundary.
- **Structures**: In structures (or classes), each member should be aligned according to its type, and the structure itself is aligned according to its largest member's alignment requirement.
- **Padding**: Compilers often insert padding bytes into structures to ensure proper alignment of each member.

### How to Ensure Proper Alignment
- **Compiler Directives**: Most compilers provide directives or attributes to specify the desired alignment for data structures. For example, in C and C++, you can use the `alignas` keyword or compiler-specific attributes like `__attribute__((aligned(N)))`.
- **Memory Allocation**: When dynamically allocating memory, use functions that return memory aligned to a suitable boundary, such as `posix_memalign` in POSIX-compliant systems or `std::aligned_alloc` in C++ (C++17 and later).
- **Language Support**: Use language features that automatically enforce alignment. For example, C++'s `std::aligned_storage` or `std::align`.

### Example of Alignment in C++
```c++
#include <iostream>

struct alignas(16) AlignedStruct {
    float x;
    float y;
    float z;
    float w;
};

int main() {
    AlignedStruct as;
    std::cout << "Address of as: " << &as << std::endl;
    std::cout << "Alignment of AlignedStruct: " << alignof(AlignedStruct) << std::endl;
    return 0;
}
```

In this example, `AlignedStruct` is aligned on a 16-byte boundary, which is suitable for SIMD (Single Instruction, Multiple Data) operations that may operate on 128-bit values.

### Considerations
- **Cache Line Size**: Aligning data structures to cache line sizes (typically 64 bytes on modern processors) can help prevent cache line splitting and false sharing in multi-threaded environments.
- **Profile and Measure**: Always profile and measure the performance impact of alignment changes. Over-aligning can increase memory usage without providing additional benefits.

Proper alignment is a low-level optimization that can have a high impact on performance, especially in data-intensive applications. It's important to understand the alignment requirements of the target architecture when writing performance-critical code.