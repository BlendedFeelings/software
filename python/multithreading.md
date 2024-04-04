---
b: https://blendedfeelings.com/software/python/multithreading.md
---

# Multithreading in Python 
can be achieved using the `threading` module, which is included in the Python Standard Library. The `threading` module allows for the creation and synchronization of multiple threads, which are sequences of instructions that can run concurrently within a single process.

It's important to note that due to the Global Interpreter Lock (GIL) in the CPython implementation of Python, threads do not actually run in parallel on multiple CPU cores. Instead, they take turns executing within a single process. This means that multithreading in Python is most beneficial for I/O-bound tasks rather than CPU-bound tasks. For CPU-bound tasks, multiprocessing (using the `multiprocessing` module) is often a better approach as it can leverage multiple CPU cores.

Here is a basic example of how to use multithreading in Python:

```python
import threading

# This is a simple function that prints numbers
def print_numbers():
    for i in range(1, 6):
        print(i)

# This is another function that prints letters
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution")
```

In this example, two threads are created: one to print numbers and another to print letters. Each thread is started with the `start()` method, and the `join()` method is used to wait for each thread to finish before the main program continues.

Keep in mind that when working with threads, it's crucial to manage shared resources carefully to avoid race conditions and ensure thread safety. This can be achieved using synchronization mechanisms provided by the `threading` module, such as Locks, Semaphores, Events, and Conditions.