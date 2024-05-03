---
b: https://blendedfeelings.com/software/flow-based-programming/communication.md
---

# Components
also known as "processes" or "nodes," communicate with each other through predefined connections using a concept called "information packets" (IPs). The communication model in FBP is based on streams of data that flow through the network of components. Here's how the communication typically works:

1. **Ports**: Each component has defined input and output ports. These ports are the interfaces through which components receive and send IPs.

2. **Information Packets (IPs)**: IPs are the data units that flow through the network. They can contain various types of data, such as strings, numbers, objects, or more complex data structures.

3. **Connections**: The components are connected to each other by "connections" or "channels" that link the output ports of one component to the input ports of another. These connections define the flow of IPs in the network.

4. **Sending IPs**: When a component has processed its input data and produced an output, it sends this output as IPs through its output ports to the next connected component(s).

5. **Receiving IPs**: Components wait for IPs to arrive at their input ports. Once an IP is received, the component processes it according to its internal logic. This could involve transforming the data, combining it with other data, performing calculations, etc.

6. **Asynchronous Processing**: Components operate concurrently and asynchronously. They do not need to wait for other components to complete their processing. This allows for a high degree of parallelism and can lead to more efficient processing of data streams.

7. **Back-Pressure**: In some FBP systems, a mechanism known as "back-pressure" can be implemented to prevent a component from being overwhelmed by incoming IPs. If a component cannot process IPs quickly enough, it signals upstream components to slow down the production of IPs.

8. **Bounding Buffers**: Connections often have bounded buffers, which means they can hold a limited number of IPs at a time. If a buffer is full, the producing component must wait until there is space available before sending more IPs.

9. **Lifecycle of IPs**: IPs have a lifecycle; they are created, sent, received, and eventually destroyed or recycled after processing is complete.

10. **Network Definition**: The communication structure between components is typically defined in a separate configuration or network definition, which specifies the components, ports, and connections that make up the application.

FBP's communication model emphasizes loose coupling between components, high cohesion within components, and a focus on the flow of data. This makes it a useful paradigm for building complex, scalable, and maintainable systems, especially when dealing with stream processing or data-driven applications.