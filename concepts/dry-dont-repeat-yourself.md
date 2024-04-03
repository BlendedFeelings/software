---
b: https://blendedfeelings.com/software/concepts/dry-dont-repeat-yourself.md
---

# DRY (Don't Repeat Yourself) principle 
is a fundamental concept in software development that emphasizes the importance of reducing repetition within a codebase. It was popularized by Andy Hunt and Dave Thomas in their book "The Pragmatic Programmer". The principle states that "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system."

### Understanding DRY

The DRY principle is about avoiding duplication of code and knowledge in a system. When following DRY, you should strive to have a single source of truth for every piece of information in your application, which means:

- Avoiding the same code block in multiple places.
- Not repeating database schema definitions in SQL and code.
- Keeping business rules in a single place.
- Using constants or configuration files rather than hardcoding values in multiple locations.

The goal is to reduce the amount of redundant code, which can lead to fewer bugs, easier maintenance, and a more understandable codebase.

### Benefits of DRY

- **Easier Maintenance**: When a change is needed, it can be made in a single location rather than having to find and update duplicates throughout the codebase.
- **Reduced Bugs**: Duplication often leads to inconsistency over time as changes get applied to some instances but not others. DRY reduces this risk.
- **Improved Readability**: A codebase with less duplication is generally easier to read and understand.
- **Enhanced Reusability**: By centralizing code, you create reusable components, methods, or services that can be used across different parts of the application.

### Examples of DRY

1. **Functions and Methods**: If you find yourself writing the same algorithm or sequence of instructions in several places, you should encapsulate it in a function or method and call it from those places.

2. **Inheritance or Composition**: When multiple classes share common behavior, you can use inheritance or composition to encapsulate the shared functionality in one place.

3. **Configuration Files**: Instead of scattering configuration values (like API keys or database connection strings) throughout the code, they should be placed in a single configuration file or environment variables.

4. **Templates and Partials**: In web development, instead of repeating HTML structures, use templates and partials to define these structures once and include them where needed.

### Applying DRY

While DRY is a valuable principle, it's important to apply it judiciously. Overzealous application can lead to premature abstraction, which can make the code more complex and harder to understand. The goal should be to eliminate harmful duplication but not to remove duplication at the cost of increasing complexity or decreasing clarity.

In practice, DRY is balanced with other principles and considerations, like KISS (Keep It Simple, Stupid) and YAGNI (You Ain't Gonna Need It), to ensure that the codebase remains both dry and approachable.