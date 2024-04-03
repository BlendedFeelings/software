---
b: https://blendedfeelings.com/software/design/pipes-and-filters-pattern.md
---

# Pipes and Filters pattern 
is a design pattern that provides a structure for systems that process a stream of data. Each processing step is encapsulated in a filter component; data passes through pipes between adjacent filters. Recombining filters allows developers to build families of related systems.

Here are the key concepts of the Pipes and Filters pattern:

1. **Filters**: These are the processing units that perform some operation on the data. Each filter has a set of inputs and outputs. A filter reads streams of data on its inputs and produces streams of data on its outputs. This processing can be anything from simple transformations, such as converting data from one format to another, to complex operations like image recognition or data compression.

2. **Pipes**: Pipes are the connectors that pass data from one filter to the next. They are the conduits for the data streams. In a software context, a pipe can be a data buffer, a network connection, or a simple variable.

3. **Data**: This is the information that flows through the pipes and is processed by the filters. It can take various forms, such as a stream of bytes, structured objects, or messages.

4. **Reusability and Composability**: Because filters perform specific, well-defined tasks, they can be reused in different contexts. Similarly, because the pattern defines strict interfaces for pipes, different filters can be composed to create new processing pipelines without much effort.

5. **Concurrency**: Since each filter can potentially operate independently of the others, the Pipes and Filters architecture naturally lends itself to concurrent execution. Filters can process data in parallel, improving performance on multi-core or distributed systems.

6. **Ease of Understanding and Maintenance**: The separation of concerns in this pattern makes it easier to understand and maintain the system. Each filter can be developed and tested independently, reducing complexity.

7. **Flexibility**: New filters can be added to existing pipelines, and existing filters can be replaced or removed without affecting the rest of the system. This makes the architecture highly adaptable to changing requirements.

Here's a simple example to illustrate the concept:

```plaintext
[Raw Data] --> |Filter A: Clean Data| --> |Filter B: Transform Data| --> |Filter C: Aggregate Data| --> [Processed Data]
```

In this example:
- Filter A might remove invalid entries from a dataset.
- Filter B might convert the cleaned data into a different format or apply some computation.
- Filter C might summarise the transformed data, for example, by calculating averages or totals.

The Pipes and Filters pattern is widely used in various domains such as data processing pipelines, compilers, and network protocols. It is particularly prevalent in systems where data processing can be decomposed into discrete, sequential stages.