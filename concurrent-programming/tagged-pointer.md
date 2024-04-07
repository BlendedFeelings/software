---
b: https://blendedfeelings.com/software/concurrent-programming/tagged-pointer.md
---

# Tagged pointers in concurrent programming 
are a technique used to solve some of the issues related to memory management and synchronization in multi-threaded environments. This technique is especially useful in lock-free and wait-free algorithms, where it helps to avoid the ABA problem.

The ABA problem occurs when a memory location is read by thread A, which then gets preempted. Meanwhile, thread B changes the value of the memory location and then changes it back to the original value. When thread A resumes, it sees the same value (A) even though the value has changed in the meantime (to B and back to A), leading to incorrect behavior because thread A doesn't realize the change has occurred.

Tagged pointers address this issue by adding a tag or version number to the pointer. Each time the memory location is modified, the tag is incremented. This way, even if the value at the memory location is set back to the original value, the tag will be different, and threads can detect that a change occurred.

Here's how tagged pointers work:

1. **Pointer Representation**: A tagged pointer combines a memory address with a tag (usually a small integer). Since most modern architectures have memory addresses that are aligned (e.g., on 4 or 8-byte boundaries), the least significant bits of the address are typically zero. These bits can be used to store the tag.

2. **Atomic Operations**: Operations on tagged pointers must be atomic to ensure that both the pointer and the tag are updated together without interference from other threads. This is commonly achieved using atomic compare-and-swap (CAS) operations.

3. **Memory Reclamation**: Tagged pointers can help with memory reclamation in lock-free data structures by ensuring that a thread can detect if a node has been removed and possibly freed, even if a new node has been allocated at the same address.

Here's an example of how a tagged pointer might be represented in C++:

```cpp
#include <cstdint>
#include <atomic>

// Assume that pointers are aligned to 4 bytes, so we can use the last 2 bits for the tag.
const uintptr_t TAG_MASK = 0x3; // Mask to extract the tag.

struct TaggedPointer {
    std::atomic<uintptr_t> ptr;

    void* getPointer() const {
        return reinterpret_cast<void*>(ptr.load(std::memory_order_acquire) & ~TAG_MASK);
    }

    uint32_t getTag() const {
        return ptr.load(std::memory_order_acquire) & TAG_MASK;
    }

    void setPointer(void* pointer, uint32_t tag) {
        uintptr_t newPtr = reinterpret_cast<uintptr_t>(pointer);
        newPtr |= (tag & TAG_MASK);
        ptr.store(newPtr, std::memory_order_release);
    }

    bool compareAndSwap(void* oldPointer, uint32_t oldTag, void* newPointer, uint32_t newTag) {
        uintptr_t oldPtr = reinterpret_cast<uintptr_t>(oldPointer) | (oldTag & TAG_MASK);
        uintptr_t newPtr = reinterpret_cast<uintptr_t>(newPointer) | (newTag & TAG_MASK);
        return ptr.compare_exchange_strong(oldPtr, newPtr, std::memory_order_acq_rel);
    }
};
```

In this example, the `TaggedPointer` structure encapsulates an atomic pointer with a tag. The `getPointer` and `getTag` methods allow you to retrieve the pointer and tag separately. The `setPointer` method sets the pointer and tag atomically, and the `compareAndSwap` method performs an atomic compare-and-swap operation that checks both the pointer and the tag.

Tagged pointers are a low-level optimization technique, and their use requires careful consideration of the target architecture and alignment guarantees. They are particularly useful in implementing non-blocking data structures where avoiding locks can result in significant performance improvements in concurrent environments.