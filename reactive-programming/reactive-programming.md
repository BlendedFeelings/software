---
b: https://blendedfeelings.com/software/reactive-programming/reactive-programming.md
---

# Reactive Programming 
is a programming paradigm oriented around data flows and the propagation of change. It means that when a data flow is emitted by one component, other components that depend on that data flow react by updating themselves in response. This paradigm is particularly useful for developing systems that need to react to real-time information, such as UIs, real-time trading systems, or systems that handle streams of data from IoT devices.

Key concepts in Reactive Programming include:

1. **Observables**: These represent sources of data or events. Observables emit values over time.

2. **Observers**: These are entities that listen to Observables. They react to the values or events emitted by the Observables.

3. **Subscriptions**: When an Observer is interested in an Observable's emitted values, it subscribes to the Observable. The subscription is the connection through which the values are passed.

4. **Operators**: These are methods that allow for the transformation, combination, and manipulation of data streams that Observables emit.

5. **Schedulers**: These manage concurrency, allowing for the coordination of when and where the computations on the streams happen (e.g., on which thread or with what priority).

6. **Streams**: A sequence of ongoing events ordered in time that offer some hooks with which to observe and manipulate the data.

Reactive Programming libraries and frameworks provide tools to work with these concepts. For example, in the JavaScript world, RxJS (Reactive Extensions for JavaScript) is a widely-used library. In the Java world, there's Project Reactor and RxJava. On the .NET platform, there's System.Reactive.

An example of Reactive Programming can be seen in a UI application where user inputs, server responses, and other events are treated as data streams that can be subscribed to and reacted upon. This results in a more declarative and flexible way to handle asynchronous data flows and concurrency.

Reactive Programming is different from the traditional imperative programming model because it is fundamentally asynchronous and event-driven. Traditional imperative programming often requires explicit management of state and the flow of control, whereas Reactive Programming abstracts those concerns, allowing developers to focus on the relationships between data flows and how they propagate through the system.