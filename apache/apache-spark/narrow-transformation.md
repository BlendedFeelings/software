---
b: https://blendedfeelings.com/software/apache/apache-spark/narrow-transformation.md
---

# Narrow transformations in Apache Spark
are those where each input partition will contribute to only one output partition. This means that the data required to compute the records in a single partition reside in at most one partition of the parent RDD. Because of this, narrow transformations do not require data to be shuffled across the partitions/network. They are more efficient as they can be done locally within a single partition.

Here are some examples of narrow transformations:

1. `map(func)`: Applies a function to each element in the RDD and returns a new RDD.
2. `filter(func)`: Returns a new RDD containing only the elements that satisfy a predicate.
3. `flatMap(func)`: Similar to map, but each input item can be mapped to 0 or more output items.
4. `mapPartitions(func)`: Similar to map, but runs separately on each partition (block) of the RDD.
5. `mapPartitionsWithIndex(func)`: Similar to mapPartitions, but also provides a function with an index of the partition.
6. `sample(withReplacement, fraction, seed)`: Sample a fraction of the data, with or without replacement.
7. `union(otherDataset)`: Returns a new dataset that contains the union of the elements in the source dataset and the argument.
8. `takeSample(withReplacement, num, seed)`: Returns an array with a random sample of num elements of the dataset, with or without replacement.

Since narrow transformations do not involve the shuffling of data, they are generally faster and less costly in terms of performance. They can be used to perform operations that do not require data from other partitions, such as filtering or mapping.

In contrast, wide transformations require the data to be shuffled. For example, operations like `groupBy`, `reduceByKey`, and `join` are wide transformations because they require data from multiple partitions to be aggregated or combined.