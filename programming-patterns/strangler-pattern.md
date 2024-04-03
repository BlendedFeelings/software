---
b: https://blendedfeelings.com/software/programming-patterns/strangler-pattern.md
---

# Strangler Pattern
is a software development process that gradually replaces a legacy system by building a new system around it, piece by piece. The term was coined by Martin Fowler and the pattern is named after the strangler fig, which grows around other trees, eventually replacing them.

The idea is to incrementally replace specific pieces of functionality with new applications and services. This approach allows developers to work on a new system without the need to fully understand the complexities of the old system. Over time, the new system will "strangle" the old one, taking over its responsibilities until the old system can be decommissioned.

Here's how the Strangler Pattern typically works:

1. **Identify**: Determine the areas of the legacy system that are candidates for replacement. These could be modules or features that are in need of updating or that would benefit from being redeveloped with modern technology.

2. **Intercept**: Create a facade or an intermediary layer that intercepts calls to the old system. This facade will direct some of the traffic to the new system as new features are developed.

3. **Incremental Replacement**: Gradually build the new system around the old, replacing one piece of functionality at a time. During this phase, some calls will go to the old system and some to the new, depending on what has been replaced.

4. **Decommission**: Once all functionality has been replaced by the new system, the old system can be turned off.

The benefits of the Strangler Pattern include:

- **Risk Reduction**: By replacing the system incrementally, you reduce the risk associated with big-bang replacements.
- **Continuous Delivery**: It allows for continuous delivery and integration of new features without disrupting the existing system.
- **Learning**: Developers learn about the system as they go, which can be easier than understanding the entire system at once.
- **Legacy System Uptime**: The legacy system remains operational throughout the process, ensuring that business operations are not affected.

The Strangler Pattern is particularly useful in complex, high-risk, or critical systems where a direct cut-over from old to new is not feasible. It is a common approach in modernising legacy systems, especially when moving to a microservices architecture.

```java
// Define the legacy application
class LegacyApplication {
  void processRequest(request) {
    // Process the request using the legacy code
    return legacyCode.process(request);
  }
}

// Define the new application
class NewApplication {
  void processRequest(request) {
    // Process the request using the new code
    return newCode.process(request);
  }
}

// Define the strangler application
class StranglerApplication {
  // Create instances of the legacy and new applications
  legacyApp = new LegacyApplication();
  newApp = new NewApplication();

  function processRequest(request) {
    // Check if the request can be processed by the new application
    if (newApp.canProcess(request)) {
      // Process the request using the new application
      return newApp.process(request);
    } else {
      // Process the request using the legacy application
      return legacyApp.process(request);
    }
  }
}

```