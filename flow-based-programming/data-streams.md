---
b: https://blendedfeelings.com/software/flow-based-programming/data-streams.md
---

# Data streams 
are handled by encapsulating data into Information Packets (IPs) that are asynchronously passed between concurrently running, modular components through defined connections with support for buffering and back-pressure.

Here's how data streams are handled in FBP:

1. **Information Packets (IPs)**: In FBP, the data that flows between components is encapsulated in chunks called Information Packets. These are the basic units of data that are transmitted through the network.

2. **Ports**: Each component has defined input and output ports. Data streams are sent and received through these ports. Input ports accept incoming IPs, and output ports send IPs to the next component in the network.

3. **Connections**: Components are connected by streams, which are made up of a series of IPs. These connections define the path that data takes through the network. The connections are usually unidirectional, meaning data flows from an output port of one component to an input port of another.

4. **Buffers**: Data streams are often buffered in FBP, which means that a queue is used to store IPs at the connection points between components. The buffer allows components to work at different rates; a fast producer can continue to work without waiting for a slower consumer.

5. **Asynchronous Processing**: Components process IPs asynchronously. Each component operates independently and concurrently, which means they do not have to wait for other components to finish processing. This allows for parallel processing and can lead to performance improvements in data handling.

6. **Back-Pressure**: FBP naturally supports back-pressure, which is a way to handle situations where a component cannot process incoming data fast enough. If a buffer is full, the producing component can be signaled to slow down or stop producing data until the consuming component has processed some of the buffered IPs.

7. **Transactions**: Some FBP systems support transactions, allowing for groups of IPs to be treated as a single unit of work. This can help ensure data consistency and manage complex data processing scenarios.

8. **Reusability and Modularity**: Since components are designed to be black boxes with specific inputs and outputs, they can be reused across different FBP networks. This modularity makes it easy to handle data streams in a consistent and scalable way.

FBP provides a high level of abstraction for data stream processing, making it a powerful tool for building complex, scalable, and maintainable systems. The visual nature of FBP also makes it easier to understand the flow of data through the application, which can be beneficial for designing and debugging.