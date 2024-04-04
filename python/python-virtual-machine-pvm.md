---
b: https://blendedfeelings.com/software/python/python-virtual-machine-pvm.md
---

# The Python Virtual Machine (PVM) 
is the runtime engine of Python; it's the component that interprets the compiled bytecode of Python programs. When you write a Python program, the source code is first compiled into a format known as bytecode, which is a low-level set of instructions that is platform-independent. This compilation happens just before execution or when the Python file is imported as a module in another Python script.

The bytecode is then executed by the Python Virtual Machine. The PVM is part of the Python interpreter, which is typically referred to as CPython when you're talking about the original implementation that is written in C. The PVM is what makes Python an interpreted language, as the bytecode is not directly executed by the host machine's CPU but is run by the PVM.

The PVM is an abstraction layer that allows Python code to be executed on any machine that has a Python interpreter installed, without needing to modify the code for different operating systems or architectures. This is what makes Python a portable language.

It's important to note that there are other implementations of Python, such as PyPy, Jython, and IronPython, which have their own versions of a virtual machine optimized for different purposes. PyPy, for example, includes a just-in-time (JIT) compiler that can greatly speed up the execution of Python code.

The process of executing a Python program typically involves the following steps:

1. **Writing the source code**: The programmer writes the Python script (`*.py` files).
2. **Compiling to bytecode**: When the script is run, or when it is imported as a module in another script, the Python interpreter compiles the source code into bytecode. This bytecode is a lower-level, platform-independent representation of the source code.
3. **Executing with PVM**: The Python Virtual Machine reads and executes the bytecode. This step involves translating the bytecode instructions into machine code that the computer's CPU can execute, and it happens just-in-time as the bytecode is executed by the PVM.

The PVM is not a separate entity you interact with directly; it's simply a part of the Python interpreter that executes your Python code. When you run a Python script using the `python` command, you're invoking the Python interpreter along with its built-in PVM.