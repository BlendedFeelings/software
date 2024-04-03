---
b: https://blendedfeelings.com/software/programming-patterns/middleware-pipelines-pattern.md
---

# Middleware Pipelines
refers to a design pattern where a request is processed through a sequence of middleware components before reaching the core application logic. Each middleware component can perform operations before and/or after the core application logic. This pattern is commonly used in web application frameworks to handle various aspects of request processing, such as authentication, logging, error handling, and data manipulation.

Here's a high-level overview of how middleware pipelines work:

**Request Handling**: An incoming request (e.g., HTTP request) enters the middleware pipeline.
**Middleware Components**: The request passes through a series of middleware components. Each middleware can:
- Inspect or modify the request.
- Decide whether to pass the request to the next middleware or halt the pipeline.
- Perform actions asynchronously or synchronously.
**Core Application Logic**: Once the request has passed through the necessary middleware, it reaches the core application logic (e.g., a controller in an MVC framework) where the primary processing occurs.
**Response Generation**: The core application generates a response.
**Response Handling**: The response travels back through the middleware pipeline, giving each middleware a chance to inspect or modify the response.
**Response Sent**: The final response is sent back to the client.
Middleware pipelines are often configurable, allowing developers to add, remove, or reorder middleware components to suit the needs of their application.

```js
// Define the middleware functions
function middleware1(request, next) {
  // Do something with the request
  // Call the next middleware function
  next(request);
}

function middleware2(request, next) {
  // Do something with the request
  // Call the next middleware function
  next(request);
}

function middleware3(request, next) {
  // Do something with the request
  // Call the next middleware function
  next(request);
}

// Define the pipeline
function pipeline(request) {
  middleware1(request, function(request) {
    middleware2(request, function(request) {
      middleware3(request, function(request) {
        // The pipeline is complete
        // Do something with the final request
      });
    });
  });
}

// Call the pipeline
pipeline(request);

```