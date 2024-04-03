---
b: https://blendedfeelings.com/software/programming-patterns/inversion-of-control-ioc.md
---

# Inversion of Control (IoC)
is a design principle in software engineering that inverts the flow of control compared to traditional procedural programming. In traditional programming, the flow of the program's execution is determined by the application itself. However, with IoC, the flow of control is inverted so that external factors, such as a framework or a container, manage the program flow.

The main goal of IoC is to decouple the execution of a task from its implementation. It makes the system more modular, and easier to test, maintain, and extend. IoC can be achieved through various mechanisms, including but not limited to:

**Dependency Injection (DI)**: This is a form of IoC where objects are given their dependencies at creation time by some external entity that coordinates each object in the system. Instead of objects creating dependencies or asking a factory object to make them, they are passed (injected) into the object externally.

**Service Locator Pattern**: Instead of direct dependency injection, a service locator provides a mechanism to retrieve dependencies on demand. However, this pattern is generally considered less desirable than dependency injection because it can obscure a class's dependencies and make the system harder to understand and maintain.

**Event-driven Programming**: This is where the application flow is determined by events or messages. This can also be seen as a form of IoC, where the system reacts to events rather than the program dictating the order of execution.

**Template Method Pattern**: In this pattern, an abstract class will define the template of an algorithm, and the concrete implementations will invert the control by overriding the abstract methods defined by the template.

**Strategy Pattern**: This is where algorithms are passed into a context object as a parameter, allowing the client to change the algorithm without changing the context.

**Frameworks**: Many software frameworks use IoC to provide extensibility points where the user can hook their own code into the framework's workflow.

The benefits of IoC include:

**Loose Coupling**: Components are less dependent on the concrete implementations of other components, which promotes reusability and testability.
**Flexibility**: The system becomes more flexible as components can be replaced without requiring changes in the dependent components.
**Separation of Concerns**: It helps in separating the concerns of construction and use of objects, which is good for maintaining clean code architecture.
**Ease of Testing**: It is easier to test components in isolation when they are not tightly coupled to the rest of the system.

In summary, Inversion of Control is a powerful principle that, when used correctly, can greatly improve the design and maintainability of a software system. It is widely used in modern software development, especially in object-oriented programming.

```java
// Define a dependency interface
interface IMyDependency {
  void doSomething();
}

// Define a class that depends on IMyDependency
class MyClass {
  private IMyDependency myDependency;
  
  public MyClass(IMyDependency myDependency) {
    this.myDependency = myDependency;
  }
  
  public void run() {
    myDependency.doSomething();
  }
}

// Define a class that implements IMyDependency
class MyDependency implements IMyDependency {
  public void doSomething() {
    // do something here
  }
}

// Create an instance of MyDependency
MyDependency myDependency = new MyDependency();

// Create an instance of MyClass and pass in the instance of MyDependency
MyClass myClass = new MyClass(myDependency);

// Call the run() method on MyClass, which will call the doSomething() method on MyDependency
myClass.run();

```