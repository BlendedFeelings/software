---
b: https://blendedfeelings.com/software/dataflow-programming/edge.md
---

# Edge in Dataflow programming 
is a connection between nodes that represents the pathway for data to travel from one node to another within the dataflow graph. It serves as a conduit through which data packets, containing the actual information being processed, are transmitted from the output of one node to the input of another.

Here's a brief overview of how edges function in dataflow programming:

1. **Data Transmission:** Edges are the conduits through which data packets move from one node to another. When a node completes a computation, it sends the result along the outgoing edges to the next nodes in the graph.

2. **Synchronization:** Edges can also be responsible for synchronizing the flow of data. In some dataflow models, a node will not execute until all its incoming edges have data available, ensuring that all required inputs are present before computation begins.

3. **Buffering:** Edges can include buffers to store data packets if the receiving node is not ready to process them. This can help in managing different processing speeds of nodes and allows for asynchronous computation.

4. **Typing:** Edges can be typed, meaning that they are designed to carry specific types of data. This ensures that the data being transmitted is compatible with the operations expecting to receive it.

5. **Control Signals:** Apart from data, edges can also carry control signals that may affect the flow of execution. For example, a control signal can indicate the end of a data stream or instruct a node to reset its state.

6. **Multiplicity:** An edge can connect one node to multiple nodes (broadcasting) or multiple nodes to one node (aggregation). This allows for patterns like fan-out and fan-in, which are common in parallel processing.

7. **Dynamic Reconfiguration:** In some advanced dataflow systems, edges can be reconfigured during runtime. This allows for dynamic graph topologies that can adapt to changing data or processing requirements.