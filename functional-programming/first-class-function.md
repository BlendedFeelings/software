---
b: https://blendedfeelings.com/software/functional-programming/first-class-function.md
---

# First-class functions in functional programming 
are a fundamental concept where functions are treated as first-class citizens. 

This means that functions can be:

1. **Passed as arguments to other functions:** You can treat functions just like any other data type, and pass them as parameters to other functions.

2. **Returned as values from other functions:** Functions can return other functions as their result, allowing for higher-order functions.

3. **Assigned to variables:** You can assign a function to a variable, store it in a data structure, or even have a function without a name (anonymous functions).

4. **Stored in data structures:** Functions can be elements of arrays, objects, or any other data structures.

Here's an example in JavaScript, which supports first-class functions:

```javascript
// A simple function that adds two numbers
function add(x, y) {
  return x + y;
}

// Assigning a function to a variable
const subtract = function(x, y) {
  return x - y;
};

// Passing a function as an argument to another function
function applyOperation(a, b, operation) {
  return operation(a, b);
}

// Using an anonymous function and storing it in an array
const operations = [
  add,
  subtract,
  function(x, y) { return x * y; },
  (x, y) => x / y // Arrow function syntax
];

// Using the applyOperation function
const result = applyOperation(5, 3, add); // result is 8

// Returning a function from another function
function createMultiplier(multiplier) {
  return function(x) {
    return x * multiplier;
  };
}

const double = createMultiplier(2);
const doubledValue = double(5); // doubledValue is 10
```

In this example, we see various ways in which functions are used as first-class citizens. This flexibility allows for powerful abstractions and compositional programming patterns.