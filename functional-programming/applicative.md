---
b: https://blendedfeelings.com/software/functional-programming/applicative.md
---

# Applicative pattern 
is a concept in functional programming. It refers to a type of functor that allows for functions that take multiple arguments to be applied within a context, such as a list, an optional value, or a computational effect like IO or State. Applicatives are a generalization of monads, providing a way to sequence computations and combine their results.

The key feature of an applicative functor is that it provides an `apply` operation (often denoted as `<*>` in Haskell) that takes a functor that contains a function and another functor that contains a value, and applies the function to the value within the context of the functor.

Here's a simple example in Haskell syntax to illustrate the concept:

```haskell
-- Suppose we have two functions, add and multiply
add :: Int -> Int -> Int
add x y = x + y

multiply :: Int -> Int -> Int
multiply x y = x * y

-- We have applicative functors containing values
maybeX :: Maybe Int
maybeX = Just 10

maybeY :: Maybe Int
maybeY = Just 5

-- We can use the applicative pattern to apply functions to these values
resultAdd :: Maybe Int
resultAdd = add <$> maybeX <*> maybeY  -- Just (10 + 5)

resultMultiply :: Maybe Int
resultMultiply = multiply <$> maybeX <*> maybeY  -- Just (10 * 5)
```

In the example above, `<$>` is the infix notation for `fmap` (the functor map operation), which applies a function to the value inside a functor. `<*>` is the applicative apply operation, which takes a functor containing a function and a functor containing a value and applies the function to the value.

Applicative functors are useful because they allow for function application in contexts where values might not be directly accessible (e.g., within a `Maybe` type that could also be `Nothing`, or within a list that could have multiple values), without having to manually handle the context. They also provide a way to deal with multiple arguments in a clean and composable manner.