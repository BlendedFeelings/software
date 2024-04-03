---
b: https://blendedfeelings.com/software/design/kappa-architecture.md
---

# Kappa Architecture 
is a data processing architecture designed to handle streaming data. It was proposed as a simplification of the Lambda Architecture, which combines batch processing and stream processing. The Kappa Architecture, in contrast, uses a single processing layer, which simplifies the system's design and operation.

Here's an overview of the key concepts in Kappa Architecture:

1. **Event Logs**: At the heart of the Kappa Architecture is an immutable sequence of records, often referred to as an event log or a commit log. This log stores a historical record of all events (data changes) in the system.

2. **Stream Processing**: A stream processing system reads data from the event log and processes it in real time. This is the only processing layer in the Kappa Architecture, which distinguishes it from the Lambda Architecture that also includes a batch processing layer.

3. **Processing Jobs**: The stream processing layer consists of jobs or applications that subscribe to the event log and perform computations on the incoming data. These jobs can be used for real-time analytics, data enrichment, filtering, or any other data processing tasks.

4. **State Management**: As the processing jobs read from the event log, they often need to maintain state. This can be done using databases or in-memory data stores. The state is built from the event log and can be rebuilt at any time by reprocessing the log from the beginning.

5. **Serving Layer**: The processed data is then made available to end-users or downstream systems through a serving layer, which could be a database, a cache, or an API.

The Kappa Architecture is particularly well-suited for scenarios where data needs to be processed in real time and where the simplicity of having a single processing layer is beneficial. It eliminates the complexity of managing two separate codebases for batch and stream processing, which is a common challenge in the Lambda Architecture.

However, the Kappa Architecture also has its limitations. For example, it may not be as efficient for processing large historical data sets, and it requires that the event log be durable and capable of storing all historical data, which can be challenging for systems with very high volumes of data.