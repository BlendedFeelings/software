---
b: https://blendedfeelings.com/software/apache/apache-spark/data-frame.md
---

# DataFrame In Spark
is a distributed collection of data organized into named columns, conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood. DataFrames can be constructed from a wide array of sources such as: structured data files, tables in Hive, external databases, or existing RDDs (Resilient Distributed Datasets).

Here are some of the key features of Spark DataFrames:

1. **Immutability and Lazy Evaluation**: DataFrames are immutable, meaning once created, they cannot be changed. They are also lazily evaluated, which means that the computation is not executed until an action (like `collect()` or `show()`) is called.

2. **Distributed**: DataFrames are distributed across the cluster, allowing for parallel processing on multiple nodes.

3. **Typed**: Each column in a DataFrame has a type associated with it.

4. **API Consistency**: DataFrames provide a domain-specific language (DSL) for data manipulation in Scala, Java, Python, and R.

5. **Optimization**: The Spark SQL Catalyst optimizer optimizes queries with DataFrame API, and the Tungsten execution engine provides efficient code generation and memory management.

6. **Interoperability**: DataFrames can be easily converted to and from RDDs, and can also be created from various data sources.

Here is a simple example of how to create a DataFrame in PySpark (the Python API for Spark):

```python
from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a DataFrame using a list of tuples
data = [("James", "Smith", "USA", 1),
        ("Michael", "Rose", "USA", 2),
        ("Robert", "Williams", "USA", 3),
        ("Maria", "Jones", "USA", 4)]

columns = ["firstname", "lastname", "country", "rank"]

df = spark.createDataFrame(data).toDF(*columns)

# Show the DataFrame
df.show()
```

In this example, we create a DataFrame `df` with four columns and four rows of data. The `show()` action triggers the computation and displays the data in a tabular form.

Spark DataFrames support a wide range of operations, including selection, filtering, aggregation, and joining, which are essential for data analysis and manipulation.