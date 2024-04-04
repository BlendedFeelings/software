---
b: https://blendedfeelings.com/software/apache/apache-spark/rdd-dataframes-datasets.md
---

# Resilient Distributed Datasets (RDDs), DataFrames, and Datasets
are abstractions for working with big data.Resilient Distributed Datasets (RDDs) are the foundational data structure in Apache Spark, offering low-level APIs for distributed data processing with fault tolerance and fine-grained control over computations. DataFrames provide a higher-level abstraction for structured data processing, allowing users to work with data in a tabular form with built-in query optimization through Spark's Catalyst optimizer. Datasets combine the type safety and functional programming benefits of RDDs with the optimization and ease-of-use features of DataFrames, making them a powerful tool for efficient data processing in Scala and Java.

### RDDs (Resilient Distributed Datasets)

- **Low-Level API**: RDDs are the fundamental data structure in Spark, providing a low-level API for data processing.
- **Immutable Collections**: They are immutable, distributed collections of objects, which can be processed in parallel across a Spark cluster.
- **Fault Tolerance**: RDDs provide fault tolerance through lineage; if a partition of an RDD is lost, it can be recomputed using the lineage information.
- **Language Support**: RDDs can be created and manipulated using APIs in Java, Scala, and Python.
- **Flexibility**: They allow users to perform functional programming and have complete control over the execution process.
- **Performance**: Operations on RDDs can have higher overheads due to the lack of optimization opportunities.

### DataFrames

- **High-Level API**: DataFrames are built on top of RDDs and provide a higher-level API that is similar to working with databases or data frames in R/Python (pandas).
- **Structured Data**: They represent data in a structured tabular form with rows and columns, where each column has a name and a type.
- **Optimization**: DataFrames allow Spark to manage the schema, which enables it to optimize query execution using the Catalyst optimizer and Tungsten execution engine.
- **Language Support**: DataFrames can be used in Java, Scala, Python, and R APIs.
- **Interoperability**: They can be easily converted to and from RDDs and can also be created from various data sources like Hive tables, JSON, and Parquet files.
- **Limited Control**: With DataFrames, users have less control over the physical execution compared to RDDs.

### Datasets

- **Unified API**: Datasets are a combination of RDDs and DataFrames, providing both the type safety of RDDs and the query optimization of DataFrames.
- **Type Safety**: Datasets are strongly typed in Scala and Java but are represented as DataFrames in Python and R, which do not have compile-time type safety.
- **Encoders**: They use encoders for serialization and deserialization. Encoders allow for more efficient serialization, which can lead to better performance for certain use cases.
- **Interoperability**: Datasets can interoperate with DataFrames and RDDs, allowing users to switch between different levels of abstraction.
- **Optimized Execution**: Like DataFrames, Datasets benefit from Catalyst optimizer and Tungsten execution engine for optimized execution plans.

In summary, RDDs are the low-level data processing abstraction that provides fine-grained control but lacks built-in optimization. DataFrames provide a higher-level abstraction with built-in optimization for structured data processing. Datasets combine the benefits of RDDs and DataFrames by offering type safety and optimization for structured and semi-structured data. The choice between these abstractions depends on the specific use case, the need for optimization, and the preference for type safety.