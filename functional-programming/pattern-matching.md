---
b: https://blendedfeelings.com/software/functional-programming/pattern-matching.md
---

# Pattern matching 
is a powerful feature commonly found in functional programming languages that allows for a concise and expressive way to deconstruct and match data structures against patterns. It is a form of conditional branching which goes beyond simple comparisons and enables complex data manipulations based on the structure of the data. Here's an overview of how pattern matching works in functional programming:

1. **Deconstruction**: Pattern matching allows you to "deconstruct" or "unpack" data structures, such as lists, tuples, or custom types (like algebraic data types in Haskell or case classes in Scala), into their constituent parts.

2. **Matching Patterns**: When a data structure is matched against a pattern, the language runtime checks whether the structure fits the pattern. If it does, the runtime extracts the relevant parts of the data structure as specified by the pattern.

3. **Binding Variables**: Patterns can include variables that are bound to the corresponding parts of the data structure when a match is successful. These variables can then be used in the body of the pattern match.

4. **Guards**: Some languages allow for the use of guards in pattern matching. Guards are boolean expressions that provide an additional level of filtering by allowing a match to succeed only if the guard expression evaluates to true.

5. **Case Expressions**: Many functional languages use a `case` expression (or a similar construct) to facilitate pattern matching. A `case` expression evaluates an input expression and matches it against a series of patterns, executing the code associated with the first pattern that matches.

6. **Exhaustiveness**: Some languages enforce or encourage exhaustiveness in pattern matching, where all possible cases must be covered. This helps to avoid runtime errors due to unhandled cases.

7. **Wildcard Patterns**: A wildcard pattern, often represented by an underscore (`_`), matches any value, providing a way to specify a default case or to ignore certain parts of a data structure.

8. **Nested Patterns**: Patterns can be nested to match against complex or deeply nested data structures. This allows for very precise control over the data being matched.

9. **Algebraic Data Types (ADTs)**: In languages with ADTs, pattern matching is particularly powerful because it can match against the different constructors of an ADT, enabling very readable and declarative code for manipulating these types.

10. **First-class Patterns**: Some languages treat patterns as first-class citizens, allowing them to be passed around and manipulated like any other value.

Here's an example of pattern matching in Haskell, which has a very strong pattern matching system:

```haskell
data Fruit = Apple String | Banana | Cherry

describeFruit :: Fruit -> String
describeFruit fruit = case fruit of
    Apple variety -> "An apple of the " ++ variety ++ " variety."
    Banana        -> "A banana."
    Cherry        -> "A cherry."
    _             -> "Some other fruit."
```

In this example:

- The `Fruit` type is an algebraic data type with three constructors: `Apple`, `Banana`, and `Cherry`.
- The `describeFruit` function uses a `case` expression to match the input `fruit` against different patterns.
- Each pattern corresponds to one of the constructors of the `Fruit` type.
- The `Apple` pattern binds a variable `variety` to the string associated with the `Apple` constructor.
- The wildcard pattern `_` acts as a catch-all for any other `Fruit` value not explicitly matched.

Pattern matching is a feature that greatly enhances the readability and maintainability of functional programs, especially when dealing with complex data types. It reduces the need for verbose conditional statements and allows for more declarative and concise code.