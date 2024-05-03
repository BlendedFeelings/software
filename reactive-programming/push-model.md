---
b: https://blendedfeelings.com/software/reactive-programming/push-model.md
---

# Push model 
is a paradigm where data producers (sometimes called publishers) actively send or "push" data to consumers (subscribers) when new data becomes available. This is in contrast to the pull model, where consumers request or "pull" data from producers when they are ready to process it.

Here's how the push model works in the context of reactive programming:

1. **Observables/Streams**: Data is represented as a stream of events or values over time, which can be observed. These streams are known as observables.

2. **Producers**: The producers are the ones who generate the data. In the push model, producers determine when the data is sent to the consumers. They are responsible for pushing the new data or events into the stream.

3. **Subscribers**: Consumers, or subscribers, express interest in the data by subscribing to the observables. They provide a callback function that will be invoked whenever new data is pushed into the stream.

4. **Notifications**: When new data is available, the producer pushes the data into the stream, which then automatically notifies all subscribed consumers by invoking their callback functions with the new data.

5. **Asynchronous Processing**: The push model is inherently asynchronous. Producers do not wait for consumers to be ready; they push the data whenever it's available, and the consumers handle it asynchronously.

6. **Backpressure**: In some reactive systems, there is a mechanism to handle backpressure, which occurs when consumers cannot keep up with the rate at which producers are pushing data. This mechanism allows consumers to signal to producers to slow down the data flow.

7. **Completion and Error Handling**: Observables can also push completion or error notifications to indicate that there is no more data to be sent or that an error has occurred in the data production process.

The push model is particularly useful in scenarios where data is produced at unpredictable intervals, such as user input events, stock prices updates, sensor data, etc. It allows for a more responsive and resource-efficient system, as consumers do not have to constantly check for new data.

Reactive programming libraries and frameworks such as RxJS (Reactive Extensions for JavaScript), Project Reactor for Java, and ReactiveX for various languages, implement the push model and provide abstractions to work with asynchronous data streams effectively.