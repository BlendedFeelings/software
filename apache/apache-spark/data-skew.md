---
b: https://blendedfeelings.com/software/apache/apache-spark/data-skew.md
---

# Data skew 
is a common issue in distributed computing environments, such as Apache Spark, where data is partitioned across multiple nodes. It refers to an uneven distribution of data across these partitions, which can lead to performance bottlenecks. When one or more partitions have significantly more data than others, tasks that process these larger partitions take longer to complete, resulting in an inefficient use of cluster resources and longer overall processing times.

Here are some strategies to handle data skew in Spark:

1. **Salting**: Add a random prefix to the key values, which distributes the data more evenly across partitions. After the shuffle operation, the salt can be removed or aggregated accordingly.

2. **Custom Partitioner**: Implement a custom partitioner that distributes the data more evenly across partitions based on the application's specific logic.

3. **Increasing Partition Count**: Increase the number of partitions using `repartition()` or `coalesce()` to spread out the skewed data over more partitions.

4. **Broadcast Join**: For skewed data during a join operation, if one of the datasets is small enough, use a broadcast join to send it to all nodes, avoiding shuffles.

5. **Filtering and Joining Separately**: If the skew is due to a few keys, filter out the skewed keys, perform join operations separately on the skewed and non-skewed data, and then union the results.

6. **Sampling and Scaling**: Use sampling to estimate the skewness and then scale up the smaller partitions to match the larger ones.

7. **Data Duplication**: Duplicate the keys that are causing the skew across multiple partitions, which can help in join operations.

8. **Adaptive Query Execution**: In Spark 3.0 and later, Adaptive Query Execution (AQE) can help mitigate skew by dynamically coalescing shuffle partitions and optimizing joins.

9. **Monitoring and Diagnostics**: Use Spark's UI to monitor the stages and tasks for signs of data skew. Tools like Spark's event log and history server can help diagnose issues.

Here is an example of how to apply salting to a DataFrame in Spark to mitigate skew:

```scala
val skewedDF = ... // your skewed DataFrame
val saltedDF = skewedDF
  .withColumn("salted_key", concat(col("key"), lit("_"), (rand() * 100).cast("int")))
  .repartition(col("salted_key"))

// Perform your operations on saltedDF, then remove the salt if necessary
val resultDF = saltedDF
  .groupBy("key")
  .agg(/* your aggregations */)
  .withColumn("key", expr("split(key, '_')[0]")) // remove the salt from the key
```

In this example, we add a random integer between 0 and 99 to the key column, which helps to distribute the data more evenly across partitions. After the operations are performed, the salt is removed from the key.

Remember that the strategies to handle data skew are highly dependent on the specific use case and data characteristics. It's essential to analyze the data and processing patterns to choose the most effective approach.