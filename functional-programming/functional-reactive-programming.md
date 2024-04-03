---
b: https://blendedfeelings.com/software/functional-programming/functional-reactive-programming.md
---

# Functional Reactive Programming (FRP) 
is a programming paradigm for reactive programming (asynchronous dataflow programming) using the building blocks of functional programming (e.g., pure functions, higher-order functions, and types). It provides a framework for working with values that change over time, such as user input, sensor data, or messages from other programs.

FRP is particularly well-suited for dealing with time-varying values in a declarative way, which can lead to more readable and maintainable code. It allows developers to express the logic of computation as a series of transformations on streams of data. These streams are called "signals" or "observables" in different FRP systems.

Here are some key concepts in FRP:

1. **Immutable Values**: In functional programming, values are immutable. Once created, they cannot be changed. This principle is also applied in FRP, where the data flowing through the streams is immutable.

2. **Pure Functions**: Functions in FRP should be pure, meaning they have no side effects and always produce the same output for the same input. This makes the behavior of the system more predictable and easier to reason about.

3. **Signals/Observables**: These are abstractions that represent a value that changes over time. They can be thought of as a type of dynamic variable that emits a new value whenever it changes.

4. **Subscribers**: Components that are interested in the value of a signal can subscribe to it. When the signal emits a new value, all its subscribers are notified and can react to the change.

5. **Operators**: FRP provides a set of operators that can be used to transform, combine, and create new signals from existing ones. Examples include `map`, `filter`, `merge`, `concat`, `flatMap`, etc.

6. **Event Streams**: These are similar to signals but represent a series of events over time rather than a continuously changing value.

7. **Time-Variant Relationships**: FRP makes it easy to define relationships between values that can change over time, without having to manually track and update those relationships.

FRP can be implemented in various functional programming languages or can be available as libraries in multi-paradigm languages. For instance, Haskell has libraries like `reactive-banana` and `reflex`, while in JavaScript, libraries like RxJS provide FRP concepts.

Implementing FRP typically involves creating observables for the data sources, applying a series of transformations using pure functions, and finally subscribing to the resulting observables to perform side effects or update the UI.

FRP is particularly useful in user interface programming, where user actions can be treated as event streams, and the UI can react to changes in the underlying data model. It also has applications in robotics, game development, and any domain where a system needs to respond to a continuous stream of asynchronous events.