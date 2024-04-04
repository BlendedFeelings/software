---
b: https://blendedfeelings.com/software/python/global-interpreter-lock-gil.md
---

# Global Interpreter Lock (GIL) 
is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This lock is necessary because CPython's memory management is not thread-safe.

Here's how the GIL works:

1. **Single-threaded Performance**: The GIL allows only one thread to execute Python bytecodes at a time. This simplifies the CPython implementation by making the object model (including critical built-in types like lists and dictionaries) and the garbage collector implicitly safe against concurrent access.

2. **Multithreading Limitations**: Because of the GIL, threads cannot run Python bytecodes in parallel on multiple CPU cores. If you have a multi-threaded program, the GIL can become a bottleneck for performance, especially for CPU-bound programs. This limitation is less significant for I/O-bound programs that spend most of their time waiting for external events.

3. **Workarounds**: To avoid the GIL's limitations, you can use multi-processing instead of multi-threading. The `multiprocessing` module in Python allows you to create separate processes, each with its own Python interpreter and memory space, thus bypassing the GIL and taking full advantage of multiple processors.

4. **Extension Modules**: The GIL can be temporarily released by extension modules that perform lengthy tasks without needing access to Python objects. This allows other threads to run in the meantime. For example, NumPy releases the GIL when doing computationally intensive tasks.

5. **Alternative Implementations**: Some implementations of Python, such as Jython (Python for the Java Virtual Machine) and IronPython (Python for the .NET framework), do not have a GIL. Each thread can execute in parallel without the need for a GIL because these environments have their own garbage collectors that are designed to be thread-safe.

6. **Efforts to Remove the GIL**: There have been various efforts to remove the GIL from CPython or to replace it with a more granular locking mechanism. However, these efforts have often led to reduced single-threaded performance or increased complexity. As of my knowledge cutoff date in April 2023, CPython still has the GIL.

It's important to note that the GIL is specific to the CPython implementation of Python. Other implementations may not have a GIL and may handle concurrency differently.