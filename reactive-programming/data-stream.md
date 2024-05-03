---
b: https://blendedfeelings.com/software/reactive-programming/data-stream.md
---

# Data stream 
is a sequence of asynchronous data items that can be observed over time. These data items can represent anything from variables, user inputs, properties, caches, data structures, etc. Essentially, a data stream is a model for handling data that changes or evolves over time.

Here are some key characteristics of data streams in reactive programming:

1. **Asynchronous**: Data streams can emit values at any point in time, not necessarily in a predictable manner. This allows for handling of real-time data or events that occur independently of the main program flow.

2. **Observable**: Data streams are observable, meaning that developers can subscribe to them and react to the data items or events as they occur. This is done using observer patterns or similar constructs.

3. **Immutable**: Once a data item has been emitted by a stream, it cannot be changed. If data needs to be updated, a new item is emitted.

4. **Continuous**: Data streams can be infinite, where they continue to emit data as long as the application is running, or they can be finite, where they complete after a certain condition is met or a certain amount of data has been emitted.

5. **Composable**: Data streams can be combined, filtered, transformed, and manipulated using various operators to create new streams. This composability allows for complex data flow architectures and reactive chains.

6. **Event-driven**: Data streams are often used in event-driven architectures, where the emission of a new item is considered an event that subscribers can handle.

In reactive programming, libraries and frameworks like RxJS (Reactive Extensions for JavaScript), Project Reactor for Java, and others provide tools to work with data streams. They offer a rich set of operators for creating, transforming, combining, and consuming data streams, allowing developers to write code that is more declarative and less concerned with low-level threading and synchronization details.