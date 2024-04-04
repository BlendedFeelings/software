---
b: https://blendedfeelings.com/software/apache/apache-spark/lazy-evaluation.md
---

# Lazy evaluation in Apache Spark 
refers to the computation process where the execution of operations is delayed until it is absolutely necessary. This is a key feature of Spark that contributes to its efficiency, particularly when processing very large datasets in distributed computing environments.

Here are some key points about lazy evaluation in Spark:

1. **Transformation and Action**: Spark operations can be categorized into two types: transformations and actions. Transformations create new RDDs (Resilient Distributed Datasets) from existing ones, but they do not compute their results right away. Instead, they are lazily evaluated. Actions, on the other hand, trigger the computation to produce results or side-effects.

2. **Lineage Graph**: When transformations are applied to RDDs, Spark maintains a lineage graph (also known as a DAG, Directed Acyclic Graph) that records how the new RDD is derived from the parent RDDs. This graph is used to compute the RDDs later when an action is called.

3. **Optimization**: Lazy evaluation allows Spark to optimize the execution plan. Since Spark knows the entire sequence of transformations before executing an action, it can organize and combine operations to optimize data processing. For example, it can merge multiple transformations into a single stage to reduce the number of passes over the data.

4. **Fault Tolerance**: The lineage graph also enables fault tolerance. If a partition of an RDD is lost due to a node failure, Spark can use the lineage information to rebuild just that partition rather than recomputing the entire RDD.

5. **Efficient Resource Usage**: By delaying computation until necessary, Spark can minimize the use of memory and other resources. It does not need to store intermediate results unless they are explicitly cached or persisted.

6. **Debugging**: While lazy evaluation has many benefits, it can make debugging more challenging because errors are not thrown when transformations are defined, but rather when an action is executed.

An example of lazy evaluation in Spark can be illustrated with the following sequence of transformations and an action:

```python
rdd = sparkContext.textFile("data.txt")  # Read data (lazy)
rdd = rdd.filter(lambda x: "error" in x)  # Filter transformation (lazy)
rdd = rdd.map(lambda x: x.split())        # Map transformation (lazy)
count = rdd.count()                       # Count action (triggers execution)
```

In this example, the `textFile`, `filter`, and `map` operations are transformations that define a lineage of RDDs, but they do not trigger any computation. Only when the `count` action is called does Spark actually execute the operations to compute the result.