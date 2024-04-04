---
b: https://blendedfeelings.com/software/apache/apache-spark/dag.md
---

# DAG (Directed Acyclic Graph) in Apache Spark
is a conceptual representation of the sequence of operations applied to the data to form the final result. It is a graph with nodes and directed edges where each node represents an RDD (Resilient Distributed Dataset) and each edge represents an operation that will transform one RDD into another. The DAG abstraction helps Spark optimize the execution of operations by allowing it to see the entire flow of the computation.

When you write Spark code using its transformations and actions, you are building up a lineage for the RDDs. The lineage graph, which is a DAG, keeps track of all the transformations applied to the RDDs and the dependencies between them. This information is used by Spark to compute each RDD on demand and to recover lost data if part of the computation is lost.

Here's a simple example of how a Spark DAG might look:

1. **Read data**: Start with a source dataset, which becomes the initial RDD.
2. **Transformation 1**: Apply a `map` operation to transform the data (e.g., parsing each line of text into a more structured format). This creates a new RDD.
3. **Transformation 2**: Apply a `filter` operation to remove unwanted records. This creates another new RDD.
4. **Transformation 3**: Use a `groupBy` operation to group data by a key. Yet another RDD is created.
5. **Action**: Finally, an action like `collect` or `count` triggers the execution of the DAG. 

Spark's lazy evaluation means that transformations are not executed immediately when they are defined. Instead, they are recorded in the DAG. The DAG is executed only when an action is called. This allows Spark to optimize the execution plan. For example, it can combine certain transformations into a single stage to minimize data shuffling across the cluster.

The DAG Scheduler is the component of Spark that translates the RDD transformations into stages of tasks. A stage comprises tasks based on partitions of the input data. The DAG Scheduler pipelines operators together. For instance, if you have a sequence of `map` operations, Spark will group them into a single stage. The DAG Scheduler also determines the preferred locations to run each task based on the location of the input data.

During execution, the DAG Scheduler submits stages to the Task Scheduler, which launches tasks via cluster managers like YARN, Mesos, or the standalone scheduler. The Task Scheduler doesn't know about dependencies between stages; it just launches tasks. The DAG Scheduler is responsible for tracking the progress of stages and handling failures by resubmitting stages.

Understanding the DAG and how Spark executes it can be crucial for optimizing Spark jobs, as it can help identify performance bottlenecks and opportunities for optimization.