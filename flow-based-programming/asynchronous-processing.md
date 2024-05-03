---
b: https://blendedfeelings.com/software/flow-based-programming/asynchronous-processing.md
---

# Asynchronous processing 
is handled by allowing independent components to concurrently execute and communicate through non-blocking data streams, supporting parallelism and event-driven execution.

Here's how FBP handles asynchronous processing:

1. **Component Independence**: Each component in an FBP network is independent and encapsulates a specific piece of logic. Components can process data at their own pace, without having to wait for other components to complete their work. This allows for asynchronous and parallel execution.

2. **Data Streams**: Components communicate by sending and receiving data streams via connections. These streams can be thought of as asynchronous message queues or pipes, where data can flow from one component to another without requiring a synchronous handshake.

3. **Non-blocking I/O**: FBP encourages the use of non-blocking input/output operations. When a component performs I/O, it doesn't need to block and wait for the operation to complete; it can yield control so that other components can continue processing.

4. **Back-pressure**: In FBP, back-pressure is a mechanism that allows components to handle the flow of data at a manageable pace. If a downstream component is slower in processing messages, it can exert back-pressure to slow down the upstream component, preventing it from sending data too quickly. This is an important aspect of asynchronous processing, ensuring that the system remains stable under load.

5. **Event-driven Execution**: Components can be event-driven, responding to incoming data events as they occur. This model fits well with asynchronous processing, as components can be triggered by the arrival of new data without polling or waiting synchronously.

6. **Concurrency Models**: FBP supports various concurrency models, such as threads, event loops, or actor systems, to manage the asynchronous execution of components. The choice of concurrency model can affect how components are scheduled and how they communicate.

7. **Buffers and Queues**: FBP often uses buffers and queues to manage the asynchronous flow of data between components. These can help to decouple the production and consumption rates of data, allowing components to operate independently.

8. **Error Handling**: Asynchronous processing can lead to complex error-handling scenarios. FBP typically handles errors by sending error messages through the network, allowing components to react accordingly or pass the error on for centralized handling.

In summary, FBP is well-suited for asynchronous processing due to its architecture, which naturally separates concerns, allows for concurrent execution, and provides mechanisms for handling asynchronous data flow and back-pressure. This makes it a good fit for applications that require high levels of parallelism, such as data processing pipelines, network servers, and distributed systems.