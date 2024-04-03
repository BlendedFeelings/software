---
b: https://blendedfeelings.com/software/functional-programming/function-composition.md
---

# Function composition 
is a fundamental concept in functional programming. It refers to the process of combining two or more functions to create a new function. The output of one function becomes the input to the next, and so on. This allows for the creation of more complex functions by combining simpler ones.

In mathematical terms, if you have two functions \( f \) and \( g \), composing them would create a new function \( h \) such that \( h(x) = f(g(x)) \). The function \( g \) is applied to the input \( x \) first, and then the function \( f \) is applied to the result of \( g(x) \).

Here's a simple example in pseudocode to illustrate function composition:

```pseudocode
function f(x):
    return x + 2

function g(x):
    return x * 3

// Compose f and g to get a new function h
function h(x):
    return f(g(x))
```

In this example, the function \( h(x) \) first multiplies the input \( x \) by 3 using function \( g \), and then adds 2 to the result using function \( f \), effectively performing \( h(x) = (x * 3) + 2 \).

In many functional programming languages, there are operators or functions provided to compose functions more easily. For example, in Haskell, you can use the `.` operator to compose functions:

```haskell
f x = x + 2
g x = x * 3

-- Compose f and g to get a new function h
h = f . g
```

This would achieve the same result as the pseudocode example. When you call `h 5`, it would first compute `g 5`, which is `15`, and then apply `f` to `15`, resulting in `17`.

Function composition is a powerful technique because it promotes the creation of small, reusable, and testable functions that can be combined to solve complex problems. It also leads to code that is often more readable and maintainable.