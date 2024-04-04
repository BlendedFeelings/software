---
b: https://blendedfeelings.com/software/apache/apache-spark/sparkcontext-sparksession.md
---

# SparkContext and SparkSession
are both entry points to Spark functionalities, but they serve different purposes and are used in different versions of Spark.

### SparkContext:
- **Introduced in:** Spark 1.x
- **Purpose:** It was the primary entry point for Spark functionality before Spark 2.0. It is responsible for connecting to the Spark cluster, creating RDDs, accumulators, and broadcast variables, and running jobs.
- **Usage:** To create a `SparkContext`, you need to first create a `SparkConf` object with the application configuration.

```scala
val conf = new SparkConf().setAppName("MyApp").setMaster("local")
val sc = new SparkContext(conf)
```

### SparkSession:
- **Introduced in:** Spark 2.0
- **Purpose:** It is a unified entry point for reading data, creating DataFrames and Datasets, and interacting with Spark SQL. It encompasses all the functionality of `SparkContext`, `SQLContext`, and `HiveContext` (if Hive support is enabled).
- **Usage:** `SparkSession` simplifies the user interface and is now the recommended way to interact with Spark functionalities.

```scala
val spark = SparkSession.builder()
  .appName("MyApp")
  .master("local")
  .getOrCreate()

// SparkContext is accessible through SparkSession for backward compatibility
val sc = spark.sparkContext
```

### Key Differences:
- **Scope:** `SparkContext` is more RDD-centric, while `SparkSession` provides a more comprehensive interface for Spark's higher-level APIs, including structured data processing with DataFrames and Datasets.
- **APIs:** `SparkSession` provides a more user-friendly API for Spark SQL and data operations, which is not directly available in the `SparkContext`.
- **Backward Compatibility:** `SparkSession` includes `SparkContext` as a part of it. So when you create a `SparkSession`, you can still access the `SparkContext` for operations that require it.

In summary, if you are using Spark 2.0 or later, it is recommended to use `SparkSession` as it provides a more streamlined and feature-rich interface for all Spark functionalities. `SparkContext` is still available for backward compatibility and for when you need to work with RDDs directly.