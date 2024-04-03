---
b: https://blendedfeelings.com/software/functional-programming/continuation-passing-style.md
---

# Continuation Passing Style (CPS) 
is a programming technique used in functional programming to manage control flow and handle asynchronous operations. In CPS, instead of a function returning a value directly, it takes an additional parameter called the continuation, which represents the rest of the computation. The function passes the result to the continuation instead of returning it.

Here's an example to illustrate how CPS works. Consider a simple function that adds two numbers:

```javascript
function add(a, b) {
  return a + b;
}
```

In CPS, the same function would be written as:

```javascript
function addCPS(a, b, cont) {
  cont(a + b);
}
```

In this example, the `addCPS` function takes three parameters: `a` and `b` are the numbers to be added, and `cont` is the continuation function that will receive the result. Instead of returning the result directly, `addCPS` calls the continuation with the sum of `a` and `b` as the argument.

CPS is particularly useful when dealing with asynchronous operations, such as callbacks or promises. By passing the continuation as a parameter, CPS allows for explicit control over the flow of execution and enables handling of asynchronous results in a more flexible and composable manner.

CPS can be used to implement control structures like `if-else` and loops, as well as to handle error handling and backtracking. It can also be combined with other functional programming techniques, such as currying and higher-order functions, to create powerful abstractions.

While CPS can provide benefits in terms of control flow and handling asynchronous operations, it can make code more complex and harder to read. It requires careful management of continuations and can lead to callback hell if not used judiciously. Therefore, it is important to weigh the trade-offs and consider the specific requirements of the application before adopting CPS as a programming technique.