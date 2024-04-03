---
b: https://blendedfeelings.com/software/low-level/assembly-language/control-flow-for-while-do-while.md
---

# Loops in assembly language
are implemented using jump instructions that alter the flow of execution based on certain conditions. The specific instructions used can vary depending on the assembly language and the architecture (e.g., x86, ARM, MIPS). Below are examples of how you might implement `for`, `while`, and `do-while` loops in a generic assembly language for an x86 architecture.

### For Loop
A `for` loop is generally used when the number of iterations is known. Here's a pseudo-assembly code example of a `for` loop:

```assembly
; for loop example
; for (int i = 0; i < 10; i++) {
;     // loop body
; }

    mov ecx, 0      ; Initialize counter (i = 0)
for_loop_start:
    cmp ecx, 10     ; Compare counter with 10
    jge for_loop_end ; If counter >= 10, exit loop

    ; Loop body goes here

    add ecx, 1      ; Increment counter (i++)
    jmp for_loop_start ; Jump back to the start of the loop
for_loop_end:
```

### While Loop
A `while` loop continues as long as a condition is true. Here's a pseudo-assembly code example of a `while` loop:

```assembly
; while loop example
; while (condition) {
;     // loop body
; }

while_loop_start:
    ; Code to evaluate condition
    ; Set the ZF flag if condition is false
    jz while_loop_end ; If condition is false, exit loop

    ; Loop body goes here

    jmp while_loop_start ; Jump back to the start of the loop
while_loop_end:
```

### Do-While Loop
A `do-while` loop executes the loop body at least once and then continues as long as a condition is true. Here's a pseudo-assembly code example of a `do-while` loop:

```assembly
; do-while loop example
; do {
;     // loop body
; } while (condition);

do_while_loop_start:
    ; Loop body goes here

    ; Code to evaluate condition
    ; Set the ZF flag if condition is false
    jnz do_while_loop_start ; If condition is true, repeat loop
```

Keep in mind that these are simplified examples. In a real assembly language program, you would need to handle the loop body and the condition evaluation more specifically, and the actual instructions might differ based on the CPU architecture and the assembler syntax.