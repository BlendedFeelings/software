---
b: https://blendedfeelings.com/software/dataflow-programming/firing-rules.md
---

# Firing Rules in Dataflow programming 
are the conditions that dictate when a node within the dataflow network is ready to execute its operation. These rules ensure that the computations within the nodes are carried out in the correct order and with the right data. The execution of a node is commonly referred to as "firing," and it happens when the firing rules associated with that node are satisfied. Some of the key firing rules include:

Here are the common firing rules in dataflow programming:

1. **Availability of Data**: A node can fire when all necessary input data is available on its incoming edges. This is the most basic rule and ensures that a node has all the information it needs to perform its computation.

2. **Token Matching**: In some dataflow models, nodes may require a matching set of tokens (data items) on all input channels to fire. This ensures that the data being processed is synchronized across different inputs.

3. **Sufficient Resources**: A node may only fire if there are sufficient system resources (such as memory or CPU time) available to handle the computation.

4. **Priority and Scheduling**: If multiple nodes are ready to fire, a scheduling algorithm or priority system may determine the order in which they execute.

5. **Non-determinism**: In some dataflow systems, the firing of nodes may be non-deterministic, meaning that if multiple nodes are ready to fire, any one of them could fire next, and the choice is not predetermined.

6. **Initialization**: Some nodes may have an initialization condition that must be met before they can begin firing, such as the presence of initial configuration data.

7. **Quiescence**: A node might have a quiescence condition where it will not fire until all other nodes have stopped firing, which can be useful for nodes that perform finalization or aggregation operations.

8. **Threshold**: A node might fire once the amount of data on its inputs reaches a certain threshold, rather than waiting for all inputs to be filled.

9. **Rate Control**: In some systems, nodes may have firing rules based on timing or rate control, where they only fire at certain intervals or when a timing condition is met.