---
b: https://blendedfeelings.com/software/functional-programming/pure-function.md
---

# Pure function in functional programming, 
is a deterministic function that always produces the same output for the same inputs and has no side effects. 

Function that has the following properties:

1. **Deterministic**: The output of the function is solely determined by its input values, without any observable side effects. This means that for the same inputs, a pure function will always produce the same output.

2. **No Side Effects**: A pure function does not cause any observable changes in the state of the system or interact with external mutable states. This means it doesn't alter any global variables, static variables, non-local variables, or perform I/O operations like reading from or writing to a console, files, or the web.

Here are some of the benefits of using pure functions:

- **Predictability**: Since the output is determined only by the input values, pure functions are highly predictable, making them easier to understand and debug.

- **Reusability**: Pure functions can be reused across different parts of a program or even in different programs.

- **Testability**: Pure functions are easy to test because they do not depend on any state or external context.

- **Parallelizability**: Since pure functions do not have side effects, they can be executed in parallel without the risk of race conditions or other concurrency issues.

- **Cachability/Memoization**: The results of pure functions can be cached and reused if the function is called again with the same inputs, which can improve performance.

Here is an example of a pure function in JavaScript:

```javascript
function add(a, b) {
  return a + b;
}
```

In this example, the `add` function is pure because it always returns the sum of `a` and `b` without causing any side effects. It is deterministic and has no side effects, satisfying the criteria for a pure function.