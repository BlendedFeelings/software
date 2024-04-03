---
b: https://blendedfeelings.com/software/low-level/assembly-language/control-flow-if-else-switch.md
---

# Control flow in assembly language 
is managed through a set of instructions that change the flow of execution based on certain conditions. These instructions are typically conditional jumps, calls, and returns. Unlike high-level languages that have `if`, `else`, and `switch` constructs, assembly language uses comparison instructions followed by conditional jump instructions to achieve similar logic.

Here's a basic overview of how conditionals are implemented in assembly language:

### If Statement

An `if` statement is typically implemented using a comparison followed by a conditional jump. If the condition is true, the jump is taken; otherwise, it continues to the next instruction.

```assembly
    cmp ax, bx      ; Compare AX and BX
    jne not_equal   ; Jump to not_equal if AX is not equal to BX (condition for 'if' not met)
    ; Code for 'if' condition met
    ...
not_equal:
    ; Code to execute if the 'if' condition is not met (like 'else')
    ...
```

### If-Else Statement

An `if-else` statement uses a conditional jump to skip over the `else` block if the `if` condition is true.

```assembly
    cmp ax, bx      ; Compare AX and BX
    je equal        ; Jump to equal if AX is equal to BX (condition for 'if' met)
    ; Code for 'else' part
    ...
    jmp end_if      ; Jump to the end of the 'if' block to avoid executing 'else' code
equal:
    ; Code for 'if' part
    ...
end_if:
```

### Switch Statement

A `switch` statement can be implemented using a series of comparisons and jumps, or by using a jump table (also known as a branch table) for more efficient handling of multiple cases.

```assembly
    cmp ax, 1       ; Compare AX with case 1
    je case1        ; Jump to case1 if equal
    cmp ax, 2       ; Compare AX with case 2
    je case2        ; Jump to case2 if equal
    cmp ax, 3       ; Compare AX with case 3
    je case3        ; Jump to case3 if equal
    ; Default case code
    ...
    jmp end_switch
case1:
    ; Code for case 1
    ...
    jmp end_switch
case2:
    ; Code for case 2
    ...
    jmp end_switch
case3:
    ; Code for case 3
    ...
end_switch:
```

Or with a jump table:

```assembly
    ; Assuming AX holds the switch variable
    jmp [jump_table + ax * 4] ; Jump to the address in the jump table indexed by AX

    ; Jump table where each entry is the address of the code for a case
jump_table:
    dd case1
    dd case2
    dd case3
    dd default_case ; Default case

case1:
    ; Code for case 1
    ...
    jmp end_switch
case2:
    ; Code for case 2
    ...
    jmp end_switch
case3:
    ; Code for case 3
    ...
    jmp end_switch
default_case:
    ; Code for default case
    ...
end_switch:
```

Please note that the actual syntax and available instructions can vary depending on the specific assembly language you are using (x86, ARM, MIPS, etc.), and you may need to adjust the instructions accordingly.