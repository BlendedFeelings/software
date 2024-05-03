---
b: https://blendedfeelings.com/software/dataflow-programming/synchronous-dataflow.md
---

# Synchronous Dataflow (SDF) 
is a specific type of dataflow programming where the flow of data is synchronized across different nodes or processing elements. In dataflow programming, the program is represented as a directed graph, where nodes represent operations or computations, and edges represent the data that flows between these nodes.

In an SDF model, each node operates by firing (executing its operation) when a predetermined number of data tokens are available at its inputs. The number of tokens consumed and produced by each node is fixed and known in advance. This allows for the analysis of the system's behavior and the design of schedules that can execute the nodes without deadlock and with bounded memory.

Key characteristics of Synchronous Dataflow include:

1. **Deterministic Execution**: Since the number of tokens consumed and produced by each node is known, the execution is deterministic. This means that given the same set of input tokens, the SDF graph will always produce the same output.

2. **Static Scheduling**: The predictable nature of token consumption and production allows for static scheduling. A schedule can be computed at compile-time that dictates the order in which nodes should fire to ensure correct execution.

3. **Bounded Memory**: With knowledge of the token rates, it is possible to calculate the maximum buffer sizes required for the edges in the graph, ensuring that the system can operate with bounded memory.

4. **Parallel Execution**: If the SDF graph has independent subgraphs or nodes that do not depend on each other, these can potentially be executed in parallel, improving performance.

5. **Deadlock-Free**: Properly designed SDF graphs are deadlock-free as long as the static schedule is followed.

Synchronous Dataflow is particularly useful in the design of digital signal processing (DSP) systems, multimedia processing, and other domains where the rates of data production and consumption are regular and predictable. It simplifies the design and verification of such systems by providing a clear and analyzable model of computation.

However, SDF is less suitable for applications where the rates of data production and consumption are dynamic or unpredictable, as this would violate the basic assumptions of the SDF model. In such cases, other dataflow models, such as Dynamic Dataflow or Kahn Process Networks, might be more appropriate.