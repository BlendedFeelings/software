---
b: https://blendedfeelings.com/software/low-level/assembly-language/addressing-mode.md
---

# Addressing modes in assembly language 
are used to specify how an operand is accessed or manipulated within an instruction. Each addressing mode provides a different method of computing the address of the operand. Here are some common addressing modes used in assembly language:

1. **Immediate Addressing Mode**: The operand is a constant value or an immediate value provided within the instruction. For example:
   ```
   MOV AX, 5 ; Move the immediate value 5 into the AX register
   ```

2. **Register Addressing Mode**: The operand is located in a register, and the register's name is specified in the instruction. For example:
   ```
   MOV AX, BX ; Move the value from the BX register into the AX register
   ```

3. **Direct (or Absolute) Addressing Mode**: The operand's memory address is directly specified in the instruction. For example:
   ```
   MOV AX, [1234h] ; Move the value at memory address 1234h into the AX register
   ```

4. **Indirect Addressing Mode**: The memory address of the operand is contained in a register, and the register is specified in the instruction. For example:
   ```
   MOV AX, [BX] ; Move the value from the memory location pointed to by the BX register into the AX register
   ```

5. **Register Indirect Addressing Mode with Displacement**: The effective address of the operand is the sum of a base register and a displacement value. For example:
   ```
   MOV AX, [BX+10h] ; Move the value from the memory location (BX register + 10h) into the AX register
   ```

6. **Indexed Addressing Mode**: The effective address is the sum of an index register and a displacement value. For example:
   ```
   MOV AX, [SI+20h] ; Move the value from the memory location (SI register + 20h) into the AX register
   ```

7. **Based Indexed Addressing Mode**: Combines both base and index registers with an optional displacement to calculate the address. For example:
   ```
   MOV AX, [BX+SI+30h] ; Move the value from the memory location (BX + SI + 30h) into the AX register
   ```

8. **Relative Addressing Mode**: Used for branching instructions where the operand is a relative offset from the current instruction pointer (IP). For example:
   ```
   JMP label ; Jump to the instruction located at 'label'
   ```

9. **Scaled Indexed Addressing Mode**: Similar to indexed addressing but includes a scaling factor for the index register. This mode is common in more advanced processors like x86-64. For example:
   ```
   MOV AX, [SI*4+100h] ; Move the value from the memory location (SI * 4 + 100h) into the AX register
   ```

Different assembly languages and different processors may have variations or additional addressing modes. The specific syntax and available addressing modes can depend on the assembly language and the architecture you are working with (e.g., x86, ARM, MIPS, etc.).