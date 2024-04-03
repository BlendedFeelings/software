---
b: https://blendedfeelings.com/software/programming-patterns/factory-method-pattern.md
---

# Factory Method Pattern
is a creational design pattern that defines an interface for creating an object but lets subclasses alter the type of objects that will be created. This pattern is particularly useful when a class cannot anticipate the class of objects it must create or when a class wants its subclasses to specify the objects it creates.

Here are some key points about the Factory Method Pattern:

**Creator**: The 'Creator' class is an abstract class that declares the factory method, which returns an object of a product class.

**Concrete Creator**: Subclasses of the Creator override the factory method to return an instance of a specific product.

**Product**: The 'Product' class defines the interface of objects the factory method creates.

**Concrete Product**: Subclasses of the Product implement the product interface. Concrete creators return an instance of these concrete products.

**Client**: The client code calls the factory method to create an object, but it is unaware of the concrete class of the object being created. The client works with the product through its interface.

```java
// Define the Product interface
interface Product {
    void operation();
}

// Define the ConcreteProduct classes
class ConcreteProductA implements Product {
    public void operation() {
        // Implementation of ConcreteProductA's operation
    }
}

class ConcreteProductB implements Product {
    public void operation() {
        // Implementation of ConcreteProductB's operation
    }
}

// Define the Creator abstract class
abstract class Creator {
    // Factory method that returns a Product object
    public abstract Product factoryMethod();

    // Method that uses the factory method to create a Product object
    public void someOperation() {
        Product product = factoryMethod();
        product.operation();
    }
}

// Define the ConcreteCreator classes
class ConcreteCreatorA extends Creator {
    // Implementation of ConcreteCreatorA's factoryMethod
    public Product factoryMethod() {
        return new ConcreteProductA();
    }
}

class ConcreteCreatorB extends Creator {
    // Implementation of ConcreteCreatorB's factoryMethod
    public Product factoryMethod() {
        return new ConcreteProductB();
    }
}

// Example usage
Creator creator = new ConcreteCreatorA();
creator.someOperation();

```