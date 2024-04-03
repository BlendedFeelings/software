---
b: https://blendedfeelings.com/software/functional-programming/recursion.md
---

# Recursion in functional programming 
is a fundamental concept where a function calls itself to solve smaller instances of the same problem until it reaches a base case. This technique is often used in functional programming due to the absence of traditional looping constructs like `for` or `while` loops, which are common in imperative programming languages.

Functional programming languages favor recursion for several reasons:

1. **Immutability**: Functional programming often involves immutable data structures. Recursion naturally fits this model because it doesn't require changing the state of variables; instead, it passes the updated data to the next recursive call.

2. **Statelessness**: Recursion helps maintain statelessness, as each recursive call can be thought of as an independent computation with its own scope, without relying on or modifying external state.

3. **Expressions over Statements**: Functional programming languages emphasize expressions that return values rather than statements that change state. Recursive functions are expressions that return values based on their inputs and the results of their recursive calls.

4. **Higher-Order Functions**: Functional programming languages support higher-order functions, which can take other functions as arguments or return them as results. Recursive functions can be used as higher-order functions, providing a powerful abstraction mechanism.

5. **Tail Call Optimization**: Some functional languages implement tail call optimization (TCO), which allows recursive functions to be called without adding a new stack frame for each call. This optimization is crucial for making recursion practical for iterative processes that would otherwise consume too much stack space.

Here is a simple example of recursion in a functional programming language, using a function to calculate the factorial of a number:

```haskell
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

In this Haskell example, the `factorial` function calls itself with the argument `n - 1` until it reaches the base case `factorial 0`, which returns 1. The recursive calls build up until the base case is reached, and then the results are multiplied together as the call stack unwinds.

Recursion is a powerful tool in functional programming, but it must be used with care to avoid issues such as stack overflow, which can occur if the base case is not properly defined or if the recursion is too deep. Tail call optimization can help mitigate this risk in languages that support it.