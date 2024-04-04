---
b: https://blendedfeelings.com/software/python/interpreted-language.md
---

# Python is interpreted programming language
which means that Python code is executed by an interpreter rather than being compiled into machine code before running. The Python interpreter reads and executes the code line by line, which allows for the dynamic evaluation of expressions and the flexibility to modify the code at runtime.

### Interpreted Language

In the context of programming languages, there are generally two main types of language implementations: compiled and interpreted. Python falls into the latter category.

#### Compiled Languages
- **Compilation**: Compiled languages, such as C, C++, and Rust, require a separate compilation step before execution. In this step, the source code is transformed into machine code by a compiler.
- **Machine Code**: The output of the compilation is often a binary executable file that the CPU can run directly.
- **Performance**: Because the code is pre-compiled into machine code, the execution is typically faster.
- **Platform-Specific**: The compiled binary is usually specific to a particular operating system and hardware architecture.

#### Interpreted Languages
- **Interpreted Execution**: Interpreted languages, like Python, are executed by an interpreter which reads the source code and performs the instructions directly.
- **No Separate Compilation Step**: There is no separate build or compilation step; you can run the program directly from the source code.
- **Line-by-Line Execution**: The interpreter typically processes the program line by line, which may result in slower execution compared to compiled languages.
- **Dynamic Evaluation**: Since the code is not pre-compiled, it allows for dynamic evaluation of expressions. Variables can be created at runtime, and types can change as the program executes.
- **Flexibility**: You can modify the code while the program is running (in certain contexts), which is useful for interactive development and debugging.

### Python's Interpretation Process

When you run a Python script, the Python interpreter takes several steps:

1. **Parsing**: The interpreter reads the source code and parses it into a data structure known as an abstract syntax tree (AST). The AST represents the syntactic structure of the code.

2. **Compilation**: Python does have a compilation step, but it's not to machine code. The AST is compiled into bytecode, which is a low-level, platform-independent representation of the source code.

3. **Execution**: The bytecode is then executed by the Python Virtual Machine (PVM), which is part of the interpreter. The PVM translates the bytecode into machine code instructions that the CPU can execute.

4. **Runtime**: During execution, the interpreter handles memory management, variable storage, and operation execution. It also provides dynamic typing, which means that the types of variables are checked at runtime.

### Benefits and Drawbacks

The interpreted nature of Python provides several benefits:
- **Ease of Use**: Python is user-friendly, with a simple syntax that's easy to learn and read.
- **Portability**: Python code can run on any platform that has a Python interpreter, without modification.
- **Development Speed**: The lack of a separate compilation step speeds up the development cycle. You can write and test code quickly.

However, there are also drawbacks:
- **Performance**: Interpreted languages generally run slower than compiled languages because of the overhead of interpreting code at runtime.
- **Resource Usage**: Interpreters may use more memory and CPU resources compared to running pre-compiled binaries.

Despite these drawbacks, Python's design choices prioritize developer productivity and ease of use over raw execution speed, making it a popular choice for a wide range of applications where the speed of development is more critical than the speed of execution.