---
b: https://blendedfeelings.com/software/functional-programming/parallelism.md
---

# Parallelism in functional programming 
refers to the ability to execute multiple computations or processes simultaneously, which can lead to better performance on multi-core processors. Functional programming languages are particularly well-suited for parallelism because of their emphasis on immutable data and stateless functions, which naturally avoid issues with shared mutable state that can complicate parallel programming in imperative languages.

Key concepts related to parallelism in functional programming include:

1. **Immutability**: Since functional programming often relies on immutable data structures, there is no need to worry about concurrent modifications to shared data, which can lead to race conditions in imperative programming.

2. **Pure Functions**: Functions in functional programming are generally pure, meaning they do not have side effects and do not rely on or modify any state outside their scope. This makes it easier to run functions in parallel since there's no need to manage dependencies between different parts of the code.

3. **Higher-Order Functions**: Functional programming languages typically provide higher-order functions like `map`, `filter`, and `reduce` that can be parallelized. For example, mapping a function over a collection can be done in parallel because each application of the function is independent of the others.

4. **Lazy Evaluation**: Some functional programming languages use lazy evaluation, which can help in creating efficient parallel programs. Lazy evaluation allows the creation of potentially infinite data structures and defers computation until the results are needed, which can be optimized for parallel execution.

5. **Task Parallelism and Data Parallelism**: Functional programming supports both task parallelism (executing different tasks in parallel) and data parallelism (executing the same task on different pieces of data in parallel).

6. **Functional Parallel Libraries**: Many functional programming languages provide libraries that abstract away the low-level details of parallel execution, allowing developers to write parallel code more easily.

In practice, parallelism in functional programming can be implemented in various ways, such as using parallel collections, parallel algorithms, and frameworks designed for concurrent and parallel execution. It's important to note that while functional programming can make parallelism easier to implement, developers still need to consider the overhead of parallel execution and ensure that the benefits of parallelism outweigh the costs for a given task.