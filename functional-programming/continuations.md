---
b: https://blendedfeelings.com/software/functional-programming/continuations.md
---

# Continuations in functional programming 
are a way of structuring code such that the flow of control is explicitly managed. Instead of having the program execute in a direct style, where function calls result in the immediate execution of the called function, continuations allow the programmer to capture the "rest of the computation" at any given point, which can then be executed later. This makes continuations a powerful tool for implementing advanced control structures, such as coroutines, exceptions, backtracking, and concurrency.

Here's a basic explanation of how continuations work:

1. **Continuation**: A continuation represents the state of a program at a certain point in its execution. It is usually implemented as a function that, when called, will continue the execution from the point where it was created.

2. **Continuation-Passing Style (CPS)**: This is a style of programming where functions do not return values directly. Instead, they take an extra argument: a continuation function that represents the rest of the computation. When a function reaches a result, it passes this result to the continuation function instead of returning it.

3. **Capturing Continuations**: Some functional languages (like Scheme with its `call/cc` operator) allow programmers to capture the current continuation at any point in the program. This captured continuation can then be invoked later, effectively allowing the program to "jump back" to the point where the continuation was captured.

4. **Benefits**: Continuations can simplify the structure of code that performs complex control flows, such as error handling, asynchronous operations, and multi-threading. They can also be used to implement features like generators or coroutines in languages that do not natively support them.

5. **Example**: In Scheme, a simple example of using continuations with `call/cc` (call with current continuation) might look like this:

```scheme
(define (with-escape exit)
  (call/cc (lambda (k) (exit k)))
  (display "This line is executed normally.\n"))

(define (test)
  (with-escape
    (lambda (escape)
      (escape 'escaped) ; This will jump out of the with-escape function.
      (display "This line will not be executed.\n")))
  (display "Continuation after escape.\n"))

(test)
```

In this example, `with-escape` is a function that takes another function `exit` as an argument. Inside `with-escape`, `call/cc` is used to capture the current continuation and pass it to `exit`. When `escape` is called with `'escaped'`, the continuation is invoked, and the control jumps out of the `with-escape` function, skipping the second `display` and continuing with the third `display`.

Continuations are a deep and complex topic, and they can be quite difficult to grasp at first. They are less commonly used in day-to-day programming but are invaluable in certain domains and for certain problems.