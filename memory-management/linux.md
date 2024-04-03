---
b: https://blendedfeelings.com/software/memory-management/linux.md
---

# Memory management in Linux 
is a complex and sophisticated process, involving several subsystems and algorithms that work together to efficiently use the system's RAM and ensure smooth operation. Here's an overview of some key components and concepts related to memory management in Linux:

1. **Virtual Memory**: Linux uses virtual memory, which means that the memory addresses a program uses are not the same as the physical addresses where the data is actually stored. This abstraction allows for more flexible memory management and enables features like memory protection and swapping.

2. **Page Allocator**: Linux organizes memory into pages, which are typically 4 KB in size on x86 systems. The page allocator is responsible for managing these pages, allocating and freeing them as needed by the system and user processes.

3. **Slab Allocator**: For kernel objects of fixed sizes, Linux uses a slab allocator, which is a memory management system that reduces fragmentation caused by allocations and deallocations of small objects.

4. **Buddy System**: The buddy system is used for allocating memory for use by the kernel itself. It allocates memory in blocks of various sizes, all of which are powers of two. When memory is freed, the buddy system attempts to merge adjacent free blocks into larger ones.

5. **Swapping**: When the system runs out of physical memory, Linux can move inactive pages of memory to a swap space, which is a dedicated area on the disk. This frees up RAM for active processes. Swapping can degrade performance due to the relative slowness of disk access, but it allows the system to handle more memory than is physically available.

6. **Memory Zones**: Linux divides physical memory into zones, such as DMA (Direct Memory Access), Normal, and HighMem, to accommodate the different addressing capabilities of devices and the kernel.

7. **Page Cache**: Linux uses a significant portion of memory as a cache for disk data, known as the page cache. This cache stores pages read from or written to the disk, speeding up disk operations by keeping frequently accessed data in RAM.

8. **OOM Killer**: When the system runs out of memory and cannot reclaim enough to satisfy current demands, the Out-Of-Memory (OOM) Killer may be invoked to forcibly terminate one or more processes to free up memory.

9. **Transparent Huge Pages**: Linux supports the use of huge pages, which are larger than the standard 4 KB pages, to reduce the overhead of managing large amounts of memory and to improve performance by reducing page table lookups.

10. **Memory Overcommit**: Linux allows for memory overcommitment, where it lets processes allocate more memory than is actually available. This is based on the observation that processes often allocate more memory than they use. The kernel employs heuristics to manage overcommitment and ensure system stability.

11. **Control Groups (cgroups)**: Linux provides cgroups as a way to limit and monitor the memory usage of groups of processes, providing a mechanism for resource management across different workloads.

12. **/proc and /sys Filesystems**: Linux exposes a lot of its memory management internals via virtual filesystems like /proc and /sys, where administrators can inspect and sometimes adjust the system's memory management behavior.

13. **Memory Management Unit (MMU)**: The MMU is a hardware component that handles the translation of virtual memory addresses to physical addresses. Linux's memory management subsystem works closely with the MMU to manage the system's memory.

Linux's memory management is designed to be highly efficient and scalable, working well for both small embedded systems and large multi-processor servers. It is continually being developed and improved to handle new hardware architectures and to meet the needs of modern computing workloads.