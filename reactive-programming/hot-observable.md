---
b: https://blendedfeelings.com/software/reactive-programming/hot-observable.md
---

# Hot observables
are active and start emitting items as soon as they are created, regardless of whether there are any subscribers. When a subscriber subscribes to a hot observable, it begins to receive items emitted from that point forward, potentially missing any items that were emitted before the subscription.

An analogy for hot observables is a live concert or a broadcast. If you tune in late, you miss the beginning and only see the performance from the moment you start watching.

### Key Differences
- **Subscription**: Cold observables start emitting upon subscription, while hot observables emit regardless of subscriptions.
- **Shared Execution**: Hot observables share execution among all subscribers, while cold observables do not.
- **Items Sequence**: Subscribers to cold observables receive the entire sequence of items from the start, while subscribers to hot observables only receive items from the point of subscription.

### Converting Between Hot and Cold
It is possible to convert a cold observable into a hot observable and vice versa. For example, you can use operators like `publish()` and `connect()` to convert a cold observable into a hot one by making it start emitting items immediately and sharing the emitted items with all subscribers.

Conversely, you can take a hot observable and use operators like `replay()` or `cache()` to ensure that new subscribers receive items that were previously emitted, thus mimicking the behavior of a cold observable.

### Use Cases
- **Cold Observables**: Ideal for sequences where each subscriber needs the full data set independently, such as HTTP requests or file reads.
- **Hot Observables**: Suitable for representing events or data that is live and continuous, such as mouse movements, stock tickers, or sensor data.

In summary, the choice between hot and cold observables depends on the nature of the data stream and the desired behavior for subscribers. Understanding and utilizing hot observables correctly is essential in scenarios where the timing of subscriptions relative to the data stream is important.