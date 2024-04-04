---
b: https://blendedfeelings.com/software/apache/apache-spark/sparkcontext.md
---

# SparkContext
is the entry point to programming with Apache Spark, a fast and general engine for large-scale data processing. It allows your Spark application to access Spark's distributed data processing capabilities. When you write a Spark application in Python using PySpark, you typically start by creating a `SparkContext` object.

Here's a basic example of how you would create a `SparkContext` in a PySpark application:

```python
from pyspark import SparkConf, SparkContext

# Create a SparkConf object to configure the application
conf = SparkConf().setAppName("My Spark Application").setMaster("local[*]")

# Create a SparkContext object with the configuration
sc = SparkContext(conf=conf)

# Your Spark code goes here

# Stop the SparkContext when done to free up resources
sc.stop()
```

In the above code:

- `SparkConf` allows you to configure various aspects of your Spark application, such as the application name and the master URL.
- `setAppName("My Spark Application")` sets a name for your application, which will be shown in the Spark web UI.
- `setMaster("local[*]")` sets the master URL for your application. In this case, it's set to run locally with as many worker threads as logical cores on your machine (`[*]` means use all available cores).
- `SparkContext` is created with the configuration object `conf`. This is the object that you use to interact with the Spark cluster.
- `sc.stop()` is called at the end of your application to shut down the SparkContext.

Please note that in a cluster environment, you would set the master to the URL of your cluster's master node instead of `local[*]`. Also, when running in a notebook or an interactive environment, you typically do not need to explicitly create a `SparkContext` as it is created for you (e.g., when using `pyspark` shell or Databricks notebooks).