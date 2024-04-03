---
b: https://blendedfeelings.com/software/functional-programming/function-currying.md
---

# Function currying 
is a concept in functional programming where a function with multiple arguments is decomposed into a sequence of functions, each with a single argument. In essence, currying transforms a function from callable as `f(a, b, c)` into callable as `f(a)(b)(c)`.

Currying is based on the mathematical concept of a curried function, named after the logician Haskell Curry. The idea is to partially apply a function - that is, to fix some number of arguments and produce a new function that only requires the remaining arguments.

Here's an example in JavaScript to illustrate currying:

```javascript
function add(a) {
  return function(b) {
    return a + b;
  };
}

const addFive = add(5); // This is a partial application
console.log(addFive(10)); // Outputs: 15
```

In this example, `add` is a curried function that takes one argument and returns a new function that takes the next argument. The function `addFive` is a partial application of `add`, where the first argument `a` is fixed to `5`. When `addFive` is called with `10`, it returns the sum of `5` and `10`, which is `15`.

Currying can be useful for creating more specific functions from general ones and can lead to more readable and maintainable code by minimizing repetition and making functions more modular.

Currying is a common feature in functional programming languages like Haskell, and it is also used in languages that support first-class functions, like JavaScript, Python, and Scala. In languages that do not natively support currying, it can be implemented manually by returning functions from functions, as shown in the example above.