---
b: https://blendedfeelings.com/software/python/library-asyncio.md
---

# Library: asyncio
provides a framework for writing concurrent code using the async/await syntax. It is used to run Python coroutines, which are a way to achieve concurrency in Python. With `asyncio`, you can write single-threaded concurrent code that uses non-blocking I/O operations, which is particularly useful for I/O-bound and high-level structured network code.

Here's a basic example to illustrate how you can use `asyncio` in Python:

```python
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # Run two coroutines concurrently:
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )

    print(f"finished at {time.strftime('%X')}")

# Python 3.7+
asyncio.run(main())
```

In this example, the `say_after` function is a coroutine that takes a `delay` and a message `what` as arguments. It will wait for the specified `delay` and then print the message. The `main` coroutine uses `asyncio.gather` to schedule the execution of two `say_after` coroutines concurrently. The `asyncio.run` function is used to run the main coroutine, which is the entry point for the asyncio program.

Key concepts in `asyncio`:
- **Event Loop**: The core of every asyncio application. It runs in a loop, executing asynchronous tasks and callbacks.
- **Coroutines**: Asynchronous functions defined with `async def`. They are the main building blocks of asyncio applications.
- **Tasks**: Used to schedule coroutines concurrently. When a coroutine is wrapped into a task with functions like `asyncio.create_task()`, it's scheduled to run on the event loop.
- **Futures**: A low-level awaitable object representing an eventual result of an asynchronous operation.
- **async/await syntax**: Used to define and call asynchronous code. The `await` keyword is used to pause the coroutine until the awaited task is complete.

Remember that `asyncio` is part of the Python standard library from version 3.3 onwards, with significant improvements and new features added in subsequent releases. Always refer to the documentation for the version of Python you are using to ensure compatibility with the `asyncio` features you plan to use.