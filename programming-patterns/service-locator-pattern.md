---
b: https://blendedfeelings.com/software/programming-patterns/service-locator-pattern.md
---

# Service Locator Pattern
is a design pattern used in software development to improve the modularity of the application by decoupling the client classes from the concrete classes they depend on. Instead of instantiating the services directly, the client classes request them from a central location known as the Service Locator.

Here's an overview of how the Service Locator pattern works:

1. **Service Interface**: Defines the contract for the services that can be used by clients.

2. **Concrete Services**: Implementations of the service interfaces.

3. **Service Locator**: A central registry that knows how to instantiate and provide instances of the concrete services.

4. **Client**: The class that requires the services. It interacts with the Service Locator to obtain an instance of the service it needs.

The process typically follows these steps:

- A client needs a service and asks the Service Locator for it.
- The Service Locator either creates a new instance of the service or provides a cached one.
- The Service Locator returns the service instance to the client.
- The client uses the service as if it had created it directly.

The pattern can be beneficial in scenarios where:

- The application needs to be highly configurable.
- Services need to be swapped out at runtime.
- Dependency injection is not suitable or overkill for the project's needs.

However, the Service Locator pattern is sometimes considered an anti-pattern because it can obscure the actual dependencies of a class, making it harder to understand and maintain the code. It also makes it more difficult to manage the lifecycle of services and can lead to issues with service replacement and testing.



```java
// Define an interface for the service
interface IService {
  void doSomething();
}

// Define a concrete implementation of the service
class ServiceA implements IService {
  void doSomething() {
    // Implementation of the service
  }
}

// Define a Service Locator class
class ServiceLocator {
  private static Map<String, IService> services = new HashMap<String, IService>();

  // Register a service with the Service Locator
  public static void registerService(String serviceName, IService service) {
    services.put(serviceName, service);
  }

  // Retrieve a service from the Service Locator
  public static IService getService(String serviceName) {
    return services.get(serviceName);
  }
}

// Usage
ServiceLocator.registerService("ServiceA", new ServiceA())
IService service = ServiceLocator.getService("ServiceA");
service.doSomething();

```