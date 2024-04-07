---
b: https://blendedfeelings.com/software/asynchronous-programming/event-loop.md
---

# Event loop 
is a fundamental concept that manages the execution of tasks in a non-blocking manner. It allows for efficient handling of I/O-bound and other operations that can be executed independently of the main thread of execution. The event loop works by repeatedly collecting and dispatching events or messages in a program.

Here's how the event loop generally works:

1. **Initialization**: When an asynchronous program starts, it initializes the event loop.

2. **Event Queue**: The event loop maintains a queue of events or messages. These events might be the completion of I/O operations, timers expiring, or user interactions like clicks or key presses.

3. **Polling**: The event loop continuously checks (or polls) the queue to see if there are any events that need to be processed.

4. **Callback Execution**: When an event is detected, the event loop takes the corresponding callback function and executes it. A callback function is a piece of code that is scheduled to be executed in response to an event.

5. **Non-blocking**: While the event loop is executing a callback, new events can still be added to the queue. The event loop will not be blocked by the execution of a single callback, as it will complete that execution and then move on to the next event.

6. **Microtasks and Macrotasks**: Some event loops distinguish between different types of tasks. Microtasks are typically small tasks that are executed immediately after the current operation completes, while macrotasks are scheduled to be executed later and may include things like rendering or I/O callbacks.

7. **Concurrency and Parallelism**: Although the event loop itself runs on a single thread, it can achieve concurrency through mechanisms like worker threads or by delegating tasks to the system's I/O facilities, which may run in parallel.

8. **Event Loop Continuation**: After executing a callback, the event loop will continue to run, checking for more events in the queue. This process repeats until there are no more events to process, at which point the program may terminate or continue to wait for new events.

In languages like JavaScript, which is commonly used for web development, the event loop is a critical part of the runtime environment that enables asynchronous programming. Node.js, for example, uses an event-driven architecture that relies on the event loop to handle numerous concurrent connections without creating multiple threads for each connection.

The event loop enables applications to be responsive and efficient, especially in environments where I/O operations are frequent and the cost of thread management is high. It's important to write non-blocking code to take full advantage of the event loop, ensuring that long-running computations do not block the loop and degrade the application's responsiveness.