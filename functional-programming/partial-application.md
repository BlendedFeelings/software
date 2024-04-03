---
b: https://blendedfeelings.com/software/functional-programming/partial-application.md
---

# Partial application 
is a concept in functional programming where you can take a function that accepts multiple arguments and fix a few of those arguments to create a new function. This new function then requires fewer arguments to be called. It's a way of creating a new function with some preset parameters.

Here's a simple example to illustrate partial application:

Suppose you have a function that adds two numbers together:

```python
def add(x, y):
    return x + y
```

Using partial application, you can create a new function where one of the parameters is already set. For example, you can create a function that always adds 5 to any number:

```python
from functools import partial

# Original function
def add(x, y):
    return x + y

# Create a new function with partial application
add_five = partial(add, 5)

# Now you can use add_five with only one parameter
print(add_five(10))  # Output: 15
```

In this case, `add_five` is a partially applied function of `add`, with the first parameter (`x`) fixed to 5.

Partial application is useful in many scenarios, such as when you have a function that is frequently called with the same argument(s), or when you want to pass a function as an argument to another function but need to fix some of the parameters ahead of time.

In many functional languages, partial application can be done more naturally. For example, in Haskell, you can partially apply functions just by providing fewer arguments than the function expects:

```haskell
add :: Int -> Int -> Int
add x y = x + y

addFive :: Int -> Int
addFive = add 5

main = print (addFive 10)  -- Output: 15
```

In this Haskell example, `addFive` is created by simply calling `add` with one argument. Haskell automatically creates a new function that takes the remaining arguments. This is possible because of Haskell's curried function definitions, where each function technically takes only one argument and returns a new function for the remaining arguments.