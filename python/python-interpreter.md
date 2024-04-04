---
b: https://blendedfeelings.com/software/python/python-interpreter.md
---

# Python interpreter 
is a program that reads and executes Python code. Depending on the context, the term "Python interpreter" can refer to the Python runtime environment that directly executes Python source code, or it can refer to the specific program you run to start executing a Python script, often referred to as `python` or `python3` in the command line.

Here's a breakdown of the Python interpreter's role and workflow:

### Role of the Python Interpreter

1. **Parsing**: The interpreter reads the Python source code (`.py` files) and checks for syntax errors. It parses the source code into an abstract syntax tree (AST).

2. **Compilation**: The AST is then compiled into bytecode, which is a lower-level, platform-independent representation of the source code. Bytecode is stored in `.pyc` files within a `__pycache__` directory.

3. **Execution**: The Python Virtual Machine (PVM) executes the bytecode. The PVM is part of the interpreter and runs the bytecode instruction by instruction.

### Workflow of the Python Interpreter

When you execute a Python script, the following steps occur:

1. You run the Python interpreter by using the `python` or `python3` command followed by the name of your Python script file. For example:
   ```
   python my_script.py
   ```
   or
   ```
   python3 my_script.py
   ```

2. The interpreter reads the Python source code file.

3. The source code is parsed and compiled into bytecode if this hasn't been done already or if the source code has changed since the last compilation.

4. The bytecode is then executed by the PVM.

5. As the bytecode is executed, the interpreter performs the actions specified by the bytecode, such as performing calculations, manipulating data, or calling functions.

6. If there are any errors in the code, the interpreter will halt execution and report the errors.

### Interactive Mode

The Python interpreter can also be run in interactive mode, which allows you to type and execute Python code directly in the command line. This is useful for testing small pieces of code, experimenting with Python features, or as a calculator. You can enter interactive mode by simply typing `python` or `python3` without specifying a script file:

```
python
```
or
```
python3
```

### Implementation Variants

- **CPython**: The original and most widely used implementation of the Python interpreter, written in C. When people refer to the Python interpreter without specifying a version, they usually mean CPython.

- **PyPy**: An alternative implementation of Python that includes a just-in-time (JIT) compiler, which can make Python code run faster in many cases.

- **Jython**: A Python interpreter implemented in Java, designed to run on the Java platform and integrate with Java libraries.

- **IronPython**: A Python interpreter implemented in C# for the .NET framework.

Each of these implementations has its own interpreter and, in some cases, its own Python Virtual Machine (PVM) to execute Python code. The choice of interpreter can depend on the specific needs of a project, such as performance requirements, compatibility with other languages or platforms, or the availability of certain libraries.