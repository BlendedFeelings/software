---
b: https://blendedfeelings.com/software/memory-management/call-stack.md
---

# Call stack 
often simply referred to as "the stack," is a special region of computer memory that stores information about the active subroutines (also known as functions or methods) of a computer program. This data structure is a stack because it operates in a last-in, first-out (LIFO) manner, meaning that the most recently called subroutine is the first to be completed and removed from the stack.

The call stack is used for several important tasks in program execution:

1. **Function Call Management**: When a function is called, a new frame (also called a stack frame or activation record) is pushed onto the call stack. This frame contains the function's return address, parameters, local variables, and sometimes the state of the CPU registers.

2. **Local Variable Storage**: Each stack frame provides storage for the local variables of its function. These variables are only accessible while their function is executing.

3. **Return Address**: When a function is called, the address of the instruction to return to upon completion of the function is stored in the stack frame. This ensures that the program can continue executing from the right place after a function returns.

4. **Nested Function Calls**: The call stack keeps track of nested function calls. When a function calls another function, a new frame is pushed onto the stack. When the called function completes, its frame is popped from the stack, and control returns to the calling function.

5. **Stack Unwinding**: In the event of an error or exception, the call stack can be unwound to remove frames until a suitable error handler is found.

Here's a simple illustration of how the call stack operates with function calls:

```
// Pseudocode
function main() {
    doSomething();
}

function doSomething() {
    int localVariable = 10;
    doSomethingElse(localVariable);
}

function doSomethingElse(value) {
    // ...
}

// Call stack representation during execution:
[Bottom of Stack]
main frame (with its return address and any local variables)
doSomething frame (with its return address and localVariable)
doSomethingElse frame (with its return address and parameter 'value')
[Top of Stack]
```

The stack's operation is largely managed by the CPU with support from the operating system. It is a critical structure for the control flow of most modern programming languages, although the specifics of how it is implemented can vary between programming languages and machine architectures. The stack is fast and efficient but has a limited size, which is determined at the start of the program. If the stack overflows—usually due to excessively deep or infinite recursion or excessive allocation of local data—this can lead to a stack overflow error, potentially causing the program to crash.