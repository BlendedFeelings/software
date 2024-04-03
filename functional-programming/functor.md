---
b: https://blendedfeelings.com/software/functional-programming/functor.md
---

# Functor 
in functional programming is a type of abstraction that allows you to map a function over or apply a function to values wrapped in a context, without having to unwrap the values from that context. Functors are typically represented as data types that implement a specific interface or contract, often with a method commonly named `map`.

The `map` function is a key characteristic of a functor. It takes a function and a functor, applies the function to the functor's value(s), and returns a new functor with the transformed value(s). This process does not alter the original functor; instead, it creates a new functor with the new value(s).

The concept of a functor comes from category theory in mathematics, where it refers to a mapping between categories that preserves the structure of the categories. In programming, it's a way to work with values in a context (like a container or a computational effect) in a consistent and composable way.

Here is the basic structure of a functor in pseudo-code:

```pseudo
interface Functor<T> {
    // map applies a function to the value(s) contained in the functor
    // and returns a new functor with the result.
    map<U>(f: (T) -> U): Functor<U>
}
```

In this interface, `T` represents the type of value contained in the functor, and `U` represents the type of value returned by the function `f` that is applied to `T`. The `map` method takes a function `f` and returns a new functor containing values of type `U`.

A simple example of a functor is a list or an array. When you apply a function to each element of the list using `map`, you get back a new list with each element transformed by the function, but the structure of the list (i.e., being a list) remains the same.

Here's an example in JavaScript, which has built-in support for functors with its array type:

```javascript
const numbers = [1, 2, 3, 4];
const increment = (x) => x + 1;

const incrementedNumbers = numbers.map(increment);
console.log(incrementedNumbers); // Output: [2, 3, 4, 5]
```

In this example, the array `numbers` is a functor, and the `map` method applies the `increment` function to each element of the array, resulting in a new array with each element incremented by 1.