---
b: https://blendedfeelings.com/software/dataflow-programming/execution-models.md
---

# Execution Models in Dataflow programming 
is a concept that refers to the different ways in which a dataflow-oriented program can execute its operations based on the flow and transformation of data. These models are essential for understanding how a program will behave, how resources are managed, and how data is processed and passed between different operations. Each model provides a unique approach to execution, and the choice of model can significantly impact the performance, scalability, and responsiveness of a program. The models range from static structures with predetermined execution paths to dynamic and adaptive systems that can change during runtime, catering to a variety of application requirements and processing patterns.

Here are some common execution models in dataflow programming:

1. **Static Dataflow**: In static dataflow, the structure of the dataflow graph is determined at compile time. Each node in the graph represents an operation that fires (executes) whenever all of its input data are available. Once an operation fires, it consumes its input tokens and produces output tokens for downstream operations. This model is deterministic, meaning that for a given input, the output will always be the same.

2. **Dynamic Dataflow**: Unlike static dataflow, in dynamic dataflow, the structure of the graph can change during runtime. Operations can generate new operations or modify the connectivity of the graph. This allows for more flexibility and adaptability but can also make the behavior of the program more complex and less predictable.

3. **Demand-Driven Dataflow**: This model, also known as pull-based dataflow, is where operations request data from their upstream nodes as needed. This is in contrast to the push-based approach of static and dynamic dataflow, where data is pushed downstream as it becomes available. Demand-driven dataflow can be more efficient when not all data is needed to produce a result.

4. **Synchronous Dataflow (SDF)**: In SDF, the execution of nodes is determined by a fixed schedule based on the known rates of production and consumption of tokens on each edge of the graph. This allows for predictable and repeatable execution, which is beneficial for applications with real-time constraints.

5. **Dataflow Process Networks (DPN)**: DPNs generalize synchronous dataflow by allowing variable production and consumption rates. Nodes in a DPN can produce and consume different numbers of tokens each time they fire, which provides more flexibility but also requires more complex scheduling algorithms.

6. **Actor-Based Dataflow**: This model extends dataflow with the concept of actors, which are autonomous entities that encapsulate state and behavior. Actors communicate by sending messages (data tokens) to each other. Each actor processes messages independently, and the system's execution is driven by the availability of messages and the readiness of actors to process them.

7. **Stream Processing**: In stream processing, dataflow programming is applied to streams of data. Operations are applied to data in real-time as it flows through the system. This model is well-suited for applications that need to process continuous data sources, such as sensor data or financial transactions.

Each of these models has its own advantages and is suitable for different types of applications. The choice of model depends on factors such as the need for runtime flexibility, determinism, real-time constraints, and the nature of the data being processed.