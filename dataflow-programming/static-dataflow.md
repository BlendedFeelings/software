---
b: https://blendedfeelings.com/software/dataflow-programming/static-dataflow.md
---

# Static dataflow in dataflow programming 
refers to a programming model where the structure of the dataflow graph is fixed and does not change at runtime. In this model, the nodes represent computation units, and the edges represent the data that flows between these nodes. Each node operates independently and processes data as it arrives, often in parallel with other nodes.

Key characteristics of static dataflow include:

1. **Fixed Structure**: The dataflow graph's topology is defined at compile-time and remains unchanged during execution. The number and types of nodes, as well as the connections between them, are predetermined.

2. **Deterministic Execution**: The behavior of the dataflow graph is predictable, as the flow of data through the static structure is consistent for the same inputs.

3. **Parallelism**: Since nodes operate independently, they can be executed in parallel, provided that the necessary data is available. This allows for efficient utilization of multi-core and distributed systems.

4. **Data-driven**: Computation is triggered by the availability of data rather than by explicit control flow constructs like loops or conditionals. Nodes wait passively for data to arrive on their input ports.

5. **Synchronous or Asynchronous**: Data can be processed synchronously, where nodes wait for all inputs to be ready before executing, or asynchronously, where nodes can start processing with partial inputs.

6. **Determinacy**: Despite parallel execution, a static dataflow program is deterministic if it always produces the same output for a given input, which is often the case in static dataflow systems.

Static dataflow is contrasted with dynamic dataflow, where the dataflow graph can change during execution, with nodes being added or removed as needed. Dynamic dataflow allows for more flexibility and adaptability, but it can also introduce complexity in terms of managing the changing topology and ensuring correct operation.

Static dataflow programming is often used in applications where the processing stages and data dependencies are well-understood and do not change, such as in digital signal processing, image processing, and certain scientific computing tasks. It is also a common model in hardware design, such as in Field Programmable Gate Arrays (FPGAs) and other parallel computing architectures.