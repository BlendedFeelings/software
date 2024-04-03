---
b: https://blendedfeelings.com/software/programming-patterns/promise-pattern.md
---

# Promise Pattern
 is a software design pattern often used in asynchronous programming, particularly in languages like JavaScript. It represents a proxy for a value that may not be known when the promise is created. This allows for asynchronous methods to return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise of having a value at some point in the future.

Here’s a basic outline of how the Promise pattern works:

1. **Creation**: A new promise is created with the `new Promise()` constructor, which is provided with a function that takes two arguments: `resolve` and `reject`.
   - `resolve(value)` is called when the async operation completes successfully, and the promise's value becomes the provided `value`.
   - `reject(error)` is called if the operation fails, and the promise is rejected with the provided `error`.

2. **Pending State**: Initially, the promise is in a pending state, which means the async operation it represents has not completed yet.

3. **Settlement**: The promise can be settled in two ways:
   - **Fulfilled**: If the operation completes successfully, the promise is fulfilled, and any functions waiting for its value are executed.
   - **Rejected**: If the operation fails or encounters an error, the promise is rejected, and any error handling functions are executed.

4. **Consumption**: Other parts of the code can register functions to handle the value from the promise (using `.then()`) or to handle a possible error (using `.catch()`). The `.finally()` method can be used to run code regardless of the outcome.

```javascript
const myPromise = new Promise((resolve, reject) => {
  // Perform some asynchronous operation
  // If successful, call the resolve function with the result
  // If unsuccessful, call the reject function with the reason for the failure
});

```