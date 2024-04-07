---
b: https://blendedfeelings.com/software/concurrent-programming/fetch-and-add.md
---

# Fetch-and-add operation 
is an atomic operation that performs two actions on a shared variable atomically: it fetches the current value of the variable and then adds a given value to it. The operation is considered atomic because it is completed in a single step from the perspective of other threads, ensuring that no other thread can see an intermediate state or interfere with the operation.

The fetch-and-add operation is often used in scenarios where multiple threads need to update a shared counter or accumulate a sum without causing a race condition. A race condition occurs when multiple threads access and modify shared data concurrently, leading to unpredictable and incorrect results.

Here's a conceptual example of how the fetch-and-add operation works:

1. Thread A wants to increment a shared counter by 1.
2. Thread A performs a fetch-and-add operation on the counter.
3. The operation fetches the current value of the counter.
4. The operation adds 1 to the fetched value.
5. The new value is stored back into the counter.
6. The original value (before addition) is returned to Thread A.

This operation is typically supported directly by hardware (CPU) instructions, which makes it very efficient. In programming languages like C and C++, atomic operations such as fetch-and-add can be performed using the atomic library (e.g., `std::atomic_fetch_add` in C++). In higher-level languages like Java, the `AtomicInteger` class provides methods like `getAndAdd` to perform the operation safely.

The importance of the fetch-and-add operation lies in its ability to help maintain consistency and correctness in concurrent programs by ensuring that updates to shared variables are done without interruption.