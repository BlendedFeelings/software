---
b: https://blendedfeelings.com/software/low-level/assembly-language/control-flow-function-call.md
---

# Function calls in assembly language 
are generally made using a `call` instruction, which jumps to the address of the function being called and saves the return address on the stack. The exact syntax and conventions for function calls can vary between different assembly languages and architectures, such as x86, ARM, MIPS, etc.

Here's an example of how a function call might look in x86 assembly language:

```assembly
; Assume we have a function named 'myFunction' at some address

section .text
global _start

_start:
    ; Prepare arguments for the function call if necessary
    ; For example, if the function expects an integer argument in the EAX register:
    mov eax, 123

    ; Call the function
    call myFunction

    ; Function has returned, result may be in a register like EAX
    ; Do something with the result

    ; Exit the program (using a system call or similar)
    mov eax, 1      ; syscall number for exit on Linux
    xor ebx, ebx    ; exit code 0
    int 0x80        ; interrupt to make the system call

; The function definition
myFunction:
    ; Function code here
    ; ...

    ; Return from the function
    ret
```

In this example, we assume that the function `myFunction` is defined elsewhere in the code. The `call` instruction will jump to the `myFunction` label, pushing the address of the next instruction (`ret`) onto the stack. When `myFunction` executes the `ret` instruction, it will pop the return address off the stack and jump back to that location, resuming execution after the `call` instruction.

The way arguments are passed to a function can vary. In this example, we used the `EAX` register to pass an integer argument to `myFunction`. The calling convention (which dictates how arguments are passed and how the stack is managed) can differ by platform and compiler settings. Common calling conventions include cdecl, stdcall, and fastcall, among others.