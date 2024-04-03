---
b: https://blendedfeelings.com/software/functional-programming/immutability.md
---

# Immutability in functional programming 
refers to the concept that data should not be changed once it has been created. Instead of modifying existing data structures, functional programming encourages the creation of new data structures with the desired changes. This approach is fundamental to functional programming paradigms and has several benefits:

1. **Predictability**: Since data cannot be altered, it's easier to understand and predict the behavior of programs because the state is not subject to change outside of its scope.

2. **No Side Effects**: Functions in functional programming are designed to be pure, meaning they do not cause any side effects outside of their scope. This includes not altering any data structures. With immutability, it's easier to maintain this purity.

3. **Concurrency**: Immutability is very beneficial in concurrent programming. Since data cannot be changed, there's no need for locks or synchronization mechanisms typically required to prevent race conditions in mutable state environments.

4. **Easier to Reason About**: Code that utilizes immutable data is often easier to reason about and can be more straightforward to debug. Each function's output is dependent only on its inputs and not on any external state.

5. **Undo/Redo Functionality**: Immutability makes it simple to implement undo/redo functionality because you can keep previous versions of the data structure without worrying about them being changed.

6. **Referential Transparency**: Functions always return the same output for the same input, which is a principle known as referential transparency. This concept is closely related to immutability because it relies on data not changing.

In many functional programming languages, immutability is enforced by the language itself. For example, in Haskell, all values are immutable by default. In languages where immutability is not enforced, such as JavaScript, it is a practice that developers can choose to follow to gain the benefits listed above.

Here is an example of how immutability might be applied in a functional language like Haskell:

```haskell
-- A simple immutable data structure
data Point = Point Int Int deriving (Show)

-- A function that "changes" the x value of a point
-- by creating a new point with the new value
shiftX :: Point -> Int -> Point
shiftX (Point _ y) newX = Point newX y

-- Usage
let p1 = Point 10 20
let p2 = shiftX p1 15
```

In this example, `shiftX` does not modify the original `Point` (`p1`); instead, it returns a new `Point` (`p2`) with the updated x value. The original `Point` remains unchanged, demonstrating immutability.