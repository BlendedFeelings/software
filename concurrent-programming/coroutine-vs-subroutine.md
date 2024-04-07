---
b: https://blendedfeelings.com/software/concurrent-programming/coroutine-vs-subroutine.md
---

# Coroutines and subroutines 
are both types of functions used in programming, but they operate differently and serve different purposes.

Also check: [Coroutine](coroutine.md)

### Subroutines (Functions/Procedures/Methods):

A subroutine is a sequence of program instructions that perform a specific task, packaged as a unit. This unit can be called from other parts of a program and may return a value to the caller. Subroutines are the basic building blocks of structured programming and are known by various names in different programming languages, such as functions, procedures, or methods.

**Characteristics of Subroutines:**
- **Linear execution:** Once a subroutine is called, the control flow of the program enters the subroutine, executes all its instructions sequentially, and then returns to the point of call.
- **Stack-based:** Subroutines typically use a stack to keep track of return addresses and local variables. When a subroutine is called, a new stack frame is created.
- **Single entry, single exit:** A subroutine has a single entry point (the beginning of the subroutine) and typically a single exit point, although it may have multiple return statements.
- **No state retention:** Subroutines do not retain state between calls. Each call to a subroutine is independent, and local variables are reinitialized.

### Coroutines:

Coroutines, on the other hand, are similar to subroutines but with the added ability to suspend and resume execution at certain points without losing their state. Coroutines facilitate cooperative multitasking where functions can yield control back to the caller without completing their execution.

**Characteristics of Coroutines:**
- **Cooperative multitasking:** Coroutines work together by yielding control to each other rather than being preemptively scheduled by the operating system.
- **Stateful:** Coroutines retain their state (local variables, instruction pointer, etc.) between yields, allowing them to resume where they left off.
- **Multiple entry points:** Coroutines can have multiple points where execution can be suspended (yielded) and later resumed.
- **Stackless or stackful:** Some coroutine implementations are stackless, meaning they do not use a stack and therefore cannot be nested. Others are stackful, allowing nesting and more complex control flows.

Coroutines are particularly useful in scenarios where tasks need to wait for certain events without blocking the entire program's execution, such as in I/O operations, animations, or handling asynchronous events in user interfaces.

In summary, while subroutines are the traditional way to organize code into callable units, coroutines extend this concept by allowing functions to pause and resume, which is very useful for creating efficient, non-blocking, and concurrent programming patterns.