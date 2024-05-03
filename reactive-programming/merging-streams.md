---
b: https://blendedfeelings.com/software/reactive-programming/merging-streams.md
---

# Merging streams 
refers to the combination of multiple streams of data into a single stream. This pattern is often used when you want to treat data from different sources as if it were coming from a single source. The merged stream emits items as they come from any of the source streams.

Here's an example of how you might merge streams in Reactive Extensions (Rx), which is a popular library for reactive programming in various languages:

```csharp
IObservable<int> firstStream = Observable.Interval(TimeSpan.FromSeconds(1)).Select(_ => 1);
IObservable<int> secondStream = Observable.Interval(TimeSpan.FromSeconds(2)).Select(_ => 2);

IObservable<int> mergedStream = firstStream.Merge(secondStream);

mergedStream.Subscribe(Console.WriteLine);
```

In this C# example using Rx.NET:

- `firstStream` emits the number 1 every second.
- `secondStream` emits the number 2 every two seconds.
- `mergedStream` is the result of merging `firstStream` and `secondStream`. It will emit 1, 2, 1, 1, 2, 1, 1, 2, and so on.

The `Subscribe` method is used to start listening to the merged stream and print the emitted items to the console.

In Reactive Programming, the merge operation is typically non-blocking and the order of items in the merged stream corresponds to their emission order in the source streams. This means that if two items are emitted at the same time from different streams, their order in the merged stream might not be guaranteed.

There are other operators related to merging streams, such as `Concat`, `Zip`, and `CombineLatest`, each with its own semantics for how the streams are combined. For example:

- `Concat` will subscribe to the second stream only after the first one completes.
- `Zip` will combine items from two or more streams into a single item, waiting for all streams to emit before emitting the combined item.
- `CombineLatest` will emit an item whenever any of the source streams emit an item, combining it with the latest emitted items from the other streams.

Each of these operators is useful in different scenarios depending on the desired behavior of the stream combination.