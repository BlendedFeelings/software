---
b: https://blendedfeelings.com/software/apache/apache-spark/checkpointing.md
---

# Checkpointing in Apache Spark 
is a process that saves the state of a computation (RDD, DataFrame, or Dataset) to a reliable storage system (like HDFS or S3) to prevent data loss and to allow for recovery in case of failures. It is particularly useful for long-running computations and for applications that require fault tolerance.

Here's how checkpointing works in Spark:

1. **Enabling Checkpointing**: Before you can checkpoint an RDD or a DataFrame, you need to specify a directory where Spark will save the checkpoint data. This is done using the `SparkContext` or `SparkSession`.

    ```scala
    sc.setCheckpointDir("hdfs://path/to/checkpoint-dir")
    ```

2. **Checkpointing an RDD**: To checkpoint an RDD, you simply call the `checkpoint` method on it. Spark will perform the checkpointing operation asynchronously. It is often a good practice to call an action (like `count`) after checkpointing to force the checkpointing to occur immediately.

    ```scala
    val rdd = sc.parallelize(1 to 100)
    rdd.checkpoint()
    rdd.count()  // Force checkpointing
    ```

3. **Checkpointing a DataFrame or Dataset**: For DataFrames or Datasets, the process is similar but uses the `DataFrameWriter` or `DatasetWriter` API.

    ```scala
    val df = sparkSession.read.json("path/to/json/file")
    df.write.checkpoint("hdfs://path/to/checkpoint-dir")
    ```

4. **Reliability**: Checkpointing saves the entire lineage of the RDD or DataFrame to a reliable storage system, which means that if a part of the computation is lost due to a node failure, Spark can recover it using the checkpointed data.

5. **Lineage Truncation**: Checkpointing also truncates the lineage of the RDD or DataFrame. Spark computations are built upon a lineage graph that can get very long over time. By checkpointing, you cut down the lineage and start a new graph from the checkpointed data, which can help in optimizing the performance of your application.

6. **Local vs Distributed Checkpointing**: Spark also provides local checkpointing, which stores the checkpointed data in the executors' local storage instead of a distributed file system. This is faster but less reliable than distributed checkpointing.

    ```scala
    rdd.localCheckpoint()
    rdd.count()  // Force local checkpointing
    ```

Checkpointing is a powerful feature that should be used judiciously, as it involves I/O operations that can be expensive. It is recommended to use it when the computation graph is long or when dealing with iterative algorithms like machine learning training.