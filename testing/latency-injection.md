---
b: https://blendedfeelings.com/software/testing/latency-injection.md
---

# Latency injection 
is a specific type of fault injection where artificial delay is introduced into a system to simulate the effects of high network latency or slow processing. This technique is used to test how well a system performs under suboptimal conditions, such as slow network connections or overloaded servers, which can be common in real-world scenarios.

Here's how latency injection works and why it's useful:

1. **Simulating Slow Networks**: By injecting latency into network communications, you can simulate the experience of users on slow or unreliable connections. This helps ensure that the system remains responsive and usable even under less-than-ideal conditions.

2. **Testing Timeouts and Retries**: Introducing delays can help test whether timeout values are set appropriately and whether retry mechanisms are functioning correctly. It can uncover issues where operations might fail or degrade the user experience due to unexpected delays.

3. **Evaluating Performance**: Latency injection can help identify performance bottlenecks in the system that only become apparent under stress. It can also validate that load balancing and scaling mechanisms kick in as expected when parts of the system are slow.

4. **Ensuring Resilience**: By intentionally slowing down services, you can test the resilience of the system as a whole. It can reveal hidden dependencies or single points of failure that might not be evident during normal operation.

5. **Verifying SLAs**: Service Level Agreements (SLAs) often include performance guarantees. Latency injection can be used to ensure that the system can meet these guarantees even when facing adverse conditions.

6. **Improving User Experience**: Understanding how latency affects user experience can lead to improvements in the frontend, such as better feedback mechanisms (e.g., loading indicators) or more efficient data fetching and caching strategies.

Latency injection can be implemented in various ways, such as:

- **Middleware**: Adding middleware to web services that intentionally delays responses.
- **Proxy**: Using a proxy server to intercept and delay traffic between services.
- **Network Configuration**: Configuring network devices to introduce latency, packet loss, or bandwidth restrictions.
- **Application Code**: Modifying application code to add sleep statements or other mechanisms to delay processing.

Tools for Chaos Engineering, like Gremlin or Chaos Monkey for Spring Boot, often include features for latency injection. This allows teams to automate the process and integrate it into their regular testing and reliability practices. Latency injection is typically conducted in a controlled environment to prevent negative impacts on real users, although it can also be carefully applied in production environments as part of a comprehensive Chaos Engineering strategy.