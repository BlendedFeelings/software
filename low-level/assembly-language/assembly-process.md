---
b: https://blendedfeelings.com/software/low-level/assembly-language/assembly-process.md
---

# Assembly process 
is a series of steps an assembler takes to convert assembly language code, which is human-readable, into machine code, which a computer's processor can execute. The process involves defining labels, translating instructions into opcodes, resolving operands, encoding the instructions, handling special directives, and checking for errors. The end result is a machine code output that can be linked to form an executable program.

### First Pass
- **Label Definition and Address Calculation**: The assembler scans the assembly code to identify and record the addresses of all labels (symbols). Labels are used to mark positions in the code, usually for the purpose of jumps, branches, or data references. The assembler creates a symbol table where each label is associated with a memory address.

### Subsequent Passes
- **Translation of Mnemonics**: The assembler translates the assembly language mnemonics (the human-readable instructions) into their corresponding opcodes, which are the numeric codes that the machine understands.
  
- **Operand Resolution**: The assembler resolves the addresses for operands that are used by the instructions. Operands can be immediate values, registers, or memory addresses. If the operand is a label, the assembler uses the symbol table to find the correct address.
  
- **Instruction Encoding**: Each instruction is encoded into a format that the machine can execute. This includes the opcode and the operand(s). The encoding may vary depending on the machine's architecture.

- **Handling Directives**: Assembly language may include directives that tell the assembler to perform specific actions, like allocating space for variables, defining constants, or including other files. These directives are processed during the assembly.

- **Error Checking**: The assembler checks for errors such as undefined labels, syntax errors, invalid instructions, or incorrect operands. If errors are found, the assembler will typically report them to the user.

### Final Output
- **Machine Code**: The final output of the assembler is the machine code, which is a binary representation of the program that can be executed by the machine's processor.

- **Object Files**: The machine code is often output into object files, which can then be linked together with other object files by a linker to create the final executable program.

The exact details of the assembly process can vary depending on the specific assembler and the architecture of the machine it is targeting. Some assemblers might combine some of the passes or perform additional optimizations.