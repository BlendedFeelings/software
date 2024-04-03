---
b: https://blendedfeelings.com/software/design/strangler-fig-pattern.md
---

# Strangler Fig pattern 
in software architecture is inspired by the way a strangler fig tree grows, which gradually envelops and strangles the host tree. In the context of software development, the Strangler Fig pattern is a strategy for handling the incremental replacement of a legacy system.

Here's how the Strangler Fig pattern typically works in software development:

1. **Identify the Legacy System:** The first step is to identify the legacy system that needs to be replaced or upgraded. This system is usually old, difficult to maintain, and unable to meet current requirements effectively.

2. **Create a Facade:** A facade is created to interface between the new and old systems. This facade intercepts calls to the legacy system and can redirect them to new implementations as they become available. The facade provides a consistent interface to clients, which means they do not need to be aware of the underlying changes.

3. **Incrementally Replace Functionality:** Instead of replacing the entire system at once, the functionality of the legacy system is gradually replaced with new implementations. Each piece of functionality is tackled one at a time, allowing for a controlled transition.

4. **Redirect through the Facade:** As new implementations are completed, the facade starts redirecting the calls related to that functionality to the new system. The old functionality can then be retired.

5. **Repeat Until Complete:** This process is repeated for each piece of functionality in the legacy system until the entire system has been replaced. Throughout this process, the system remains operational, reducing the risks associated with a big-bang replacement.

6. **Retire the Legacy System:** Once all functionality has been replaced and is being handled by the new system, the legacy system can be decommissioned.

The Strangler Fig pattern offers several advantages:

- **Risk Mitigation:** By replacing the system incrementally, the risk of a complete system failure or significant issues is reduced.
- **Continuous Delivery:** The new system can be delivered in stages, allowing for continuous improvement and delivery.
- **Feedback Loops:** Early stages of replacement can provide valuable feedback for the subsequent stages, helping to refine the approach.
- **Minimal Disruption:** The pattern aims to minimise disruption to the users and the business operations during the transition.

This pattern is particularly useful in scenarios where the legacy system is too complex or critical to be replaced all at once. It's a common approach in modernising software systems, especially when moving from monolithic architectures to microservices.