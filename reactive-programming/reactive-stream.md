---
b: https://blendedfeelings.com/software/reactive-programming/reactive-stream.md
---

# Reactive Streams 
is an initiative to provide a standard for asynchronous stream processing with non-blocking back pressure. It defines a set of interfaces for publishing and subscribing to streams, handling back pressure, and processing stream data in an asynchronous and non-blocking manner. The main goal is to allow different parts of a system to communicate with each other effectively, especially when they have different capacities for handling data.

The Reactive Streams specification consists of the following main components:

1. **Publisher**: A provider of a potentially unbounded number of sequenced elements, publishing them according to the demand received from its Subscriber(s).

2. **Subscriber**: A receiver of messages. The Subscriber has the responsibility of signaling the demand to the Publisher and processing the received elements from the stream.

3. **Subscription**: A link between a Publisher and a Subscriber. Once a Subscriber subscribes to a Publisher, a Subscription is created. The Subscription can be used by the Subscriber to signal demand or cancel the subscription.

4. **Processor**: A component that acts as both a Subscriber and a Publisher. It receives elements from upstream and processes them, potentially altering them or combining them with other data, before passing them on to downstream Subscribers.

The key feature of Reactive Streams is the concept of back pressure, which is a mechanism that allows Subscribers to control the flow of data so that they are not overwhelmed. The Subscriber can request a specific number of elements from the Publisher and can request more elements as needed. If the Subscriber cannot process the data quickly enough, it can signal to the Publisher to slow down, preventing an overflow of data and potential system failure.

Reactive Streams has been adopted by various programming languages and frameworks. In Java, for example, it's part of the Java 9 release, in the form of the `java.util.concurrent.Flow` API. Other implementations and libraries that follow the Reactive Streams specification include Project Reactor (part of the Spring Framework), RxJava, Akka Streams, and many others.

The Reactive Streams API is minimalistic and is not meant to be used directly by most applications. Instead, it serves as a foundation upon which more user-friendly and feature-rich reactive libraries and frameworks can be built. These libraries provide additional abstractions and tools to make it easier to build reactive systems.

Here's a high-level overview of how the interaction between these components works:

1. **Subscription**:
   - A `Subscriber` signals its interest in receiving data by subscribing to a `Publisher`.
   - In response, the `Publisher` sends a `Subscription` object to the `Subscriber`.
   - The `Subscription` is the contract between the `Publisher` and `Subscriber`.

2. **Demand (Back Pressure)**:
   - The `Subscriber` requests a certain number of items from the `Publisher` using the `Subscription`'s `request(n)` method, where `n` is the number of items it is prepared to handle. This is how back pressure is applied; the `Subscriber` controls the flow of data by specifying how much data it can process at a time.
   - The `Publisher` is obligated to send no more than this requested number of items to the `Subscriber`. It can send fewer items if that's all it has available.

3. **Data Flow**:
   - The `Publisher` sends items to the `Subscriber` by calling the `Subscriber`'s `onNext(item)` method for each item.
   - The `Subscriber` processes each item as it arrives.

4. **Completion or Error**:
   - If the `Publisher` has no more items to send and the sequence is complete, it calls the `Subscriber`'s `onComplete()` method to signal completion.
   - If there is an error during the processing of the stream, the `Publisher` calls the `Subscriber`'s `onError(error)` method to signal that an error has occurred. After this, no more items will be sent.

5. **Cancellation**:
   - At any point, the `Subscriber` can signal that it is no longer interested in receiving data by calling the `Subscription`'s `cancel()` method. This tells the `Publisher` to stop sending items.

6. **Processor** (optional):
   - A `Processor` acts as both a `Subscriber` and a `Publisher`. It receives items from an upstream `Publisher`, processes them, and publishes the results to downstream `Subscribers`.
   - The `Processor` itself follows the same back pressure protocol to manage the flow of data through it.

Here's a simple example in pseudocode to illustrate the interaction:

```pseudo
// A simple Publisher that publishes integers from 1 to 10
Publisher<Integer> publisher = new RangePublisher(1, 10);

// A simple Subscriber that prints integers and requests one item at a time
Subscriber<Integer> subscriber = new Subscriber<Integer>() {
    private Subscription subscription;

    @Override
    public void onSubscribe(Subscription subscription) {
        this.subscription = subscription;
        subscription.request(1); // Request the first item
    }

    @Override
    public void onNext(Integer item) {
        System.out.println(item);
        subscription.request(1); // Request the next item after processing
    }

    @Override
    public void onError(Throwable t) {
        t.printStackTrace();
    }

    @Override
    public void onComplete() {
        System.out.println("Done");
    }
};

// Subscribe the Subscriber to the Publisher
publisher.subscribe(subscriber);
```

In this example, the `Subscriber` requests one item at a time, ensuring that it is not overwhelmed by too many items. The `Publisher` respects this demand and sends items one by one. This simple interaction encapsulates the core principles of Reactive Streams: asynchronous data flow with non-blocking back pressure.