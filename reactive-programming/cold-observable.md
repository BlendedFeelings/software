---
b: https://blendedfeelings.com/software/reactive-programming/cold-observable.md
---

# Cold observables
are a type of observables that do not start emitting items until an observer subscribes to them. This is in contrast to hot observables, which may begin emitting items as soon as they are created, regardless of whether there are any subscribers.

Here are some key characteristics of cold observables:

1. **Lazy Execution**: Cold observables are lazy, meaning the data production starts only after a subscription is made. This is akin to calling a function: the code inside a function does not run until the function is called.

2. **Subscription Creates the Observable**: Each subscription to a cold observable creates a new instance of the observable sequence. This means that each subscriber gets its own unique sequence of data items.

3. **Unicast**: Cold observables are unicast – each subscribed observer owns an independent execution of the observable. If you have multiple subscribers, each one will receive a separate stream of data.

4. **Replaying Data**: Since each subscriber causes the observable to start from the beginning, subscribers can effectively "replay" the data by resubscribing.

5. **Examples**: Common examples of cold observables are HTTP requests, file reads, or any other I/O operation where the data is produced on-demand for each subscriber.

Here's a simple example in RxJS, a popular reactive programming library for JavaScript:

```javascript
const { Observable } = require('rxjs');

// This is a cold observable because the data production, in this case, a simple
// calculation, does not start until someone subscribes to the observable.
const coldObservable = new Observable(subscriber => {
  // Simulate a simple calculation
  const result = 2 + 2;
  subscriber.next(result);
  subscriber.complete();
});

// First subscription
coldObservable.subscribe(value => console.log(`First subscriber: ${value}`));

// Second subscription
coldObservable.subscribe(value => console.log(`Second subscriber: ${value}`));
```

In the above example, the calculation `2 + 2` is performed twice, once for each subscriber. Each subscriber receives the result independently of the other.

Cold observables are useful when you want to ensure that data is fresh and that each subscriber gets the latest data from the start of the sequence. They are also useful when the data is specific to each subscriber, such as user input or time-based events.