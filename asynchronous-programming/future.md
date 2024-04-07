---
b: https://blendedfeelings.com/software/asynchronous-programming/future.md
---

# Futures 
also known as promises in some programming languages, are a core concept in asynchronous programming. They represent a placeholder for a result that is initially unknown but will become available at some point in the future. Futures allow a program to continue executing without blocking for the result of an asynchronous operation.

Here's a breakdown of how futures work and why they're useful in asynchronous programming:

### Concept of Futures:

1. **Placeholder for a Result**: A future is an object that acts as a proxy for a result that is not yet known, usually because the computation of that result is ongoing or has not yet begun.

2. **Asynchronous Operations**: Futures are often used in the context of I/O operations, network requests, or any long-running computations that would otherwise block the execution thread if performed synchronously.

3. **State**: A future can be in one of several states:
   - *Pending*: The operation has not yet completed.
   - *Fulfilled*: The operation has completed successfully, and the future holds the resulting value.
   - *Rejected*: The operation has failed, and the future holds information about the error.

4. **Callbacks**: Futures allow for callbacks to be attached that will be executed once the future is fulfilled or rejected. This way, you can define what should happen when the asynchronous operation succeeds or fails.

5. **Chaining**: Futures can be chained together, allowing for a sequence of asynchronous operations to be performed in a specific order without nesting callbacks (also known as "callback hell").

### Benefits of Futures:

- **Non-blocking**: Futures enable a program to perform other tasks while waiting for an asynchronous operation to complete.
- **Error Handling**: They provide a structured way to handle errors from asynchronous operations.
- **Composability**: Futures can be easily combined and chained, making it simpler to manage complex sequences of asynchronous operations.
- **Readability**: Code that uses futures is often easier to read and maintain than code with deeply nested callbacks.

### Examples in Programming Languages:

- **JavaScript**: Promises are the JavaScript implementation of futures. They are used extensively in modern JavaScript code for asynchronous operations.
  
  ```javascript
  const myPromise = new Promise((resolve, reject) => {
    // Asynchronous operation here
    if (/* operation successful */) {
      resolve(result);
    } else {
      reject(error);
    }
  });

  myPromise.then((result) => {
    console.log(result);
  }).catch((error) => {
    console.error(error);
  });
  ```

- **Python**: Python uses the `asyncio` module to work with futures, often referred to as "Tasks" or "Futures" within the context of the module.
  
  ```python
  import asyncio

  async def my_async_function():
      # Asynchronous operation here
      return result

  future = asyncio.ensure_future(my_async_function())
  # or using: future = asyncio.create_task(my_async_function())

  result = await future  # This retrieves the result once it's available
  ```

- **C#**: In C#, futures are represented by the `Task` class in the `System.Threading.Tasks` namespace.
  
  ```csharp
  using System.Threading.Tasks;

  public async Task<string> FetchDataAsync()
  {
      // Asynchronous operation here
      return "result";
  }

  // Usage
  var fetchDataTask = FetchDataAsync();
  var result = await fetchDataTask;
  ```

In all these examples, the future (or promise/task) represents the eventual completion (or failure) of the asynchronous operation and serves as a mechanism for writing clean, efficient, and maintainable asynchronous code.