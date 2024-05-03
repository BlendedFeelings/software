---
b: https://blendedfeelings.com/software/reactive-programming/fan-in-out.md
---

# Fan in and fan out 
are used to describe patterns that deal with the flow of data between different parts of a system, particularly when dealing with streams of data or events.

### Fan Out

Fan out refers to the process of taking a single input stream and processing it in multiple ways in parallel. This typically involves splitting the stream into several streams that can be handled independently. Each of these streams may perform different operations on the data, but they all start from the same source.

For example, imagine a stream of sensor data that needs to be analyzed. The fan-out pattern would involve taking this single stream and creating multiple streams from it, where one stream might calculate averages, another might detect anomalies, and a third might archive the data for long-term storage. All of these operations can occur simultaneously.

In a programming context, fan out can be implemented using operators that duplicate the incoming stream, such as `publish` and `multicast` in RxJS, allowing multiple subscribers to listen to the same data source.

### Fan In

Fan in is the opposite process: it involves taking multiple input streams and combining them into a single output stream. This can be done by merging the streams, concatenating them, or using more complex operations like zip or combineLatest, which wait for all the input streams to provide values before producing a result.

For example, consider a user interface that needs to update based on several data sources, such as user input, incoming messages, and system notifications. The fan-in pattern would involve taking these individual streams and merging them into a single stream that the user interface subscribes to for updates.

In reactive programming libraries, fan in can be implemented with operators like `merge`, `concat`, or `combineLatest`, depending on the desired behavior for how the streams should be combined.

### Summary

- **Fan Out**: Splitting a single stream into multiple streams that can be processed in parallel.
- **Fan In**: Combining multiple streams into a single stream to be processed together.

These patterns are essential in reactive programming for creating scalable and responsive applications that can handle complex data flows and operations. They allow developers to compose asynchronous and event-based programs in a declarative style, which can be easier to understand and maintain.