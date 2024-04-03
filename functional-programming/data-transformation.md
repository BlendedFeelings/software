---
b: https://blendedfeelings.com/software/functional-programming/data-transformation.md
---

# Data transformation in functional programming 
refers to the process of converting data from one format or structure to another using functions. Functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. This approach to data transformation is characterized by the use of pure functions, immutability, and higher-order functions.

Here are some key concepts related to data transformation in functional programming:

1. **Pure Functions**: These are functions that, given the same input, will always return the same output and do not have any side effects (e.g., modifying external variables or state).

2. **Immutability**: Data is not changed in place; instead, transformations produce new data structures without altering the original ones.

3. **Higher-Order Functions**: These are functions that can take other functions as arguments or return them as results. They are often used to abstract common patterns of data transformation.

4. **First-Class Functions**: Functions are treated as first-class citizens, meaning they can be assigned to variables, passed as arguments, or returned from other functions.

5. **Map, Filter, Reduce**: These are common higher-order functions used for data transformation:
   - `map`: Applies a function to each element in a collection and returns a new collection containing the results.
   - `filter`: Creates a new collection containing only the elements that satisfy a predicate function.
   - `reduce` (also known as `fold`): Combines the elements of a collection using a function to produce a single value.

6. **Recursion**: Many functional programming languages use recursion as a primary means for iteration, since traditional loops can imply mutable state.

7. **Lazy Evaluation**: This is an evaluation strategy which delays the computation of expressions until their value is needed. It can help in optimizing programs and dealing with infinite data structures.

8. **Pattern Matching**: A mechanism for checking a value against a pattern. It is a more powerful version of the switch statement seen in many other languages.

Here's a simple example of data transformation using these concepts in functional programming, written in JavaScript:

```javascript
// A pure function that adds two numbers
const add = (x, y) => x + y;

// A pure function that doubles a number
const double = (x) => x * 2;

// An immutable list of numbers
const numbers = [1, 2, 3, 4, 5];

// Transforming data with map, filter, and reduce
const transformedData = numbers
  .map(double) // [2, 4, 6, 8, 10]
  .filter((x) => x > 5) // [6, 8, 10]
  .reduce(add, 0); // 24

console.log(transformedData); // Outputs: 24
```

In this example, the `map` function is used to double each number, `filter` is used to select numbers greater than 5, and `reduce` is used to sum all the numbers in the resulting array. Each step returns a new array without modifying the original `numbers` array, showcasing immutability.