---
b: https://blendedfeelings.com/software/functional-programming/algebraic-effect.md
---

# Algebraic effects 
are a feature of some functional programming languages that allow side effects to be treated in a structured and composable way. They are called "algebraic" because they can be understood and manipulated using algebraic laws, which makes reasoning about effects and their interactions much simpler.

In traditional functional programming, side effects (such as I/O, state mutation, exception handling, etc.) are often handled using monads. Monads are a powerful abstraction, but they can sometimes be cumbersome to use, especially when you want to combine different kinds of effects.

Algebraic effects aim to provide a more flexible and modular approach to handling side effects. The key idea is to separate the definition of an effect from its implementation. An effect is defined as a set of operations that can be performed, without specifying how those operations are implemented. The implementation is provided by a handler, which can be thought of as a kind of dynamic scope that interprets the operations.

Here's a basic outline of how algebraic effects and handlers work:

1. **Effects**: These are abstract descriptions of the operations that can be performed. For instance, an effect for mutable state might include operations like `get` and `put`.

2. **Handlers**: These are constructs that provide the concrete implementation for the effects. A handler for the mutable state effect might implement `get` and `put` using an actual mutable variable.

3. **Performing Effects**: When a piece of code wants to perform an effectful operation, it uses a special construct (often called `perform` or `effect`) to indicate which operation it wants to carry out.

4. **Handling Effects**: When an effect is performed, it is intercepted by the nearest enclosing handler for that effect. The handler then decides what to do with the operation—whether to carry it out, transform it, pass it along to another handler, or something else.

Algebraic effects can be used to model a wide variety of side effects, including but not limited to:

- I/O operations
- State management
- Exception handling
- Non-determinism
- Continuations
- Asynchronous programming

One of the main benefits of algebraic effects is that they allow for a high degree of modularity. Since effects are abstract and their implementations are provided by handlers, you can easily swap out or compose different handlers to change the behavior of your program. This makes it easier to test, refactor, and reason about your code.

Languages that support algebraic effects include Eff, Koka, and some experimental extensions to languages like OCaml. Additionally, there are libraries in languages like Haskell and JavaScript that provide similar functionality, often through the use of delimited continuations or other mechanisms.