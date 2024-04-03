---
b: https://blendedfeelings.com/software/low-level/assembly-language/register.md
---

# Registers in assembly language
are like small, fast storage spaces within the central processing unit (CPU) that the CPU uses to quickly access data and control the flow of a program. They are used for a variety of purposes, such as holding operands for arithmetic operations, addressing memory, holding pointers, and more.

Here's a simplified explanation of the common types of registers:

1. **General-Purpose Registers (GPRs)**: These are like multipurpose boxes where the CPU can store and manipulate numbers for various tasks like calculations, temporarily holding data, and managing memory addresses.

2. **Index Registers**: Think of these as counters or pointers that help the CPU go through lists or arrays of data, often used in loops or to move through data in steps.

3. **Base Pointer (BP)**: This is like a bookmark that keeps track of the starting point of a stack frame, which is a section of the stack used for managing function calls and local variables.

4. **Stack Pointer (SP)**: Imagine this as a marker that always points to the topmost item in a stack of plates. Whenever a new plate is added or the top one is removed, the marker moves accordingly.

5. **Instruction Pointer (IP)**: This is like a cursor that indicates which line of code (instruction) the CPU will read and execute next.

6. **Segment Registers**: These are like labels that mark different sections of memory for specific uses, such as one for code, another for data, and one for the stack.

7. **Flags Register**: This register contains a series of switches that the CPU flips on or off to indicate the status of recent operations, such as whether the last calculation resulted in zero or if it was too large for the CPU to handle.

8. **Floating-Point Registers (FPRs)**: These are special boxes used for calculations with decimal numbers, allowing the CPU to perform math that involves fractions or very large and very small numbers.

The exact set of registers and their names can vary significantly between different CPU architectures. The above examples are based on the Intel x86 and x86-64 architectures, which are among the most commonly used. Other architectures, such as ARM, MIPS, and PowerPC, have their own sets of registers and conventions.