---
b: https://blendedfeelings.com/software/low-level/computer-architecture/instruction-pipeline.md
---

# CPU instruction pipeline 
is a technique used in the design of modern microprocessors to increase their instruction throughput (the number of instructions that can be executed in a unit of time). The idea is to divide the processing of instructions into several stages, with each stage completing a part of the instruction. As one instruction is being processed in one stage, other instructions can be processed in the other stages. This allows the CPU to work on multiple instructions simultaneously, improving performance.

A typical instruction pipeline might include the following stages:

1. **Fetch (IF)**: The CPU fetches the instruction from memory.
2. **Decode (ID)**: The CPU decodes the instruction to understand what operation is to be performed and which operands are involved.
3. **Execute (EX)**: The CPU performs the operation indicated by the instruction.
4. **Memory Access (MEM)**: If the instruction requires reading from or writing to memory, this is the stage where it happens.
5. **Write Back (WB)**: The results of the computation are written back to the CPU register file or memory.

These stages allow the processor to fetch the next instruction while the previous one is being decoded, and so on, which means that at any given time, multiple instructions are in various stages of execution. This is known as an instruction pipeline.

There are several types of hazards that can occur in a pipelined CPU:

- **Structural Hazards**: Occur when two instructions need the same hardware resource at the same time.
- **Data Hazards**: Occur when an instruction depends on the result of a previous instruction that has not yet completed.
- **Control Hazards**: Occur when the pipeline makes the wrong decision on branch prediction and has to flush and reload instructions.

Modern CPUs employ various techniques to mitigate these hazards, such as out-of-order execution, branch prediction, and speculative execution.