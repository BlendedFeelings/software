---
b: https://blendedfeelings.com/software/refactoring/code-refactoring.md
---

# Code refactoring 
is the process of restructuring existing computer code—changing the factoring—without changing its external behavior. Refactoring is intended to improve nonfunctional attributes of the software. Advantages include improved code readability and reduced complexity; these can improve the source code's maintainability and create a more expressive internal architecture or object model to improve extensibility.

Here are some common code refactoring techniques:

1. **Extract Method**: Identify code fragments that can be grouped together, move them into a new method, and replace the old code with a call to the method. This improves readability and reuse.

2. **Inline Method**: Replace a method call with the method content when the method is not complex and is only called in one place, to reduce unnecessary indirection.

3. **Rename Method**: Change the name of a method when the name does not clearly describe what the method does.

4. **Replace Temp with Query**: Replace a temporary variable with a method call, particularly if the variable is only assigned to once and is not modified afterwards.

5. **Introduce Explaining Variable**: Use a descriptive variable to explain the purpose of a complex expression. This can make the code more readable.

6. **Split Temporary Variable**: Avoid using the same temporary variable for multiple purposes, which can be confusing.

7. **Remove Assignments to Parameters**: Instead of changing the value of a parameter, use a temporary variable. This prevents unexpected behavior from changes to parameters.

8. **Replace Method with Method Object**: Convert a method into a separate class where the local variables become instance variables of the new class. This is useful for long methods with complex algorithms and many local variables.

9. **Decompose Conditional**: Break down complex conditional logic into smaller, more manageable methods to improve clarity.

10. **Consolidate Conditional Expression**: Combine multiple conditions that result in the same action into a single conditional expression.

11. **Consolidate Duplicate Conditional Fragments**: Move code that is the same out of conditional statements.

12. **Remove Control Flag**: Replace a control flag (a variable that directs the flow of control) with break or return statements to simplify the logic.

13. **Replace Type Code with Subclasses/State/Strategy**: Replace type code with a proper subclass or a state/strategy pattern to avoid conditional logic based on a type code.

14. **Replace Nested Conditional with Guard Clauses**: Use guard clauses for special cases and then let the "normal" case follow without nesting.

15. **Extract Class**: If a class is doing too much work, create a new class and move the relevant fields and methods from the old class into the new class.

16. **Inline Class**: If a class is no longer doing enough to justify its existence, merge it with another class.

17. **Hide Delegate**: Instead of allowing a client to call a delegate class directly, provide a method in the server class to hide the delegate.

18. **Remove Middle Man**: If a class is doing little more than delegating to another class, remove the middleman and let clients call the final class directly.

19. **Introduce Foreign Method**: If you need a method on a class that you can't modify, create a method in your own class that takes an instance of the other class as an argument.

20. **Introduce Local Extension**: If you need to add several methods to a third-party class, create a new class that contains these extra methods and make it either a subclass or a wrapper of the third-party class.

Refactoring should be done carefully, ideally with the support of a comprehensive suite of automated tests to ensure that no existing functionality is broken during the process.