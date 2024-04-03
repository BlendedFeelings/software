---
b: https://blendedfeelings.com/software/functional-programming/monad.md
---

# Monads 
are a powerful and fundamental concept in functional programming. They are a type of abstract data type used to represent computations instead of data in the domain model. Monads can be thought of as a design pattern that allows for generic types, with certain operations defined that allow for the chaining of operations on the underlying type.

The purpose of monads is to provide a way to encapsulate values along with a context (such as possible failure, list of results, etc.) and to enable chaining operations on those values while maintaining the context.

Monads are defined by two operations and three laws:

### Operations:

1. **`bind`** (also known as `flatMap`, `>>=`, etc.): This operation takes a monadic value and a function that takes a normal value and returns a monadic value. It applies the function to the unwrapped value and then re-wraps the result into the monad. This allows for the chaining of monadic operations.

   Signature: `M a -> (a -> M b) -> M b`
   
   where `M` is the monad, and `a` and `b` are types.

2. **`return`** (also known as `unit`, `pure`, etc.): This operation takes a normal value and wraps it into the monad. It provides a way to lift a value into the monadic context.

   Signature: `a -> M a`

### Laws:

1. **Left identity**: `return` acts as a neutral element when used with `bind` on the left.

   Equation: `return a >>= f  ≡  f a`

2. **Right identity**: `return` acts as a neutral element when used with `bind` on the right.

   Equation: `m >>= return  ≡  m`
   
   where `m` is a monadic value.

3. **Associativity**: The order in which operations are performed does not matter when using `bind`.

   Equation: `(m >>= f) >>= g  ≡  m >>= (\x -> f x >>= g)`

### Examples of Monads:

- **Maybe Monad**: Represents computations which might fail. It has two possible values: `Just a` for a successful computation and `Nothing` for a failed one.

- **List Monad**: Represents computations with multiple possible results. The `bind` operation applies a function to each element of the list and concatenates the resulting lists.

- **IO Monad**: Represents side-effecting computations. It encapsulates an action that performs I/O and returns a value, ensuring that the order of I/O actions is maintained.

- **State Monad**: Represents stateful computations. It encapsulates a state transformation function and allows for state to be threaded through a sequence of computations.

Monads are not just a theoretical construct; they are widely used in functional programming languages like Haskell, Scala, and others to handle side effects, manage state, deal with asynchrony, and more. They help in writing clean, maintainable, and robust code.