---
b: https://blendedfeelings.com/software/apache/apache-spark/persistence.md
---

# Persistence (or caching) in Apache Spark 
is a mechanism for keeping the intermediate results of a computation in memory or on disk after the first computation, so they can be reused in subsequent actions without having to recompute them. This can significantly improve the performance of your Spark jobs, especially when you have iterative algorithms or when you need to access the same data multiple times.

Spark provides several storage levels for persisting RDDs, DataFrames, and Datasets. Here's a brief overview of the persistence options:

1. `MEMORY_ONLY`: Stores the RDD as deserialized Java objects in the JVM. If the RDD does not fit in memory, some partitions will not be cached and will be recomputed on the fly as needed. This is the default level.

2. `MEMORY_AND_DISK`: Stores the RDD as deserialized Java objects in the JVM. If the RDD does not fit in memory, the partitions that do not fit will be stored on disk, and read from there when needed.

3. `MEMORY_ONLY_SER`: Stores the RDD as serialized Java objects (one byte array per partition). This is more space-efficient than `MEMORY_ONLY` but more CPU-intensive due to serialization.

4. `MEMORY_AND_DISK_SER`: Similar to `MEMORY_ONLY_SER`, but it will store partitions that do not fit in memory to disk instead of recomputing them on the fly.

5. `DISK_ONLY`: Stores the RDD partitions only on disk.

6. `MEMORY_ONLY_2`, `MEMORY_AND_DISK_2`, etc.: Same as the above levels, but replicate each partition on two cluster nodes.

7. `OFF_HEAP`: Stores the RDD in serialized format in an off-heap storage. This requires that you have off-heap memory configured.

To persist an RDD, DataFrame, or Dataset in Spark, you use the `persist()` method, optionally passing in the desired storage level. If you do not specify a storage level, the default is `MEMORY_ONLY`. You can also use `cache()` as a shorthand for `persist()` with the default storage level.

Here's an example of how you might persist an RDD in Scala:

```scala
val rdd = sc.parallelize(1 to 100)
rdd.persist(StorageLevel.MEMORY_AND_DISK)
```

And for a DataFrame or Dataset in Scala:

```scala
val df = spark.read.json("path/to/json/file")
df.persist(StorageLevel.MEMORY_AND_DISK)
```

Remember that you should unpersist data when it is no longer needed to free up memory or disk space. You can do this with the `unpersist()` method.

```scala
rdd.unpersist()
df.unpersist()
```

Persistence is a powerful feature in Spark that can improve the performance of your applications, but it should be used judiciously. Persisting data unnecessarily can consume a lot of memory and potentially lead to out-of-memory errors. It's important to persist only the data that will be reused and to unpersist data when it's no longer needed.