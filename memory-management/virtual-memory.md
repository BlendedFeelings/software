---
b: https://blendedfeelings.com/software/memory-management/virtual-memory.md
---

# Virtual memory 
is a memory management capability of an operating system (OS) that uses hardware and software to allow a computer to compensate for physical memory shortages, temporarily transferring data from random access memory (RAM) to disk storage. This process is often entirely transparent to the user.

Here's how virtual memory works and some of its key components:

1. **Address Space**: Each process is given its own virtual address space, which is a range of addresses that it can use for its memory needs. The virtual address space is divided into pages, which are typically 4 KB or larger.

2. **Physical Memory**: The actual RAM installed in the system is the physical memory, which is also divided into pages of the same size as the virtual pages.

3. **Page Table**: The operating system maintains a page table for each process, which is a data structure used to map virtual pages to physical pages. If a virtual page is active in memory, the page table contains the physical address where it resides.

4. **Memory Management Unit (MMU)**: The MMU is a hardware component that uses the page table to translate virtual addresses to physical addresses on-the-fly during execution.

5. **Page Fault**: When a process tries to access a part of its virtual address space that is not currently mapped to a physical page (perhaps because it's on the disk), a page fault occurs. The operating system then handles this fault by bringing the required page into physical memory.

6. **Swapping**: The process of moving data between RAM and disk storage is known as swapping or paging. When physical memory becomes full, the operating system may swap out less frequently used pages to the disk to free up RAM for other processes.

7. **Swap Space**: This is the space on a hard drive that is set aside for virtual memory. When the system needs more RAM than is available, it uses the swap space as an overflow, allowing the system to handle larger workloads than would otherwise be possible with just physical memory.

8. **Thrashing**: This occurs when a system spends more time swapping pages in and out of memory than executing the application, leading to poor performance. It usually happens when there is insufficient physical memory to handle the current set of active processes efficiently.

9. **Demand Paging**: Instead of loading an entire process into memory, the operating system loads only the necessary pages into memory, which can be more efficient. Additional pages are loaded as needed, which is known as demand paging.

10. **Memory Overcommit**: Some operating systems allow for memory overcommitment, where they let processes allocate more memory than the total size of physical memory and swap space combined. This is based on the observation that programs often allocate more memory than they use.

Virtual memory provides several benefits:

- **Isolation**: Each process operates in its own virtual address space, which prevents it from accessing memory being used by other processes unless specifically shared.
- **Security**: The separation of address spaces enhances the security of the system by preventing a process from reading or modifying the memory contents of another process.
- **Flexibility**: Processes are not limited by the size of physical memory and can use more memory than is physically available on the system.
- **Efficiency**: Memory can be used more efficiently by only loading the necessary pages into RAM and allowing for better multitasking.

Virtual memory is a fundamental concept in modern computing and is used by nearly all operating systems to extend the effective amount of memory available and to provide a better multitasking experience.