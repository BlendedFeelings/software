---
b: https://blendedfeelings.com/software/functional-programming/fold.md
---

# Fold 
is a higher-order function that processes a data structure (typically a list) in some order and builds a return value. A "left fold" (often called `foldl` in many functional languages) refers to a fold that processes the list from the left to the right, applying a function to an accumulator and each element of the list in turn.

The general form of a left fold function takes three arguments:
1. A binary function `f` that takes two arguments: an accumulator and an element from the list.
2. An initial value for the accumulator.
3. A list to process.

The fold function applies `f` to the initial value and the first element of the list to produce a new accumulator value, then applies `f` to this new accumulator value and the second element of the list, and so on, until the list is exhausted. The final value of the accumulator is the result of the fold.

Here's a simple example in Haskell, which has a built-in `foldl` function:

```haskell
-- Define a binary function that adds two numbers
add :: Int -> Int -> Int
add x y = x + y

-- Use foldl to sum a list of numbers
sumList :: [Int] -> Int
sumList xs = foldl add 0 xs

-- Example usage
main :: IO ()
main = print (sumList [1, 2, 3, 4, 5]) -- Outputs: 15
```

In the example above, `foldl` takes the `add` function, an initial accumulator value of `0`, and a list of integers. It then proceeds to add the numbers in the list from left to right, accumulating the sum, which is returned as the result.

In other languages, such as JavaScript, a left fold is typically called `reduce` and is a method on arrays:

```javascript
// Define a binary function that adds two numbers
function add(accumulator, value) {
  return accumulator + value;
}

// Use reduce to sum an array of numbers
const sumArray = [1, 2, 3, 4, 5].reduce(add, 0);

console.log(sumArray); // Outputs: 15
```

In this JavaScript example, `reduce` is used to sum the numbers in an array, starting with an initial accumulator value of `0`. The `add` function is applied to each element in the array from left to right.