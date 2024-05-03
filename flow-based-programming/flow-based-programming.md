---
b: https://blendedfeelings.com/software/flow-based-programming/flow-based-programming.md
---

# Flow-based programming (FBP) 
is a programming paradigm that defines applications as networks of "black box" processes, which exchange data across predefined connections by message passing. These processes, which can be referred to as nodes, components, actors, or filters, are encapsulated and can be reused. FBP is often used for data processing, and it can be particularly effective for parallel and distributed systems.

Here are some key concepts in flow-based programming:

1. **Components (Processes):** These are the building blocks of an FBP application. Each component is designed to execute a specific task and can operate independently of the others. Components have input and output ports for receiving and sending data.

2. **Connections (Edges):** These define the pathways for data to flow between components. Data is passed in the form of messages or packets, which can be thought of as discrete pieces of information.

3. **Network (Graph):** The overall design of an FBP application is represented as a network or graph, where nodes represent the components and edges represent the connections between them.

4. **Information Packets (IPs):** These are the units of data that are transmitted between components through connections. IPs are ideally immutable, which means that once they are created, their state does not change.

5. **Ports:** Each component has defined input and output ports. Input ports receive IPs, and output ports send them out. Ports ensure a clear interface for components and help maintain loose coupling.

6. **Encapsulation:** Components encapsulate functionality and hide their internal workings from the rest of the network. This promotes reusability and modularity.

7. **Asynchronous Processing:** Components can process data asynchronously, which allows for concurrent execution and can lead to more efficient use of system resources.

8. **Backpressure:** This is a mechanism to prevent components from being overwhelmed by incoming data. If a component cannot process IPs quickly enough, backpressure can signal upstream components to slow down data production.

FBP is similar in some respects to the actor model, but it focuses more on the data and its movement through the system, rather than on the computation entities themselves. FBP can be implemented in various programming languages, and there are specific FBP languages and frameworks that facilitate building applications in this paradigm.

Some popular FBP frameworks and tools include:

- **NoFlo:** A JavaScript framework for FBP that runs on both Node.js and the browser.
- **Apache NiFi:** A dataflow system based on the concepts of FBP, designed to automate the flow of data between systems.
- **Luna (now Enso):** A visual and textual functional programming language that incorporates FBP concepts.

FBP can be particularly useful in scenarios where the processing of data streams is complex and needs to be broken down into manageable, reusable components. It is also well-suited for systems that require high levels of scalability and maintainability.