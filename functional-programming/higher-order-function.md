---
b: https://blendedfeelings.com/software/functional-programming/higher-order-function.md
---

# Higher-order functions 
are a key concept in functional programming, and they refer to functions that can take other functions as arguments and/or return functions as their results. This allows for a more abstract and flexible way to structure programs, enabling code reuse and more concise expression of common programming patterns.

Here are some characteristics of higher-order functions:

1. **Accepts functions as arguments:** Higher-order functions can take one or more functions as parameters. This allows for a function to be applied to the items in a collection, or for a function to be used to determine if an element should be included in a result set.

2. **Returns functions as results:** Higher-order functions can return other functions as their result. This allows for the creation of functions that can be customized by the caller or for the creation of closures, which are functions that capture the environment in which they were created.

3. **Enables functional composition:** Higher-order functions can be used to compose other functions together. This means that the output of one function can be used as the input for another, creating a pipeline of functions that can process data in steps.

Some common examples of higher-order functions include:

- **Map:** Takes a function and a collection, and returns a new collection containing the result of applying the function to each element of the input collection.
- **Filter:** Takes a predicate function and a collection, and returns a new collection containing only the elements that satisfy the predicate.
- **Reduce (also known as fold):** Takes a function, a starting value, and a collection, and combines the elements of the collection into a single value using the function.
- **Compose:** Takes two or more functions and returns a new function that is the composition of those functions.
- **Curry:** Transforms a function that takes multiple arguments into a sequence of functions that each take a single argument.

In functional programming languages like Haskell, Scala, or in multi-paradigm languages like JavaScript and Python, higher-order functions are a fundamental part of the language and are used extensively to work with collections and to express complex logic in a succinct and readable manner.