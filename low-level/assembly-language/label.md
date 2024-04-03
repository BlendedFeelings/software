---
b: https://blendedfeelings.com/software/low-level/assembly-language/label.md
---

# Labels in assembly language 
are used as markers that refer to a particular point in the code. They are essentially symbolic names given to memory addresses, allowing programmers to write more readable and maintainable code. Labels can be used to mark the start of a function, a loop, or a conditional block, and are often used in conjunction with jump, branch, or call instructions to control the flow of the program.

Here's a simple example of how labels are used in assembly code:

```assembly
section .text
global _start

_start:          ; This label marks the beginning of the code
    mov eax, 1   ; Move the value 1 into the EAX register
    mov ebx, 0   ; Move the value 0 into the EBX register
    add eax, ebx ; Add the value in EBX to EAX

loop_start:      ; This label marks the beginning of a loop
    dec eax      ; Decrement the value in EAX
    jnz loop_start ; Jump to loop_start if EAX is not zero

end_program:     ; This label marks the end of the program
    mov eax, 60  ; Move the value 60 (exit syscall) into EAX
    xor edi, edi ; Zero out EDI (exit status)
    syscall      ; Make the syscall to exit the program
```

In this example, `_start`, `loop_start`, and `end_program` are labels. The `jnz` (jump if not zero) instruction uses the `loop_start` label to jump back to the beginning of the loop if the `eax` register is not zero. The `end_program` label is used to mark the end of the program, where the syscall to exit is made.

Labels are a fundamental part of assembly language and are crucial for controlling the execution flow of a program. They are also used to define entry points for functions and to create references for data sections in the program.