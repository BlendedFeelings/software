---
b: https://blendedfeelings.com/software/functional-programming/lazy-evaluation.md
---

# Lazy evaluation 
also known as call-by-need, is an evaluation strategy which delays the evaluation of an expression until its value is needed. It is a feature often found in functional programming languages, such as Haskell. Lazy evaluation can improve the program's performance by avoiding unnecessary calculations, and it can also enable the creation of data structures that can be computed on demand and can potentially be infinite in size.

Here's how lazy evaluation works in functional programming:

1. **Deferred Computation**: When an expression is encountered, instead of evaluating it immediately, the language creates a promise to compute the expression when needed. This promise is often represented as a thunk, which is a parameterless function that encapsulates the expression.

2. **Caching Results**: When the value of an expression is finally needed (for example, to display the result, to perform a conditional test, etc.), the thunk is invoked, and the expression is evaluated. The result is then cached, so if the value is needed again, the cached result is used instead of re-evaluating the expression.

3. **Infinite Data Structures**: Lazy evaluation allows the creation of infinite data structures like streams or lists. These structures can be defined recursively, but only the part of the structure that is actually consumed is evaluated. For example, you can define an infinite list of all natural numbers, but if you only need the first ten, only those ten will be computed.

4. **Control Structures**: Some control structures can benefit from lazy evaluation. For example, in a non-strict `if` statement, only the branch that is selected based on the condition is evaluated. This can prevent unnecessary or even erroneous computations in the branch that is not selected.

5. **Modularity**: Lazy evaluation can lead to more modular code. Functions can return more general results without concern for performance penalties, as the cost of evaluating the result is only incurred when necessary.

Here's an example of lazy evaluation in Haskell, which is a purely functional programming language that uses lazy evaluation by default:

```haskell
-- A lazy list of all natural numbers starting from n
naturalsFrom n = n : naturalsFrom (n + 1)

-- Take the first 10 natural numbers from the list starting with 1
take 10 (naturalsFrom 1)
-- Output: [1,2,3,4,5,6,7,8,9,10]
```

In this Haskell code, `naturalsFrom` defines an infinite list of natural numbers starting from any given number `n`. The `take` function is then used to get the first 10 numbers from this list. Despite `naturalsFrom` being capable of producing an infinite list, only the first 10 numbers are computed because of lazy evaluation.

Lazy evaluation can lead to unexpected behavior if not used carefully, especially when dealing with side effects or I/O operations. However, when used properly, it is a powerful tool that can lead to more efficient and expressive programs.