---
b: https://blendedfeelings.com/software/dataflow-programming/demand-driven-dataflow.md
---

# Demand-Driven Dataflow
 also known as pull-based or lazy dataflow, is a paradigm within dataflow programming where the computation of values is deferred until those values are explicitly needed or requested. In contrast to push-based dataflow systems, where data is propagated through the network as soon as it becomes available, demand-driven systems wait for a consumer to request data before executing the computation that produces that data.

Here's an overview of how demand-driven dataflow works:

1. **Lazy Evaluation:** Computations are represented as dataflow nodes, but they are not evaluated immediately. Instead, they are evaluated when their output is required by another node downstream in the dataflow graph.

2. **Data Requests:** When a node needs data from a predecessor node, it sends a request upstream. This demand propagates backward through the network until it reaches the source nodes that have no dependencies.

3. **Computation Trigger:** Upon receiving a data request, a source node or a node with cached results will perform the necessary computation to generate the output.

4. **Data Propagation:** Once the computation is complete, the result is sent downstream to the requester. This can trigger further computations in other nodes that were waiting for this data.

5. **Memoization:** To optimize performance, nodes may cache their results. If the same data is requested again, the computation does not need to be repeated; the cached result is sent instead.

6. **Backpressure:** Since computations are only triggered by demand, the system naturally adapts to the consumer's processing capabilities. This can help prevent resource exhaustion and manage backpressure in the system.

Demand-driven dataflow is particularly useful in scenarios where not all outputs of a dataflow graph are needed, or when the cost of computing certain values is high and should be avoided unless necessary. It is commonly used in functional programming languages that support lazy evaluation, such as Haskell, and in various data processing systems and libraries.

Implementing demand-driven dataflow requires careful design to ensure that the system is responsive and efficient. It must handle cyclic dependencies and potential deadlocks that can arise when nodes are waiting on each other for data. Additionally, it should provide mechanisms for error handling and cancellation of computations if the requested data is no longer needed.