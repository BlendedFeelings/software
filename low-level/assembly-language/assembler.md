---
b: https://blendedfeelings.com/software/low-level/assembly-language/assembler.md
---

# Assemblers 
are software tools that convert assembly language code, which is a low-level programming language that is just a step above machine code, into machine code that can be executed by a computer's CPU. Here's an overview of how assemblers perform this conversion:

1. **Lexical Analysis**: The assembler scans the assembly language code to identify tokens. Tokens are the basic building blocks of the code, such as mnemonics (operation codes like `MOV`, `ADD`, `SUB`), symbols (labels or variable names), directives (commands to the assembler itself, like `.data` or `.text`), and literals (constants like numbers or character strings).

2. **Syntax Analysis**: The assembler parses the tokens to understand the grammatical structure of the assembly code. It checks that the tokens follow the correct syntax for the assembly language, which is defined by the instruction set architecture of the target CPU.

3. **Symbol Resolution**: The assembler creates a symbol table to keep track of all the labels and variables defined in the code. This step involves assigning addresses to these symbols.

4. **Assembly Directives Handling**: The assembler processes any directives found in the code. Directives are not translated into machine code but are instructions to the assembler itself, such as reserving memory space or setting the location counter (the pointer that keeps track of the current assembly address).

5. **Code Generation**: The assembler translates each instruction into its corresponding machine code. This involves converting mnemonics to opcode (the numeric representation of the operation) and operands to the appropriate format, such as register numbers or memory addresses.

6. **Relocation**: If the code is to be loaded at a different memory address than it was assembled for, the assembler adjusts the addresses in the machine code accordingly.

7. **Object Code Generation**: The assembler outputs the machine code, often in the form of an object file, which contains the machine code along with additional information such as relocation information and symbol table entries.

8. **Linking (optional)**: While not strictly part of the assembly process, the assembler may work with a linker to combine multiple object files into a single executable. The linker resolves references between different object files and combines them into a final executable or library.

The exact details of these steps can vary depending on the specific assembler being used and the CPU architecture for which the code is being assembled. The output of the assembler, the machine code, is a binary representation of the instructions that the CPU can execute directly.


Let's walk through a simple example of how an assembler would convert a snippet of assembly language code into machine code. We'll use a hypothetical assembly language for illustration purposes.

Here's our assembly language code:

```assembly
; Example Assembly Code
section .data
    msg db 'Hello, world!', 0

section .text
global _start

_start:
    mov edx, len    ; Message length
    mov ecx, msg    ; Message to write
    mov ebx, 1      ; File descriptor (stdout)
    mov eax, 4      ; System call number (sys_write)
    int 0x80        ; Call kernel

    mov eax, 1      ; System call number (sys_exit)
    int 0x80        ; Call kernel

len equ $ - msg     ; Calculate message length
```

Here's what the assembler does with this code:

1. **Lexical Analysis**:
   - It identifies tokens such as `section`, `.data`, `.text`, `global`, `_start`, `mov`, `int`, `db`, etc.

2. **Syntax Analysis**:
   - The assembler checks that the instructions are valid, e.g., `mov` is followed by two operands.

3. **Symbol Resolution**:
   - It creates a symbol table with entries for `msg`, `_start`, and `len`.

4. **Assembly Directives Handling**:
   - `section .data` and `section .text` are directives that tell the assembler to switch between data and code sections.
   - `db` is a directive that defines a byte of data.
   - `global` is a directive that makes the `_start` label visible to the linker.

5. **Code Generation**:
   - Each instruction is translated into machine code:
     - `mov edx, len` becomes something like `BA 0000000D` (hypothetical opcode `BA` for `mov` to `edx` and `0000000D` is the length of the message in bytes).
     - `mov ecx, msg` becomes `B9 00000004` (hypothetical opcode `B9` for `mov` to `ecx` and `00000004` is the address of the message).
     - And so on for the rest of the instructions.

6. **Relocation**:
   - If necessary, the assembler adjusts the addresses in the machine code based on where the code will be loaded in memory.

7. **Object Code Generation**:
   - The assembler outputs an object file with the machine code and additional information such as the symbol table and relocation entries.

8. **Linking (optional)**:
   - If there are multiple object files, a linker combines them into a single executable, resolving any external references.

The actual machine code would be a sequence of bytes that represent the instructions and the data. For the `mov` instructions, the machine code would include the opcode for `mov` along with the encoded operands (register identifiers and immediate values or addresses). The string `'Hello, world!'` would be stored as a sequence of ASCII values followed by a null terminator `0`. The `int 0x80` instruction would be encoded with its specific opcode and the interrupt number `0x80`.

Please note that the actual opcodes and the way operands are encoded can vary significantly between different CPU architectures and assemblers. The above example is purely illustrative and not based on a specific architecture.