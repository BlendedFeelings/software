---
b: https://blendedfeelings.com/software/low-level/assembly-language/assembly-language.md
---

# Assembly language 
is a low-level programming language that is specific to a computer architecture. It is one step above machine code and is translated into machine code through an assembler. Assembly language is used when a programmer needs to directly manipulate hardware, access specialized processor instructions, or achieve maximum performance.

Here's an example of a simple assembly language code snippet that adds two numbers on an x86 architecture processor:

```assembly
section .data
    num1 db 0x01        ; Define byte num1 with value 1
    num2 db 0x02        ; Define byte num2 with value 2
    result db 0x00      ; Define byte result with value 0

section .text
    global _start

_start:
    mov al, [num1]      ; Move the value of num1 into register AL
    add al, [num2]      ; Add the value of num2 to the value in register AL
    mov [result], al    ; Move the result back into the variable result

    ; Exit the program
    mov eax, 1          ; The syscall number for exit is 1
    mov ebx, 0          ; Return a code of 0
    int 0x80            ; Call kernel
```

This code is written for NASM (Netwide Assembler), a popular assembler for x86 architecture. It defines two bytes in the data section with values 1 and 2, respectively, and a result byte initialized to 0. In the text section, it moves the first number into the AL register (the lower 8 bits of the AX register), adds the second number to it, and then stores the result back into the result variable. Finally, it exits the program using a system call.

Keep in mind that assembly language syntax and instructions vary widely between different architectures (such as x86, ARM, MIPS, etc.), and the above code will not work on other architectures without modification.