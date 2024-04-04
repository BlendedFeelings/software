---
b: https://blendedfeelings.com/software/apache/apache-spark/sparksession.md
---

# SparkSession
is the entry point to programming Spark with the Dataset and DataFrame API. It is used to create DataFrames, register DataFrames as tables, execute SQL over tables, cache tables, and read parquet files.

To create a `SparkSession`, you typically use its builder pattern as shown below:

```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("My Spark Application")  // Name of your application
  .config("spark.master", "local")  // Master node URL
  .getOrCreate()

// Now you can use `spark` to create DataFrames, register DataFrames as tables, etc.
```

In the above code snippet, we import the `SparkSession` class from the Spark SQL library and use its builder to configure the application name and the master URL. The `local` master URL means that Spark will run locally on your machine with one thread. You can specify `local[*]` to run locally with as many worker threads as logical cores on your machine.

Remember that in a real-world scenario, you would configure the master to the URL of your cluster's master node.

Once the `SparkSession` is created, it can be used to perform a variety of data operations.

Please note that the above code is written in Scala, which is one of the languages commonly used with Spark. Spark also supports Python and Java, and the way to create a `SparkSession` is similar across these languages.