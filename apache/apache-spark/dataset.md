---
b: https://blendedfeelings.com/software/apache/apache-spark/dataset.md
---

# Datasets in Apache Spark
are a distributed collection of data that provides the benefits of RDDs (Resilient Distributed Datasets) with the optimizations provided by the Spark SQL execution engine. Datasets are a strictly typed API available in Spark, which allows for more compile-time safety and better performance optimizations during execution.

Here are some key points about Spark Datasets:

1. **Typed Interface**: Unlike RDDs, which are a collection of any type of object, Datasets are a collection of a specific type of object. This type information allows Spark to serialize data more efficiently and to perform more optimizations during query execution.

2. **Lazy Evaluation**: Similar to RDDs, Datasets are evaluated lazily. Computations on Datasets are not executed until an action (like `collect`, `count`, `show`, etc.) is invoked.

3. **Interoperability**: Datasets can be easily converted to DataFrames and vice versa. This allows users to take advantage of the Dataset API's type safety and the DataFrame API's convenience for SQL-like operations.

4. **Optimized Execution**: Spark SQL's Catalyst optimizer can optimize Dataset operations, resulting in more efficient execution plans. This can lead to better performance compared to RDDs, especially for complex queries.

5. **Support for Lambda Functions**: Datasets allow you to manipulate data using lambda functions, similar to RDDs, which can be more intuitive for users coming from a functional programming background.

6. **Encoders**: Datasets use encoders to convert between JVM objects and Spark SQL's internal binary format. Encoders are responsible for serialization and deserialization, allowing for more compact data storage and faster data processing.

7. **Compatibility**: Datasets are available in Scala and Java, the statically typed languages supported by Spark. The Python and R APIs do not have the Dataset API and instead use DataFrames, which are a special case of Datasets with untyped Rows.

Here is an example of creating and using a Dataset in Scala:

```scala
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.Dataset

// Define a case class that represents the type of our Dataset
case class Person(name: String, age: Int)

// Create a SparkSession
val spark = SparkSession.builder.appName("DatasetExample").getOrCreate()

// For implicit conversions like converting RDDs to DataFrames
import spark.implicits._

// Create a Dataset using a sequence of case class objects
val peopleDS: Dataset[Person] = Seq(Person("Alice", 29), Person("Bob", 31)).toDS()

// Show the contents of the Dataset
peopleDS.show()

// Stop the SparkSession
spark.stop()
```

In this example, we define a `Person` case class, create a `SparkSession`, and then create a `Dataset[Person]` using a sequence of `Person` objects. Finally, we display the contents of the Dataset and stop the Spark session.