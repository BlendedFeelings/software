---
b: https://blendedfeelings.com/software/design/lambda-architecture.md
---

# Lambda Architecture 
is a data-processing architecture designed to handle massive quantities of data (big data) by providing a robust, scalable, and fault-tolerant system. It was proposed by Nathan Marz in the early 2010s. The architecture is named after the Greek letter lambda (λ), which is used to denote the different layers of the architecture.

Lambda Architecture is built around three main components:

1. **Batch Layer**: This layer is responsible for managing the master dataset, which is an immutable, append-only set of raw data. The batch layer pre-computes the master dataset into batch views so that queries can be answered with low latency. These computations are typically run on a distributed data processing system like Apache Hadoop.

2. **Speed Layer**: The purpose of the speed layer is to compensate for the high latency of updates to the batch views. It processes data in real-time and provides real-time views. The results from the speed layer are only temporary, as eventually, the batch layer will process the same data and provide a more accurate and comprehensive view. Apache Storm and Apache Spark Streaming are examples of technologies that can be used in the speed layer.

3. **Serving Layer**: This layer indexes the batch views so that they can be queried in an ad-hoc manner. It merges the results from the batch views and the real-time views to provide a complete answer to a query. The serving layer is designed to respond to queries in a low-latency manner, often using a distributed database like Apache HBase or Cassandra.

The key idea behind Lambda Architecture is to provide a system that can serve accurate and comprehensive data views while also being able to handle updates in real-time. This is achieved by running the batch and speed layers in parallel and combining their outputs in the serving layer. The architecture allows for the handling of both historical and real-time data in a way that balances throughput, latency, and fault-tolerance.

Lambda Architecture has been influential in the design of big data systems, although some alternatives and evolutions have been proposed since its inception, such as the Kappa Architecture, which simplifies the architecture by only using a single processing stream for both real-time and batch processing.