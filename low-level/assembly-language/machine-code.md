---
b: https://blendedfeelings.com/software/low-level/assembly-language/machine-code.md
---

# Assembly Language and Machine Code
Assembly language is a step above machine code, providing a more readable format for programmers. It uses mnemonics to represent the basic instructions that the CPU can execute, along with symbolic names for memory locations (labels) and constants. Each mnemonic corresponds to an opcode, which is the instruction for the CPU, and operands, which are the targets of the instruction (such as registers or memory addresses).

Machine code, on the other hand, is a binary representation of these instructions that the CPU can directly understand and execute. It consists of sequences of 0s and 1s organized into bytes that represent opcodes and operands.

Each type of CPU has its own specific machine code instruction set, which dictates what operations the CPU can perform. These operations include arithmetic calculations, data movement, and control flow instructions, among others.

Machine code is not typically written by humans; instead, programmers write code in higher-level programming languages, which are then compiled or assembled into machine code that the CPU can execute. The process of converting high-level code to machine code is handled by compilers and assemblers.

Here's an example of what machine code might look like, although it's important to note that it's not practical to read or write machine code directly in this form:

```
10110000 01100001  // MOV AL, 61h - Move the hexadecimal value 61 into the AL register
11101111           // OUT 0F8h, AL - Output the value in AL to the port with address F8h
```

In this example, the first line is an instruction that moves a value into a register, and the second line is an instruction that sends the value in that register to an output port. This is a simplified representation; actual machine code would be entirely in binary and specific to the CPU's instruction set.