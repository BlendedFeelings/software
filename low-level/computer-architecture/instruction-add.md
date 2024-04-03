---
b: https://blendedfeelings.com/software/low-level/computer-architecture/instruction-add.md
---

# Add - instruction in a CPU
is implemented at the hardware level using a combination of digital logic circuits. The process of adding two numbers involves several steps that are carried out by the CPU's arithmetic logic unit (ALU). Here's a simplified overview of how the "add" instruction is typically implemented:

```assembly
ADD R1, R2, R3
```

This instruction is telling the CPU to add the contents of register R2 to the contents of register R3 and store the result in register R1. Here's how the CU would handle this instruction step by step:

### 1. Instruction Fetch
The CU fetches the `ADD` instruction from memory. The address of the instruction is given by the Program Counter (PC), which points to the next instruction to be executed. The fetched instruction is then placed into the Instruction Register (IR).

### 2. Instruction Decode
The CU decodes the fetched instruction in the IR. It understands that `ADD` is an arithmetic operation and identifies R1, R2, and R3 as the operand registers involved.

### 3. Instruction Execution
The CU sends control signals to the Arithmetic Logic Unit (ALU) to perform the addition operation. It also ensures that the data from R2 and R3 are sent to the ALU for this operation.

### 4. Memory Access
In this case, there is no direct memory access required since the operation is between registers. However, if the instruction involved memory (e.g., `LOAD` or `STORE`), the CU would generate the appropriate signals to access memory.

### 5. Register Transfer
Once the ALU has computed the result, the CU controls the transfer of this result from the ALU back to the destination register R1.

### 6. Branch Control
This particular instruction does not involve a branch. However, if there was a branch instruction (e.g., `JMP`, `BEQ`), the CU would update the PC to the new instruction address based on the outcome of the branch condition.

### 7. Control Flow
After executing the `ADD` instruction, the CU updates the PC to point to the next sequential instruction in memory, unless a branch has occurred.

The CU coordinates all these steps, often in a matter of nanoseconds, and it repeats this process for every instruction in a program, thus driving the CPU's operation and enabling it to perform complex tasks.