---
b: https://blendedfeelings.com/software/dataflow-programming/dataflow-process-network.md
---

# Dataflow Process Networks (DPN) 
are a model used in dataflow programming where the computation is modeled as a network of processes communicating via data passing. This model is particularly useful for parallel and distributed systems because it naturally allows for concurrent execution of independent processes.

Here's an overview of the key concepts and elements that make up Dataflow Process Networks:

1. **Nodes (Processes):** In a DPN, nodes represent the computational processes or tasks. Each node can execute independently and performs a specific function or operation on the data it receives.

2. **Edges (Channels):** The edges in the network represent the communication channels through which data tokens (packets of information) flow from one node to another. These channels can be thought of as FIFO (First In, First Out) queues that connect the output of one node to the input of another.

3. **Tokens (Data Packets):** The data that flows through the edges are called tokens. A token is a packet of information that a process consumes and produces. The movement of tokens through the network drives the computation.

4. **Firing Rules:** Each node in a DPN has a set of firing rules that determine when the process can execute. A process typically fires (executes) when it has sufficient data tokens available on its input channels.

5. **Determinacy:** Despite the inherent parallelism and the nondeterministic order of execution, DPNs are designed to be determinate. This means that for a given set of inputs, the network will always produce the same set of outputs, regardless of the order in which nodes are executed.

6. **Buffers:** Channels may have buffers to store tokens when a process is not ready to consume them. The size of these buffers can affect the performance and behavior of the network.

7. **Scheduling:** DPNs require a scheduler to manage the execution of processes. The scheduler decides which process to fire next based on the availability of data and the firing rules.

8. **Deadlock:** Deadlock is a potential problem in DPNs if processes get stuck waiting for each other in a cycle. Careful design or dynamic scheduling strategies are needed to prevent or resolve deadlocks.

Dataflow Process Networks are used in various applications, including signal processing, multimedia processing, and scientific computing, where tasks can be decomposed into independent units of work that communicate through well-defined channels. DPNs are also a foundational model for many modern stream processing systems and parallel computing frameworks.