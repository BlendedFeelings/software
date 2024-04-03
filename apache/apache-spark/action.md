---
b: https://blendedfeelings.com/software/apache/apache-spark/action.md
---

# Actions in Apache Spark 
are operations that trigger the execution of the computation graph that has been built up through transformations. Unlike transformations, which are lazy and build up a lineage of operations to be performed, actions force the execution of those transformations and return a result to the driver program or write it to storage. Actions are the means by which Spark initiates computation across the cluster.

Here are some common actions in Spark:

1. `collect()`: Returns all the elements of the RDD as an array to the driver program. This can be a very costly operation if the RDD is large, as it pulls all the data into the driver's memory.

2. `count()`: Returns the number of elements in the RDD.

3. `take(n)`: Returns an array with the first n elements of the RDD. It is a potentially cheaper alternative to `collect()` when you only need a few elements.

4. `first()`: Returns the first element of the RDD, which is equivalent to `take(1).head`.

5. `reduce(func)`: Aggregates the elements of the RDD using a function `func` (which takes two arguments and returns one). The function should be commutative and associative so that it can be computed correctly in parallel.

6. `foreach(func)`: Applies a function to each element of the RDD, but unlike `map`, it returns nothing -- it's an action, not a transformation.

7. `saveAsTextFile(path)`: Writes the elements of the RDD to a text file (or set of text files) in a specified directory in the local filesystem, HDFS, or any other Hadoop-supported file system.

8. `saveAsSequenceFile(path)`: (For RDDs of key-value pairs) Writes the elements of the RDD to a Hadoop SequenceFile in the specified path.

9. `countByKey()`: (For RDDs of key-value pairs) Returns the count of each unique key.

10. `foreachPartition(func)`: Similar to `foreach`, but it runs separately on each partition (block) of the RDD.

11. `aggregate(zeroValue)(seqOp, combOp)`: Aggregates the elements of each partition and then the results for all the partitions using given combine functions and a neutral "zero value".

12. `saveAsObjectFile(path)`: Serializes RDD elements and saves them as an object file.

Actions are what trigger the execution of the Spark job, and the results are either collected to the driver or written to the output data store. It's important to choose actions wisely to avoid unnecessary computation and to prevent running out of memory on the driver node.