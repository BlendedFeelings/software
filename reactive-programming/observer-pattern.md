---
b: https://blendedfeelings.com/software/reactive-programming/observer-pattern.md
---

# Observer pattern 
is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. It is mainly used to implement distributed event handling systems, in a "publish-subscribe" model.

In reactive programming, the observer pattern plays a fundamental role. Reactive programming is a declarative programming paradigm concerned with data streams and the propagation of change. It's about being able to react to sequences of events over time.

Here's how the observer pattern is typically used in reactive programming:

1. **Observable**: This is the source of data or events. Observables emit data or events to which observers can subscribe. In reactive programming libraries/frameworks such as RxJS, you create observables that represent streams of data.

2. **Observer**: This is the entity that is interested in the data or events emitted by the observable. An observer subscribes to an observable and defines callback functions to handle the data or events it receives. These callback functions usually include `onNext` (to handle each new piece of data), `onError` (to handle any error that occurs in the data stream), and `onCompleted` (to handle the completion of the data stream).

3. **Subscription**: When an observer subscribes to an observable, a subscription is created. This subscription represents the ongoing process of the observer listening to the observable. The observer can also unsubscribe from the observable, which is a way of saying it is no longer interested in receiving data or events.

4. **Operators**: In reactive programming, there are numerous operators that can be used to transform, filter, combine, and otherwise manipulate data streams. These operators return new observables, allowing for the creation of complex data processing pipelines that are both declarative and composable.

Here's a simple conceptual example in pseudo-code:

```javascript
// Create an observable that emits a value every second
let observable = new Observable((observer) => {
    let count = 0;
    let interval = setInterval(() => {
        observer.onNext(count++);
    }, 1000);
    
    // Provide a way to cancel and clean up the interval resource
    return () => clearInterval(interval);
});

// Create an observer
let myObserver = {
    onNext: (value) => console.log(`Value: ${value}`),
    onError: (error) => console.log(`Error: ${error}`),
    onCompleted: () => console.log('Completed')
};

// Subscribe the observer to the observable
let subscription = observable.subscribe(myObserver);

// After 5 seconds, unsubscribe from the observable
setTimeout(() => {
    subscription.unsubscribe();
    console.log('Unsubscribed');
}, 5000);
```

In this example, the observable emits a new value every second. The observer logs each value to the console. After 5 seconds, we unsubscribe from the observable to stop receiving values.

Reactive programming libraries like RxJS (for JavaScript), ReactiveX for other languages (like RxJava for Java, RxSwift for Swift, etc.), and others provide a rich set of tools to work with the observer pattern in a reactive way. They offer a powerful abstraction for managing asynchronous data flows and event handling in a scalable and maintainable manner.