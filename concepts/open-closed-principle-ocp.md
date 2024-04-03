---
b: https://blendedfeelings.com/software/concepts/open-closed-principle-ocp.md
---

# Open/Closed Principle (OCP) 
is the second of the five SOLID principles of object-oriented design, also introduced by Robert C. Martin. The principle states that software entities (such as classes, modules, functions, etc.) should be open for extension but closed for modification. This means that the behavior of a module can be extended without modifying its source code.

### Understanding OCP

The key idea behind the Open/Closed Principle is to write code that does not need to be changed every time the requirements change. Instead, you should be able to add new functionality by adding new code, not by changing old code that already works.

OCP has two parts:
- **Open for extension**: You should be able to extend or change the behaviors of a module or class by adding new code.
- **Closed for modification**: Extending the behavior of a module should not result in changes to the existing code of the module, which is already tested and in use.

### Examples of OCP

Imagine you have a system that processes different types of payments, such as credit card and PayPal payments. If you implement this system using a large `PaymentProcessor` class with multiple methods for each payment type, adding a new payment method would require modifying this class.

To adhere to OCP, you could instead define a common interface or abstract class for payment processing, like `IPaymentProcessor`, and then implement separate classes for each payment type, such as `CreditCardProcessor` and `PayPalProcessor`. When a new payment method needs to be added, you simply create a new class that implements the `IPaymentProcessor` interface, like `BitcoinProcessor`, without modifying the existing classes or interfaces.

### Applying OCP

To apply OCP, you can use various design patterns such as:

- **Strategy Pattern**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. The strategy pattern lets the algorithm vary independently from clients that use it.
- **Template Method Pattern**: Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
- **Decorator Pattern**: Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

By using these patterns, you can create systems that are more robust to changes because they allow you to add new functionality without altering the existing code, which reduces the risk of introducing new bugs.

In summary, the Open/Closed Principle encourages the development of systems that are easy to extend and maintain over time by minimizing the impact of changes and new features on existing code. It promotes the use of interfaces and abstract classes to provide a stable base that can be extended with concrete implementations.