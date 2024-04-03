---
b: https://blendedfeelings.com/software/concepts/interface-segregation-principle-isp.md
---

# Interface Segregation Principle (ISP) 
is the fourth of the five SOLID principles of object-oriented design, and it was introduced by Robert C. Martin. ISP states that no client should be forced to depend on methods it does not use. This principle deals with the disadvantages of "fat" interfaces and encourages breaking them down into smaller, more specific ones.

### Understanding ISP

ISP suggests that when a class has a set of actions, and these actions are used by different clients in different ways, it's better to create separate interfaces for each group of actions rather than one general-purpose interface. This way, clients will only need to know about the methods that are of interest to them.

The principle aims to reduce the side effects and frequency of required changes by structuring software so that classes have the smallest possible interface that they require. This reduces the impact of changes and promotes a more decoupled and maintainable design.

### Examples of ISP

Imagine a multifunction printer that can print, scan, and fax. If you create a single interface `IMultiFunctionPrinter` with methods `Print()`, `Scan()`, and `Fax()`, any class that implements this interface would have to implement all three methods, even if it only needed the functionality of one.

This could lead to classes with empty method implementations for the functionality they don't need, which is a violation of ISP. To adhere to ISP, you could break down the `IMultiFunctionPrinter` interface into three separate interfaces: `IPrinter`, `IScanner`, and `IFax`. Then, classes could implement only the interfaces that correspond to the functionalities they require.

### Applying ISP

To apply ISP effectively, you should:

- Identify the distinct areas of functionality that clients use.
- Create focused interfaces that represent each distinct area of functionality.
- Implement these interfaces in your classes as needed.

This approach can lead to a system with a higher number of interfaces, but each interface has a clear purpose and is easier to understand and implement. It also makes the system more flexible and easier to refactor, as changes in one part of the system are less likely to affect unrelated areas.

In summary, the Interface Segregation Principle encourages a more fine-grained interface design to prevent classes from being forced to implement interfaces they don't use, thereby promoting a more maintainable and scalable codebase.