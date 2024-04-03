---
b: https://blendedfeelings.com/software/memory-management/rust.md
---

# Ownership and borrowing in Rust 
is primarily based on the ownership system, which is enforced at compile time by the Rust compiler. The ownership system in Rust has a set of rules that the compiler checks at compile time, and it does not require a garbage collector to clean up unused data. Instead, memory is automatically cleaned up when the owner of the data goes out of scope. Here's an overview of how memory management works in Rust:

### Ownership
Ownership is a set of rules that governs how memory is allocated and deallocated in Rust. The rules are as follows:

1. **Each value in Rust has a single owner** (a variable) that is responsible for managing the memory that the value occupies.
2. **When the owner goes out of scope**, Rust automatically calls the `drop` function, which deallocates the memory associated with the value.
3. **Ownership can be transferred** from one variable to another, a process known as a *move*. After transferring ownership, the original variable can no longer be used to access the value, preventing double-free errors.

### Borrowing
Borrowing is the act of accessing data without taking ownership of it. Rust allows either multiple immutable borrows or one mutable borrow at any given time:

1. **Immutable borrow (`&T`)**: You can create multiple immutable references to a value, allowing read-only access. No mutable references are allowed while immutable references exist.
2. **Mutable borrow (`&mut T`)**: You can create a single mutable reference to a value, allowing read and write access. While a mutable reference exists, no other references (mutable or immutable) are allowed.

### Lifetimes
Lifetimes are Rust's way of ensuring that references do not outlive the data they point to. The compiler uses lifetimes to check that all borrows are valid for the duration of their use.

1. **Explicit lifetimes** are denoted using syntax like `<'a>`, which declares a lifetime `'a`.
2. **Lifetime elision rules** allow the compiler to infer lifetimes in many cases, so explicit annotations are not always necessary.

### Memory Safety Guarantees
Rust's memory management system is designed to provide the following guarantees:

1. **No null pointer dereferencing**: Rust's option types (`Option<T>`) ensure that you handle cases where a value might be `None` (equivalent to `null` in other languages).
2. **No dangling references**: Lifetimes ensure that references do not outlive the data they point to.
3. **No data races**: The borrowing rules prevent data races by ensuring that mutable data cannot be accessed from multiple threads simultaneously without proper synchronization.
4. **No memory leaks**: The ownership system ensures that all memory is freed when it is no longer needed.

Rust's approach to memory management allows developers to write high-performance and safe code without the overhead of a runtime garbage collector. The strict enforcement of ownership and borrowing rules may require a different way of thinking about program design, but it results in more predictable and reliable memory usage.