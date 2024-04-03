---
b: https://blendedfeelings.com/software/design/resilience.md
---

# Resilience 
refers to the ability of a system to continue operating properly in the face of various types of failures or disruptions. This includes not only technical issues, such as hardware malfunctions or software bugs, but also external challenges like network outages, spikes in traffic, or malicious attacks. A resilient system is designed to handle these problems gracefully, maintain service continuity, and recover quickly.

Key aspects of resilience in software systems include:

1. **Redundancy**: Having multiple instances of critical components or services so that if one fails, others can take over without loss of service.

2. **Fault Tolerance**: The ability of a system to continue functioning even when some of its components fail. Fault-tolerant systems are designed to detect failures and reconfigure themselves without human intervention.

3. **Recovery Mechanisms**: Implementing strategies for data backup, state management, and recovery procedures to restore service after a failure.

4. **Graceful Degradation**: The ability of a system to reduce functionality in a controlled manner under stress or failure, while still providing service at a reduced level.

5. **Failover**: The automatic switching to a redundant or standby system upon the failure of the currently active system.

6. **Load Balancing**: Distributing workloads across multiple computing resources to ensure that no single resource is overwhelmed, which can help maintain performance under high load.

7. **Monitoring and Alerting**: Continuously monitoring the system to detect anomalies or performance issues early, and setting up alerting mechanisms to notify relevant personnel.

8. **Rate Limiting and Throttling**: Controlling the amount of incoming requests to prevent overloading the system and to prioritize critical workloads.

9. **Disaster Recovery Planning**: Preparing plans and procedures for recovering from catastrophic events, such as natural disasters or large-scale security breaches.

10. **Chaos Engineering**: Intentionally injecting faults into a system to test its resilience and to identify weaknesses that need to be addressed.

11. **Immutable Infrastructure**: Treating servers and other infrastructure components as disposable and easily replaceable, rather than trying to repair them.

12. **Self-Healing**: Implementing systems that can automatically detect and correct problems without human intervention.

13. **Dependency Isolation**: Minimizing dependencies between components or services to contain failures and prevent them from cascading through the system.

14. **Security**: Protecting the system from malicious attacks that could cause outages or data breaches.

To achieve resilience, software architects and engineers use a variety of architectural patterns and practices, such as microservices architecture, circuit breakers, bulkheads, and retry policies. These practices are often complemented by a culture that emphasizes learning from failures, continuous improvement, and proactive risk management.

Resilience is increasingly important as systems become more distributed, interconnected, and critical to business operations. Investing in resilience helps ensure that a system can withstand unexpected disruptions and continue to provide value to its users.