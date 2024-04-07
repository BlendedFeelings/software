---
b: https://blendedfeelings.com/software/concurrent-programming/cooperative-multitasking.md
---

# Cooperative multitasking 
also known as non-preemptive multitasking, is a style of multitasking where the currently running task must offer control back to the multitasking system explicitly. This is in contrast to preemptive multitasking, where the operating system can interrupt and switch between tasks at any time.

In cooperative multitasking, each task is responsible for yielding control periodically to ensure that other tasks get a chance to run. This approach relies on the cooperation of tasks to manage the sharing of the CPU, hence the name "cooperative". It is up to the programmer to ensure that tasks do not monopolize CPU time.

Advantages of cooperative multitasking include:

1. **Simplicity**: It is generally simpler to implement and understand than preemptive multitasking because there is no need for complex mechanisms to protect shared resources from concurrent access.
2. **Performance**: Overhead can be lower since there is no need for context switching by the operating system, which can be expensive in terms of performance.
3. **Determinism**: It can be more deterministic because tasks run until they yield, making it easier to reason about the order of execution.

However, there are also significant disadvantages:

1. **Reliability**: If a task does not yield or has an infinite loop, it can hang the entire system since no other task can run.
2. **Responsiveness**: System responsiveness can suffer since a long-running task can block other tasks from executing.
3. **Concurrency**: It is more challenging to implement concurrent operations since tasks must be carefully designed to yield frequently.

Examples of cooperative multitasking can be found in early operating systems and runtime environments. For instance, Windows 3.x and Mac OS before version 9 used cooperative multitasking. In modern software development, cooperative multitasking is often seen in the form of event loops in asynchronous programming frameworks and in languages that support coroutines or fibers.

In languages that support coroutines, cooperative multitasking can be achieved by having coroutines yield execution back to an event loop or scheduler. For example, in Python, the `asyncio` library provides an event loop that manages the execution of coroutines, which yield control using the `await` keyword.

Here is a simple example of cooperative multitasking using Python's `asyncio`:

```python
import asyncio

async def task1():
    for i in range(3):
        print('Task 1 iteration', i)
        # Yield control back to the event loop
        await asyncio.sleep(1)

async def task2():
    for i in range(3):
        print('Task 2 iteration', i)
        # Yield control back to the event loop
        await asyncio.sleep(1)

# Run both tasks in the event loop
async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

In this example, `task1` and `task2` are coroutines that yield control back to the event loop with `await asyncio.sleep(1)`. This allows the event loop to switch between the tasks, simulating cooperative multitasking.