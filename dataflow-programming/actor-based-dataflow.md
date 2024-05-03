---
b: https://blendedfeelings.com/software/dataflow-programming/actor-based-dataflow.md
---

# Actor-based dataflow 
is a programming paradigm that combines concepts from both dataflow programming and the actor model. In dataflow programming, the computation is structured around the flow of data, with the output of one operation becoming the input for another. The actor model, on the other hand, involves encapsulating computation and state within entities called actors that communicate through message passing.

Here's how actor-based dataflow works:

1. **Actors**: In actor-based dataflow, each actor represents a node in the dataflow graph. Actors can be thought of as independent units of computation that have their own internal state and behavior. They process incoming messages/data and produce output messages/data.

2. **Asynchronous Message Passing**: Actors communicate by sending and receiving messages asynchronously. This means that the sender does not wait for the receiver to be ready; instead, it sends the message to the receiver's mailbox, where it can be processed when the receiver is ready.

3. **Concurrency**: Actors run concurrently, and they can be distributed across multiple processors or machines. This allows for scalability and parallelism, as different parts of the dataflow graph can be processed simultaneously.

4. **Dataflow Graph**: The overall computation is represented as a graph where actors are the nodes, and the edges represent the potential paths for data to flow between actors. Each actor can have multiple input and output channels, allowing for complex dataflow topologies.

5. **No Shared State**: Actors do not share state with each other, which eliminates the need for locks or other synchronization mechanisms. Instead, all dependencies and data transfers are handled through message passing.

6. **Reactive Computation**: Actors react to the messages they receive. A computation step is triggered by the arrival of a new message, making the system reactive and event-driven.

7. **Fault Tolerance**: The actor model inherently supports fault tolerance. If an actor fails, it can be restarted or replaced without affecting the rest of the system, as long as the message-passing infrastructure remains intact.

8. **Backpressure and Flow Control**: Since actors process messages asynchronously, there needs to be a mechanism to handle situations where producers send messages faster than consumers can process them. This is often handled through backpressure, where consumers can signal producers to slow down, or through buffering strategies.

Actor-based dataflow systems are used in various domains, such as real-time analytics, distributed computing, and complex event processing. They provide a flexible and scalable way to structure applications that need to process large volumes of data or that require high levels of concurrency.

Popular frameworks and languages that implement actor-based dataflow concepts include Akka (for Scala and Java), Erlang, and Microsoft's TPL Dataflow library for .NET. Each of these provides tools and abstractions to build scalable, concurrent, and fault-tolerant systems based on the principles of actor-based dataflow.