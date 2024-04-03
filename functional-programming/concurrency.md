---
b: https://blendedfeelings.com/software/functional-programming/concurrency.md
---

# Concurrency in functional programming 
can be quite different from the traditional imperative programming model due to the nature of functional programming itself. Functional programming emphasizes the use of pure functions, which are functions that always produce the same output given the same input and have no side effects. This characteristic makes functional programming well-suited for concurrent execution because pure functions can be run in parallel without the risk of race conditions or other concurrency issues that are common in imperative programming.

Here are some key points about concurrency in functional programming:

1. **Immutability**: Functional programming often relies on immutable data structures, which means that once a data structure is created, it cannot be changed. This eliminates the need for locks or other synchronization mechanisms when accessing data concurrently, as there is no danger of one thread altering the data in a way that could affect another thread.

2. **Pure Functions**: As mentioned earlier, pure functions are a cornerstone of functional programming. Because they do not rely on or modify any external state, pure functions can be executed concurrently without fear of side effects.

3. **First-class Functions**: Functional programming treats functions as first-class citizens, meaning they can be passed as arguments to other functions, returned as values, and assigned to variables. This allows for higher-order functions that can abstract patterns of concurrency, such as map-reduce operations, which can be easily parallelized.

4. **Lazy Evaluation**: Some functional languages use lazy evaluation, where expressions are not evaluated until their results are needed. This can help with concurrency by allowing the creation of potentially infinite data structures and deferring computation until it's actually required.

5. **Functional Concurrency Primitives**: Many functional languages provide concurrency primitives that are consistent with functional programming principles. For example, Haskell has `forkIO` for lightweight thread creation and software transactional memory (STM) for managing shared state in a composable way.

6. **Actor Model**: Some functional languages, like Erlang and Elixir, use the actor model for concurrency. In this model, actors are independent entities that communicate with each other via message passing, and each actor can process messages concurrently in isolation from other actors.

7. **Parallel Collections**: Languages like Scala provide parallel collections that enable operations on collections to be automatically parallelized, abstracting away the low-level threading details.

8. **Asynchronous Programming**: Functional programming also embraces asynchronous programming patterns, using futures and promises to represent values that will be available in the future, which can be composed in a functional style.

9. **Functional Reactive Programming (FRP)**: FRP is a programming paradigm for reactive programming (programming with asynchronous data streams) using the building blocks of functional programming. It allows for elegant and powerful ways to handle events and data streams in a concurrent environment.

10. **Effect Systems**: Some functional languages use effect systems to track the effects (like IO or state mutation) that functions can have, allowing for a more controlled form of side effects that can still be reasoned about in a concurrent setting.

In summary, concurrency in functional programming is facilitated by the use of immutable data, pure functions, and high-level abstractions that allow for concurrent operations without the typical concerns of data races and mutable shared state.