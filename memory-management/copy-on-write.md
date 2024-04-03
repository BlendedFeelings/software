---
b: https://blendedfeelings.com/software/memory-management/copy-on-write.md
---

# Copy-on-Write (CoW) 
is a resource management technique used in computer programming to efficiently copy data resources, such as files or memory pages. When a system employs CoW, it allows multiple users or processes to share the same instance of a resource until one of them makes a modification, at which point a separate copy of the resource is created for that user or process. This deferred copying is used to optimize both memory usage and performance.

Here's how Copy-on-Write typically works:

1. **Initial Sharing**: When a copy operation is requested, rather than immediately creating a full duplicate of the resource, the system allows all requesting entities to reference the same instance of that resource.

2. **Write Detection**: The system keeps track of any attempts to modify the shared resource. This is usually done through mechanisms like page protection in a virtual memory system, where the memory page is initially marked as read-only.

3. **Deferred Copying**: If a modification is attempted by any of the entities, the system intercepts the operation (often through a page fault in the case of memory pages).

4. **Actual Copying**: Upon detecting a write attempt, the system creates a new copy of the resource just for the entity making the modification. This entity is then given write access to the new copy, while the other entities continue to share the original resource.

5. **Continued Isolation**: After the copy is made, changes to the new copy do not affect the original resource or any other entities that are referencing it.

The advantages of Copy-on-Write include:

- **Efficient Memory Usage**: CoW can significantly reduce memory usage when many copies of the same data are required but few modifications are made.

- **Performance**: It avoids the overhead of copying entire resources when duplicating them, which can lead to performance improvements, especially when dealing with large data sets.

- **Atomic Operations**: CoW can help ensure atomicity in operations, as the copying process can be done in a way that does not interfere with other operations on the resource.

- **Forking Processes**: CoW is commonly used in the implementation of the `fork` system call in Unix-like operating systems. The child process initially shares the same memory pages as the parent process, and pages are only copied when one of the processes writes to them.

However, CoW also has some considerations:

- **Write Penalty**: When a write does occur, there is a performance penalty due to the need to copy the resource at that time.

- **Complex Implementation**: Managing CoW requires additional logic in the system to handle the deferred copying and to track when writes occur.

- **Fragmentation**: Over time, as writes occur, the system may become more fragmented, with multiple copies of various parts of the resource.

Copy-on-Write is used in various systems, including operating systems (for efficient process forking), file systems (like ZFS and Btrfs), and programming languages/runtime libraries (such as the implementation of copy-on-write strings in PHP or the copy-on-write semantics of certain container types in C++'s Standard Template Library).