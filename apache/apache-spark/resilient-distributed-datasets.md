---
b: https://blendedfeelings.com/software/apache/apache-spark/resilient-distributed-datasets.md
---

# Resilient Distributed Datasets (RDDs) 
are the fundamental data structure of Apache Spark, which makes it unique compared to other data processing frameworks. They are an immutable distributed collection of objects that can be processed in parallel. RDDs are fault-tolerant, meaning they can automatically recover from node failures.

Here are some key characteristics of RDDs:

1. **Immutability**: Once created, the data in an RDD cannot be changed. This immutability is a key feature for achieving consistency and fault tolerance. You can transform an RDD into a new RDD using transformations, but the original RDD remains unchanged.

2. **Resilience**: RDDs achieve fault tolerance through lineage. If any partition of an RDD is lost due to a node failure, Spark can recompute the lost partition data using the original transformations. This ability to rebuild lost data using lineage information ensures that Spark can handle failures without data loss.

3. **Parallel Processing**: RDDs are distributed across a cluster, and Spark runs processing tasks on the cluster in parallel. This allows for efficient data processing on a large scale.

4. **Laziness**: RDD operations are lazy, meaning that no computation is performed until an action is called. Transformations on RDDs create a new RDD and define a lineage, but they do not compute the transformed RDD immediately. Instead, Spark remembers the set of transformations applied to some base dataset. The transformed RDDs are computed only when an action is called to return a final value to the Spark program or to write data to storage.

5. **Partitioning**: Data in RDDs is divided into partitions, which can be processed in parallel across different nodes of a Spark cluster. The way data is partitioned can be customized to optimize for data locality or to balance the workload among nodes.

6. **Caching and Persistence**: Users can explicitly persist an RDD in memory or on disk, allowing it to be reused efficiently across parallel operations. This is particularly useful for iterative algorithms that need to work on the same dataset multiple times.

7. **Wide Array of Operations**: RDDs support two types of operations: transformations, which create a new RDD from an existing one, and actions, which return a value to the driver program after running a computation on the dataset.

Here's an example of how you might create and work with an RDD in Spark using Python (PySpark):

```python
from pyspark import SparkContext

# Initialize a SparkContext
sc = SparkContext("local", "RDD example")

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Apply a transformation to the RDD (this is lazy and not computed yet)
squared_rdd = rdd.map(lambda x: x * x)

# Perform an action to compute the result and bring it to the driver
squared_data = squared_rdd.collect()

print(squared_data)  # Output: [1, 4, 9, 16, 25]
```

In the example above, `sc.parallelize(data)` creates an RDD, `rdd.map(lambda x: x * x)` applies a transformation, and `squared_rdd.collect()` performs an action that triggers the computation and returns the result to the driver program.