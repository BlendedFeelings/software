---
b: https://blendedfeelings.com/software/concurrency/load-link-store-conditional-ll-sc.md
---

# Load-Link/Store-Conditional (LL/SC) 
is a pair of instructions used in concurrent programming to achieve synchronization. It is a mechanism for implementing lock-free data structures in shared memory multiprocessing environments.

Here's how the LL/SC mechanism typically works:

- **Load-Link (LL)**: This instruction reads a value from a memory location and monitors that location for any changes. The processor keeps a record that the load-link operation has been performed on that address.

- **Store-Conditional (SC)**: This instruction attempts to write a new value to the same memory location that was read by the last load-link operation. The store will only succeed if no other writes have been made to that memory location since the load-link operation. If the store is successful, it returns a success code (usually 1 or true); if it fails (because another processor has written to the location), it returns a failure code (usually 0 or false).

The LL/SC pair is used to implement atomic read-modify-write sequences, which are critical for synchronization primitives like mutexes and semaphores. The typical usage pattern is as follows:

1. Perform a load-link operation to read the current value of a variable.
2. Compute a new value based on the read value.
3. Attempt to write the new value using a store-conditional operation.
4. If the store-conditional fails, go back to step 1.

This pattern is repeated until the store-conditional succeeds, indicating that the update was performed atomically and no other process has modified the variable in the meantime.

The LL/SC mechanism is a fundamental building block for many lock-free algorithms, which allow multiple threads to operate on shared data without the overhead of locking, thus improving performance in multi-core systems. However, designing correct lock-free data structures using LL/SC can be complex and requires a deep understanding of concurrent programming principles.