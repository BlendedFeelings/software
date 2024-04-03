---
b: https://blendedfeelings.com/software/functional-programming/type-system.md
---

# Type systems in functional programming languages 
play a crucial role in ensuring the correctness of programs by detecting errors at compile time. A type system is a set of rules that assigns a property called a "type" to the various constructs in a language, such as variables, expressions, functions, or modules. These types can be used to enforce the correct usage of the constructs and to infer information about the code without having to execute it.

Here are some key aspects of type systems in functional programming:

1. **Static vs. Dynamic Typing**:
   - **Static typing**: The type of every expression is known at compile time. Examples of statically typed functional languages include Haskell, OCaml, and F#.
   - **Dynamic typing**: The type of expressions is determined at runtime. Clojure and older versions of Lisp are examples of dynamically typed functional languages.

2. **Type Inference**:
   - Many functional languages, especially those with static typing, have powerful type inference systems that can deduce the types of expressions without explicit type annotations from the programmer. For example, in Haskell, the type of a function can often be inferred from its implementation.

3. **Strong Typing**:
   - Strongly typed languages prevent mixing operations between mismatched types without explicit conversion. This reduces the likelihood of runtime errors due to type mismatches.

4. **Algebraic Data Types (ADTs)**:
   - Functional languages often support algebraic data types, which are a way of defining composite types. ADTs can represent complex data structures with a combination of "sum" types (variants or unions) and "product" types (tuples or records).

5. **Type Classes and Polymorphism**:
   - Type classes in languages like Haskell allow for ad-hoc polymorphism, where a function can operate on any type that satisfies a certain interface (set of functions). This is different from object-oriented polymorphism, as it is based on the behavior of the type rather than inheritance.

6. **Higher-Kinded Types**:
   - Some functional languages support higher-kinded types, which allow for the definition of operations that work on types that themselves take types as parameters (like generics in other languages, but more powerful).

7. **Dependent Types**:
   - A few languages, such as Idris and Agda, support dependent types, where types can depend on values. This allows for even more precise type checking and can encode invariants directly in the type system.

8. **Immutability and Type Systems**:
   - Functional programming often emphasizes immutability, and type systems can enforce this by preventing reassignment to variables or modification of data structures after creation.

9. **Effect Systems**:
   - Some languages have type systems that can track side effects, such as IO, state mutation, or exceptions. This helps in understanding where side effects occur in a program and in ensuring that pure and impure parts of the code are properly separated.

Type systems in functional programming can be quite sophisticated and contribute significantly to the reliability, maintainability, and safety of software. They allow developers to write expressive code while catching a large class of errors before the code is ever run.