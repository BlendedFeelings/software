---
b: https://blendedfeelings.com/software/programming-patterns/dependency-injection-pattern.md
---

# Dependency Injection Pattern
is a design pattern used in software development to achieve Inversion of Control (IoC) between classes and their dependencies. It allows for decoupling the creation of a class's dependencies from its behavior, which makes the system more modular, flexible, and testable.

Here's how it works:

**Dependency**: This is an object that another object depends on. For example, a service class might depend on a data access object to retrieve data from a database.

**Client**: This is the object that depends on the dependency. It requires the dependency to function properly.

**Injector**: This is the component that creates an instance of the dependency and injects it into the client. The injector can be a container (like in Spring Framework for Java) or it can be done manually in the code.

**Interface**: Dependencies are often defined by an interface or an abstract class that the concrete implementation will fulfill. This allows for the substitution of the dependency without changing the class that uses it.

There are several methods of dependency injection:

Constructor Injection: Dependencies are provided through a class constructor.
Setter Injection: Dependencies are provided through setter methods.
Interface Injection: Dependencies are provided through an interface that the client implements.

```java
// Define a class that requires a dependency
class MyClass {
  private MyDependency dependency;

  // Constructor that accepts the dependency
  public MyClass(MyDependency dependency) {
    this.dependency = dependency;
  }

  // Method that uses the dependency
  public void doSomething() {
    dependency.someMethod();
  }
}

// Define the dependency
class MyDependency {
  public void someMethod() {
    // Do something
  }
}

// Create an instance of the dependency
MyDependency dependency = new MyDependency();

// Create an instance of the class and pass in the dependency
MyClass myClass = new MyClass(dependency);

// Call the method on the class that uses the dependency
myClass.doSomething();

```