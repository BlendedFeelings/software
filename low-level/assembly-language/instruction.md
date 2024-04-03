---
b: https://blendedfeelings.com/software/low-level/assembly-language/instruction.md
---

# Instructions  in assembly language 
are used to represent the low-level machine code instructions that the CPU can execute. Each mnemonic typically represents an operation that can be performed by the CPU, such as moving data, performing arithmetic, branching, or manipulating bits. Each assembly language is tied to a particular computer architecture, rather than being portable across multiple systems like high-level languages such as C or Java.

Assembly language instructions typically consist of an opcode (operation code) and zero or more operands. The opcode specifies the operation to be performed, and the operands specify the data to be operated on, which can be immediate values, CPU registers, or memory addresses.

Here are some common types of mnemonic instructions you might encounter in assembly language:

1. **Data Movement Instructions**
   - `MOV`: Move data from one register to another or between a register and memory.
   - `PUSH`: Push a register or memory value onto the stack.
   - `POP`: Pop a value from the stack into a register or memory location.
   - `LEA`: Load effective address into a register.

2. **Arithmetic Instructions**
   - `ADD`: Add two operands.
   - `SUB`: Subtract one operand from another.
   - `MUL`: Multiply two operands.
   - `DIV`: Divide one operand by another.
   - `INC`: Increment a value.
   - `DEC`: Decrement a value.

3. **Logical Instructions**
   - `AND`: Perform a bitwise AND operation.
   - `OR`: Perform a bitwise OR operation.
   - `XOR`: Perform a bitwise XOR operation.
   - `NOT`: Perform a bitwise NOT operation.

4. **Control Flow Instructions**
   - `JMP`: Unconditional jump to another location in the code.
   - `JE` / `JZ`: Jump if equal or jump if zero.
   - `JNE` / `JNZ`: Jump if not equal or jump if not zero.
   - `JG` / `JNLE`: Jump if greater or jump if not less or equal.
   - `JL` / `JNGE`: Jump if less or jump if not greater or equal.
   - `CALL`: Call a procedure or function.
   - `RET`: Return from a procedure or function.

5. **Comparison Instructions**
   - `CMP`: Compare two operands.
   - `TEST`: Test for bitwise AND result without modifying the operands.

6. **Shift and Rotate Instructions**
   - `SHL` / `SAL`: Shift left.
   - `SHR`: Shift right.
   - `ROL`: Rotate left.
   - `ROR`: Rotate right.

7. **String Instructions**
   - `MOVS`: Move string from source to destination.
   - `CMPS`: Compare string operands.
   - `SCAS`: Scan string.
   - `LODS`: Load string.
   - `STOS`: Store string.

8. **I/O Instructions**
   - `IN`: Read from an input port.
   - `OUT`: Write to an output port.

These are just a few examples of the many mnemonic instructions available in assembly language. The exact mnemonics and their usage can vary depending on the CPU architecture (e.g., x86, ARM, MIPS) and the specific assembly language syntax (e.g., Intel syntax vs. AT&T syntax).