---
b: https://blendedfeelings.com/software/dataflow-programming/dynamic-dataflow.md
---

# Dynamic dataflow in dataflow programming 
refers to the ability of a dataflow system to modify the structure of the dataflow graph during execution. Dataflow programming is a paradigm where the program is modeled as a directed graph of operations (nodes) and the data that flows between them (edges). Each node in the graph represents a computation, and nodes execute asynchronously when all their input data is available.

In a static dataflow graph, the structure of the graph is fixed and does not change during execution. However, in a dynamic dataflow graph, the following can happen:

1. **Nodes can be added or removed**: As the computation progresses, new computational nodes can be created, or existing ones can be removed from the graph.

2. **Edges can be added or removed**: Connections between nodes, which represent the paths along which data flows, can be altered. This means that the data dependencies can change as the program executes.

3. **Data packets can be rerouted**: The paths that data takes through the graph can be changed dynamically, allowing for different parts of the graph to be used for different data items.

4. **Feedback loops can be created or modified**: Dynamic dataflow allows for the creation of feedback loops where the output of a computation can be fed back as input to an earlier stage in the computation.

5. **Adaptive computation**: The graph can adapt to different data or conditions, allowing for more flexible and potentially more efficient computation.

Dynamic dataflow is particularly useful for applications that require runtime adaptability, such as signal processing, real-time systems, and interactive applications. It allows the program to respond to changes in the input data or external conditions by reconfiguring the computation graph on-the-fly.

Implementing dynamic dataflow requires a runtime system that can manage the changes to the graph while ensuring that the data dependencies are still met and that the computations are performed correctly. This adds complexity to the system but provides the flexibility needed for certain types of applications.