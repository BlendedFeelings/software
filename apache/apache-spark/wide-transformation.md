---
b: https://blendedfeelings.com/software/apache/apache-spark/wide-transformation.md
---

# Wide transformations in Apache Spark 
are operations that produce RDDs with dependencies on data from multiple partitions of the parent RDD. These dependencies often involve shuffling data across different executors and even different nodes, which can be quite expensive in terms of network I/O and can lead to increased computation time.

Here are some common wide transformations:

1. `groupBy(func)`: Groups the elements of an RDD according to a specified function and returns an RDD of grouped items.
2. `reduceByKey(func)`: When called on an RDD of (K, V) pairs, this operation returns a new RDD of (K, V) pairs where the values for each key are aggregated using the given reduce function.
3. `join(otherDataset)`: When called on RDDs of type (K, V) and (K, W), returns an RDD of (K, (V, W)) pairs with all pairs of elements for each key.
4. `cogroup(otherDataset)`: When called on datasets of type (K, V) and (K, W), groups data from both datasets together by key.
5. `distinct()`: Returns a new RDD containing distinct elements from the source RDD.
6. `sortByKey()`: When called on an RDD of (K, V) pairs where K implements Ordered, returns an RDD sorted by the keys.
7. `repartition(numPartitions)`: Reshuffles the data in the RDD randomly to create either more or fewer partitions and balance it across them. This always involves a shuffle, even if the number of partitions is not changed.
8. `repartitionAndSortWithinPartitions(partitioner)`: Repartitions the RDD according to the given partitioner and, within each resulting partition, sorts records by their keys.

Wide transformations are often used for aggregating data, joining datasets, or any other operations that require data interaction between different partitions. Due to the shuffle operation, they are generally more costly than narrow transformations. Optimizing the use of wide transformations can significantly improve the performance of a Spark application.