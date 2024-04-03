---
b: https://blendedfeelings.com/software/memory-management/stack-frame.md
---

# Stack frame
also known as an activation record or a function frame, is a data structure that contains information necessary for the execution of a function within a program. Each time a function is called, a new stack frame is created and pushed onto the call stack. When the function returns, its stack frame is popped from the stack. The stack frame is critical for managing the return addresses, parameters, local variables, and the state of the CPU registers for each function call.

Here's what a typical stack frame contains:

1. **Return Address**: This is the instruction address to which control should return after the function completes. It ensures the program execution continues from the correct location in the calling function.

2. **Function Parameters**: These are the arguments passed to the function. They are used within the function for various computations and operations.

3. **Local Variables**: Each function may declare variables local to its scope. These are stored in the stack frame and are accessible only while the function is executing.

4. **Saved Registers**: Depending on the calling convention and the CPU architecture, certain registers may need to be saved and restored when a function is called. These saved registers are often part of the stack frame.

5. **Control Information**: This can include the previous frame pointer (which points to the stack frame of the calling function) and other bookkeeping information necessary for the correct operation of the call stack.

6. **Optional Information**: Depending on the language and runtime, the stack frame may also include space for temporaries, space for saving the condition code register, and other function-specific data.

A stack frame is laid out in memory as follows (the exact structure can vary by CPU architecture and calling convention):

```
[Top of Stack]
-------------------------
Local Variables
-------------------------
Saved Registers
-------------------------
Control Information
-------------------------
Function Parameters
-------------------------
Return Address
-------------------------
[Bottom of Stack]
```

When a function is called, the CPU (with the help of the compiler-generated code) performs the following steps:

1. **Push the return address onto the stack**: The address of the instruction following the function call is saved.
2. **Set up the new stack frame**: Space is allocated on the stack for the function's parameters, local variables, and saved registers.
3. **Execute the function**: The CPU begins executing the function's code with the new stack frame as its context.
4. **Clean up and return**: When the function completes, its return value (if any) is stored in a designated register or stack location, the stack frame is dismantled, and control is transferred back to the return address.

The management of the stack and its frames is a key aspect of a program's runtime environment and is crucial for supporting nested function calls, recursion, and the orderly execution of code.