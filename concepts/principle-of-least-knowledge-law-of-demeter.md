---
b: https://blendedfeelings.com/software/concepts/principle-of-least-knowledge-law-of-demeter.md
---

# Principle of Least Knowledge 
also known as the Law of Demeter, is a design guideline for developing software, particularly object-oriented programs. The principle aims to promote loose coupling between software components, which can lead to more maintainable and adaptable code.

Here are the key concepts of the Principle of Least Knowledge / Law of Demeter:

1. **Minimize Object Interaction**: Each unit of software (like a class) should only have limited knowledge about other units. It should only interact with closely-related units.

2. **Only Talk to Your Friends**: Objects should only call methods on:
   - Themselves
   - Objects passed in as parameters
   - Any objects they create/instantiate
   - Their own component objects (objects held in instance variables)

3. **Don't Talk to Strangers**: Objects should avoid calling methods on objects returned from other calls (avoid "train wrecks" - `a.getB().getC().doSomething()`).

4. **Use Only One Dot**: This is a simplification of the rule, meaning that when coding, each line should only have one "dot". For example, `getAddress().getZipcode()` would violate this rule.

The Law of Demeter is not a law in the strict sense but a guideline to reduce dependencies between classes or modules. By following this principle, changes to one part of the system are less likely to require changes in other parts, and the overall system becomes more modular and easier to understand. However, it's also important to apply this principle judiciously, as overzealous application can lead to overly complex designs with too many wrapper classes or methods that add little value.