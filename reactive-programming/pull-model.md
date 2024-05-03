---
b: https://blendedfeelings.com/software/reactive-programming/pull-model.md
---

# Pull Model 
also known as Interactive or Iterable is a execution model where consumers (subscribers) explicitly request data from producers. This is a demand-driven or lazy approach, where the computation or the data production is deferred until it's explicitly requested by the consumer. This is akin to the `Iterable` pattern in many programming languages, where an iterator is used to pull elements from a collection one at a time.

#### Characteristics of the Pull Model:

1. **Consumer Control**: The consumer controls the flow of data by requesting the next piece of data when it's ready to handle it.
2. **Lazy Evaluation**: Data is not produced until the consumer requests it, which can lead to more efficient use of resources if not all data is needed.
3. **Backpressure**: Since the consumer requests data when it can process it, this naturally provides a mechanism for backpressure. Backpressure is the ability to signal to the producer that the consumer is overwhelmed and cannot handle more data at the current pace.
4. **Synchronous**: The pull model is often synchronous because the consumer waits for the producer to generate and deliver the data.

### Example in Java (Iterable):

```java
Iterable<Integer> iterable = Arrays.asList(1, 2, 3, 4, 5);

for (int value : iterable) {
    System.out.println("Consumed: " + value);
    // The consumer 'pulls' the next value when it's ready for it.
}
```

In the above example, the `for-each` loop is a consumer that pulls values from the `Iterable` collection one by one.

### Reactive Streams and Pull Model:

Reactive Streams is an initiative to provide a standard for asynchronous stream processing with non-blocking backpressure. It includes the concept of a `Publisher` and a `Subscriber`, where the `Subscriber` requests a certain amount of data from the `Publisher`. This is an example of the pull model in a reactive setting.

Here's a simplified example using Project Reactor in Java:

```java
Flux<Integer> flux = Flux.range(1, 5);

flux.subscribe(
    data -> System.out.println("OnNext: " + data),
    error -> System.err.println("OnError: " + error.getMessage()),
    () -> System.out.println("OnComplete"),
    subscription -> {
        // This is where the subscriber requests data from the publisher
        subscription.request(1);
    }
);
```

In this example, the `subscribe` method with the `subscription` parameter allows the subscriber to request how many elements it wants to receive, implementing the pull model.

In summary, the pull model in reactive programming is about consumers requesting data when they are ready to process it, providing a mechanism for efficient data handling and backpressure management.