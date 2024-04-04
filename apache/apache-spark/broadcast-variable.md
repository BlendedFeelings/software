---
b: https://blendedfeelings.com/software/apache/apache-spark/broadcast-variable.md
---

# Broadcast Variables in Apache Spark
are a feature that allows the program to keep a read-only variable cached on each machine rather than shipping a copy of it with tasks. They are used to broadcast the common data (like lookup tables or machine learning models) that is needed by tasks across all nodes. By broadcasting this data, we can save on the network overhead of sending this data with every task.

Broadcast variables are used when the size of the data is large enough that the cost of sending it to each node is high, but not so large that it doesn't fit in memory. A typical use case might be to broadcast a large dataset that is used in a lookup operation in an RDD transformation.

Here's an example of how to use broadcast variables in Spark with Python (PySpark):

```python
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext()

# Create a large lookup table
large_lookup_table = {'key1': 'value1', 'key2': 'value2', ..., 'keyN': 'valueN'}

# Broadcast the lookup table to the cluster
broadcast_var = sc.broadcast(large_lookup_table)

# Now you can access the broadcasted data in an RDD operation
rdd = sc.parallelize(range(1, 100))
result_rdd = rdd.map(lambda x: (x, broadcast_var.value.get('key' + str(x), 'default_value')))

# Collect the results
results = result_rdd.collect()

# Stop the SparkContext
sc.stop()
```

In this example, `large_lookup_table` is the data that we want to broadcast to all the worker nodes. We use `sc.broadcast()` to create a broadcast variable that sends `large_lookup_table` to the nodes. Inside the RDD transformation (`map`), we can access the broadcasted data using `broadcast_var.value`.

Broadcast variables are especially useful in Spark when joining large datasets with small ones. Instead of performing a costly join operation, you can broadcast the smaller dataset and use it for lookups during RDD transformations.