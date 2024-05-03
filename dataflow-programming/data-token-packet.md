---
b: https://blendedfeelings.com/software/dataflow-programming/data-token-packet.md
---

# Data tokens/packets in Dataflow programming 
are the individual units of data that traverse the network of nodes, acting as the inputs and outputs of computational processes. These tokens are analogous to messages that carry information from one node to another, enabling the nodes to perform their designated operations when they have received the necessary data. Each data token is self-contained and includes all the information a node needs to execute its function or to be further processed by subsequent nodes in the dataflow graph.

Here's an overview of how they work:

1. **Data Tokens/Packets**: These are the individual pieces of data that are transmitted between nodes in the dataflow network. Each token represents a piece of information, such as a number, string, object, or more complex data structures.

2. **Nodes/Processes**: The nodes (also called processes or actors) are the functional units that receive data tokens, perform operations on them, and then output the results as new data tokens. Each node can be thought of as a black box that executes a specific task.

3. **Edges/Connections**: The edges or connections between nodes represent the paths that data tokens take through the network. They define the data dependencies between nodes, ensuring that a node receives all the necessary inputs before it begins execution.

4. **Firing Rules**: Nodes in a dataflow network have firing rules that determine when they should execute. A common rule is that a node fires (executes) whenever all its input ports have received data tokens. After firing, the node processes the input data and sends output data tokens to the next nodes in the network.

5. **Concurrency**: Since the execution of nodes is driven by the availability of data, dataflow programming naturally lends itself to parallel and concurrent execution. Different nodes can process data tokens simultaneously if they are not dependent on each other, leading to potentially significant performance gains on multi-core or distributed systems.

6. **Deterministic Results**: In pure dataflow programming, the results of computation are deterministic. Given the same set of input data tokens, the network will always produce the same output, regardless of the order in which nodes execute.

7. **Buffering**: Nodes are often connected by buffers that store data tokens. Buffers allow for asynchronous communication between nodes, where a producer node can continue to produce data tokens without waiting for the consumer node to process them.

Dataflow programming is particularly well-suited for applications that can be represented as a series of operations on data streams, such as signal processing, financial data analysis, and more. It is also the basis for many visual programming languages and is used in various domains, including concurrent computing, reactive programming, and complex event processing.