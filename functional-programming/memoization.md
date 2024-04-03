---
b: https://blendedfeelings.com/software/functional-programming/memoization.md
---

# Memoization 
is a technique used in programming, often associated with functional programming, to optimize the performance of a function by caching its output for given input parameters. When a memoized function is called, it checks whether the result for the given inputs is already in the cache. If so, it returns the cached result instead of recomputing it. If not, the function computes the result, stores it in the cache, and then returns it.

This technique is particularly useful for functions that are called frequently with the same inputs, and where the computations are expensive.

While memoization is commonly used in functional programming due to its emphasis on pure functions (functions that return the same output for the same input and have no side effects), it is not exclusive to functional programming and can be used in other paradigms as well.

Here's an example of how you might implement a simple memoization function in JavaScript:

```javascript
const memoize = (fn) => {
  const cache = {};
  return (...args) => {
    const key = JSON.stringify(args);
    if (!cache[key]) {
      cache[key] = fn(...args);
    }
    return cache[key];
  };
};

// Example usage with a Fibonacci function
const fib = (n) => (n <= 1 ? n : fib(n - 1) + fib(n - 2));
const memoizedFib = memoize(fib);

console.log(memoizedFib(10)); // Computed once, then cached
console.log(memoizedFib(10)); // Retrieved from cache
```

In this example, the `memoize` function takes another function `fn` as an argument and returns a new function that, when called, caches the result of `fn` for a given set of arguments. The next time the function is called with the same arguments, the result is returned from the cache instead of being recomputed.