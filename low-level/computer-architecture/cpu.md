---
b: https://blendedfeelings.com/software/low-level/computer-architecture/cpu.md
---

# CPU Central Processing Unit 
works by carrying out a sequence of operations on data, following the instructions of a computer program. The CPU is the primary component of a computer that performs most of the processing inside a computer. To understand how it works, let's break down the process into several key stages:

1. **Fetch**: The CPU fetches instructions from the computer's memory (RAM). This is done by the control unit (CU), which sends the address of the next instruction to the memory unit and retrieves the instruction from that address.

2. **Decode**: Once an instruction is fetched, it's sent to the instruction decoder, which translates the instruction into signals that can be understood by other parts of the CPU.

3. **Execute**: The decoded instruction is then executed by the relevant parts of the CPU. This could involve the arithmetic logic unit (ALU) for mathematical and logical operations, or it might involve sending signals to other parts of the computer to perform an action, such as reading or writing data to memory.

4. **Memory Access**: If the instruction involves reading from or writing to memory, the CPU will perform this action in the memory access stage. The data needed for the execution might be fetched from memory, or the results of an operation might be written back to memory.

5. **Writeback**: After the execution, the result is written back to a CPU register or memory. This could be the result of a computation or any data that has been processed and needs to be stored.

The CPU operates in a cycle known as the instruction cycle or fetch-decode-execute cycle. Modern CPUs can execute multiple instructions at once through techniques such as pipelining (where different stages of multiple instructions are processed at the same time) and parallelism (where multiple cores can process different instructions simultaneously).

CPUs also have caches, which are small, fast memory locations that store copies of data from frequently accessed main memory locations. There are typically several levels of CPU cache, with L1 being the fastest and smallest, and L3 being slower but larger.

The CPU's performance is influenced by several factors, including its clock speed (measured in GHz), the number of cores it has, the size and speed of its caches, and its architecture (such as x86 or ARM).