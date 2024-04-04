---
b: https://blendedfeelings.com/software/python/multiprocessing.md
---

# Python's `multiprocessing` module 
is a powerful tool that allows you to create new processes, each running its own instance of the Python interpreter. This is particularly useful for CPU-bound tasks that can be performed in parallel, taking advantage of multiple cores on modern processors.

You might need Python's multiprocessing for several reasons, particularly when dealing with CPU-bound tasks that can benefit from parallel execution. Here are some key reasons to use Python's multiprocessing:

1. **Concurrency**: Multiprocessing allows your program to run multiple operations concurrently, which is especially useful when you have tasks that can be performed independently of each other.

2. **Utilizing Multiple Cores**: Most modern computers have multiple CPU cores. Python's Global Interpreter Lock (GIL) prevents standard threads from executing Python bytecodes in parallel. Multiprocessing bypasses the GIL by using separate processes instead of threads, allowing you to take full advantage of multiple cores by running different processes on each core simultaneously.

3. **CPU-bound Tasks**: If your program is performing computations that require significant CPU time, multiprocessing can help to distribute these tasks across multiple CPUs to reduce the overall processing time.

4. **Blocking I/O Operations**: If your program includes blocking I/O operations, such as reading from or writing to files, network operations, or database transactions, multiprocessing can be used to perform these operations in separate processes, keeping the main program responsive.

5. **Complex Workflows**: When you have a complex workflow where tasks can be broken down into independent units of work, multiprocessing can help to structure these tasks into separate processes that may run in parallel, improving the overall efficiency and structure of your program.

6. **Large Data Processing**: For programs that need to process large datasets, multiprocessing can be used to parallelize data processing, which can significantly speed up the analysis.

7. **Isolation and Stability**: Each process in multiprocessing has its own memory space, which means that processes do not share global variables, leading to better isolation. This can improve the stability of the system because one process crashing will not directly affect the others.

8. **Compatibility with Third-party Libraries**: Some libraries release the GIL and can therefore benefit from multi-threading, but many do not. Multiprocessing does not rely on the behavior of these libraries with respect to the GIL, ensuring compatibility and consistent performance improvements.


Here's a basic example of how to use the `multiprocessing` module to perform a task in parallel:

```python
import multiprocessing

def worker(num):
    """thread worker function"""
    print(f'Worker: {num}')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()  # Wait for all processes to finish
```

In this example, the `worker` function is a simple function that prints out a string containing the number of the worker. The main block of code creates five processes that run this function in parallel with different arguments.

Here are some key concepts and components of the `multiprocessing` module:

- `Process`: This class represents an individual process. You create a new process by instantiating this class and providing the target function and its arguments.

- `start()`: This method starts the process's activity. It must be called at most once per process object.

- `join()`: This method allows the main program to wait for the process to complete. If the optional argument `timeout` is `None` (the default), the method blocks until the process whose `join()` method is called terminates.

- `Pool`: This is a class that provides a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).

Here's an example using `Pool`:

```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == '__main__':
    with Pool(5) as p:  # Pool of 5 processes
        results = p.map(square, range(10))
    print(results)
```

In this `Pool` example, the `square` function is applied to each number in the range from 0 to 9. The `map` method is similar to the built-in `map` function but runs in parallel.

Remember to always protect the entry point of the program using `if __name__ == '__main__':`. This ensures that the code that creates new processes is not executed when the module is imported, which could lead to unintended behavior or errors.