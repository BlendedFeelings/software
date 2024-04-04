---
b: https://blendedfeelings.com/software/apache/apache-spark/application-execution.md
---

# Execution of a Spark application 
involves several components and steps that work together to process large data sets in a distributed manner. Below are the detailed steps that occur from the moment you submit a Spark application until it completes execution:

1. **Write the Application**:
   - Developers write a Spark application using Spark APIs in one of the supported programming languages (Scala, Java, Python, or R). The application defines a series of transformations and actions to be applied to distributed data.

2. **SparkSession**:
   - The application creates a `SparkSession`, which is the entry point to programming Spark with the Dataset and DataFrame API. For backward compatibility, `SparkContext` is also used, especially in older applications or those using the RDD API.

3. **Submit Application**:
   - The application is submitted to a cluster using the `spark-submit` script, which sets up the execution environment and configures the application. The script specifies various parameters, such as the main class, application JARs, and any additional libraries required.

4. **Start Driver Program**:
   - The driver program begins execution on a cluster node designated as the master node. The driver is responsible for converting the user's application into tasks and scheduling them to run on executors.

5. **Request Resources**:
   - The driver program contacts the cluster manager (Standalone, YARN, Mesos, or Kubernetes) to request resources for executors. The cluster manager allocates nodes for the application's executors.

6. **Launch Executors**:
   - Executors are launched on the worker nodes allocated by the cluster manager. Executors are JVM processes that run computations and store data for the application.

7. **Task Scheduling**:
   - The driver program converts the application code into a directed acyclic graph (DAG) of stages. Each stage represents a set of tasks that can be executed in parallel.
   - The DAGScheduler in the driver program splits the graph into stages and pipelines tasks within each stage. The TaskScheduler then queues these tasks for execution on the executors.

8. **Task Execution**:
   - Executors receive tasks from the driver and run them. If tasks require data from previous stages, executors will fetch that data across the network from other executors (or read from disk if cached).

9. **Shuffle Operations**:
   - For operations that involve grouping or sorting data (like `reduceByKey` or `groupBy`), Spark performs shuffle operations. This involves redistributing data across different executors and possibly writing data to disk.

10. **Fault Tolerance**:
    - Spark provides fault tolerance through data lineage. If a partition of an RDD is lost, Spark can recompute it using the lineage information. For stages that involve shuffling, Spark persists shuffle data to allow for recomputation of only the lost data.

11. **Collect Results**:
    - Once all tasks are completed, the results are sent back to the driver program. Actions like `collect` will gather the results to the driver, while others like `saveAsTextFile` will write the output directly from executors to a distributed storage system (e.g., HDFS, S3).

12. **Stop Application**:
    - After all actions are completed, the `SparkSession` is stopped, and the driver program terminates. The cluster manager reclaims the resources used by the application's executors.

Throughout this process, Spark's web UI can be used to monitor the progress of the application, including the execution of stages and tasks, resource usage, and other important metrics. Spark's efficient execution model allows for fast processing of large data sets by exploiting in-memory computing and optimizing for data locality.