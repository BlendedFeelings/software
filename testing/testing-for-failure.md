---
b: https://blendedfeelings.com/software/testing/testing-for-failure.md
---

# Testing for failure
often referred to as "Chaos Engineering," is a discipline in software engineering that involves experimenting on a software system in production in order to build confidence in the system's capability to withstand turbulent and unexpected conditions. Here are some methodologies and practices for testing for failure:

### Chaos Engineering

1. **Principles of Chaos**: Understand the principles of chaos engineering, which include defining 'steady state' conditions, hypothesizing that this steady state will continue in both the control group and the experimental group, introducing variables that reflect real-world events, and then trying to disprove the hypothesis.

2. **Chaos Monkey**: This is a tool developed by Netflix that randomly terminates instances in production to ensure that engineers implement their services to be resilient to instance failures.

3. **GameDays**: Organize events where the team intentionally induces failures in the system to test its resilience and the effectiveness of monitoring and alerting systems, as well as the team's incident response protocols.

### Fault Injection

4. **Fault Injection Testing**: Deliberately introduce faults into your system to see how it behaves. This can include things like killing processes, simulating network latency, or corrupting data.

5. **Simulating Outages**: Test how your system behaves under various outage scenarios, such as database downtime, loss of network connectivity, or failure of a third-party service.

### Load Testing

6. **Stress Testing**: Stress testing involves testing beyond normal operational capacity, often to a breaking point, in order to observe the results.

7. **Load Testing**: Perform tests to understand how your system behaves under heavy loads. This can help you identify bottlenecks and areas that need scaling.

### Other Testing Strategies

8. **Dependency Testing**: Test how your application handles the loss of external services it depends on. This can help you design better fallbacks and timeouts.

9. **Disaster Recovery Drills**: Run regular drills to ensure that your disaster recovery plans are effective and that the team is familiar with the procedures.

10. **Failover Testing**: Verify that your failover mechanisms (like database replicas or standby environments) work as expected.

11. **Backup and Restore Testing**: Regularly test your backup systems by performing actual data restores to ensure that your backup process works and that you can recover data when needed.

12. **Testing in Production**: While it might sound risky, testing in production is sometimes the best way to ensure that your system can handle failure in real-world conditions. This should be done with caution and monitoring.

13. **Canary Releases**: Gradually roll out changes to a small subset of users to ensure that new versions of your services are stable and do not introduce failures.

14. **Dark Launching**: Release features to production without exposing them to users. This allows you to test new features with production traffic without affecting user experience.

15. **A/B Testing**: Use A/B testing not just for user experience but also to test system stability and performance under different configurations or versions.

16. **Observability**: Enhance observability to include detailed logging, metrics, and tracing so that you can understand the state of the system and its failures in real-time.

By conducting these types of failure tests, you can identify weaknesses in your system, improve its resilience, and ensure that it can handle unexpected problems with minimal impact on the end-user experience.