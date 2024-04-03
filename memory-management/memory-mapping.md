---
b: https://blendedfeelings.com/software/memory-management/memory-mapping.md
---

# Memory mapping 
is a technique that allows files or devices to be mapped into the memory space of a process. This provides a mechanism for applications to access files on disk as if they were part of the application's main memory, enabling efficient file I/O operations and inter-process communication (IPC). Memory mapping is typically managed by the operating system, which provides system calls or APIs for applications to use this feature.

Here's how memory mapping works:

1. **Request Mapping**: The application requests the operating system to map a file or device into its address space. This is done using system calls like `mmap` on Unix-like systems or functions like `CreateFileMapping` and `MapViewOfFile` on Windows.

2. **Create Mapping**: The operating system creates a mapping between the file or device and a range of memory addresses within the process's address space. The actual physical reading of the file data from disk may be deferred until the memory is accessed.

3. **Access Data**: The application can then access the file's contents directly through pointers, as if the data were in regular memory. Reads and writes to this memory range are translated by the operating system into file I/O operations.

4. **Synchronization**: Changes made to the mapped memory are eventually synchronized back to the file on disk. This can be controlled by the application or left to the operating system's page management policies.

5. **Unmapping**: When the application is done with the file, it must inform the operating system to unmap the file from memory, releasing the resources associated with the mapping.

Advantages of memory mapping include:

- **Performance**: Memory mapping can be faster than traditional file I/O operations, particularly for random access and for large files, because it leverages the operating system's virtual memory management and page caching.

- **Simplicity**: The application can use regular memory operations to read from and write to the file, which can simplify coding compared to using read/write system calls.

- **Lazy Loading**: Only the parts of the file that are actually accessed are loaded into memory, which can be efficient for large files where only a small portion is needed at any given time.

- **Shared Memory**: Memory-mapped files can be used for IPC by allowing multiple processes to access the same file mapping, enabling them to share data.

However, there are also some considerations and potential drawbacks:

- **Complexity**: Memory-mapped I/O introduces complexity in handling the lifetime of mappings and ensuring that changes are properly synchronized to disk.

- **Resource Limits**: There may be limits on the number of files that can be mapped or the total amount of memory that can be used for mappings, imposed by the operating system.

- **Portability**: The specific API calls and behavior of memory-mapped I/O can vary between operating systems, which may affect the portability of the code.

Memory mapping is a powerful technique that is widely used in applications that require high-performance file access or IPC, such as databases, web servers, and multimedia applications.