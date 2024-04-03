---
b: https://blendedfeelings.com/software/design/graceful-degradation.md
---

# Graceful degradation 
is a design philosophy aimed at allowing a system to continue operating with reduced functionality when some of its components fail or are unavailable. The primary goal is to ensure that the system can still deliver a useful service, albeit possibly at a reduced level of performance or with limited features, rather than failing completely. This approach is particularly important for systems where availability and user experience are critical.

Here are some key aspects of graceful degradation:

1. **Prioritization of Features**: Identify which features are critical to the system's core functionality and ensure that these are the last to be affected by degradation. Non-critical features can be disabled first in response to failures.

2. **Modular Design**: Design the system in a modular way so that if one module fails, it does not necessarily affect the operation of other modules. This can help contain failures and minimize their impact.

3. **Fallback Mechanisms**: Implement fallback options for when preferred methods fail. For example, if a system normally relies on real-time data but that data feed fails, it could switch to using the last known good data or a simplified estimation algorithm.

4. **User Communication**: Inform users of any reduction in service quality or functionality. Clear communication can help manage user expectations and reduce frustration.

5. **Robust Error Handling**: Ensure that the system can handle errors gracefully, without crashing. This may involve catching exceptions and providing meaningful error messages or alternative options to users.

6. **Performance Scaling**: In cases of high load, the system might temporarily disable certain resource-intensive features to maintain overall responsiveness.

7. **State Management**: Maintain system state in such a way that if a process is interrupted, it can be resumed or safely terminated without data loss.

8. **Resource Conservation**: Implement measures to conserve resources (e.g., bandwidth, memory, processing power) when the system detects that it is under stress.

9. **Testing**: Regularly test the system's ability to degrade gracefully under various failure scenarios. This helps ensure that the degradation strategies work as intended.

10. **Simplification**: In some cases, offering a simplified version of the service that requires fewer resources and has fewer dependencies can ensure that the system remains operational.

Graceful degradation is often implemented alongside its counterpart, "progressive enhancement," which is the practice of building a basic, functional core and then adding enhancements if the environment supports them. Together, these strategies help create a more resilient and user-friendly system.

In practice, implementing graceful degradation requires careful planning and consideration of how different parts of the system interact, as well as an understanding of the user experience under various conditions. It's a balance between maintaining service quality and managing the complexity and cost of the additional safeguards.