---
b: https://blendedfeelings.com/software/testing/chaos-monkey.md
---

# Chaos Monkey 
is a service invented by Netflix that randomly terminates virtual machine instances and containers in a cloud environment to test the resilience and reliability of their system. It is one of the earliest and most well-known tools in the field of Chaos Engineering. The idea behind Chaos Monkey is to ensure that a system can withstand the loss of an instance without any significant impact on the customer experience.

Here's how Chaos Monkey works:

1. **Random Termination**: Chaos Monkey randomly selects servers or containers to shut down. The selection can be constrained to certain times of day, days of the week, or to specific services to minimize the impact on production traffic.

2. **Fault Injection**: By terminating instances, Chaos Monkey injects faults into the system, simulating failures that might occur naturally, such as hardware failures, network issues, or other unexpected disruptions.

3. **Validation of Redundancy and Failover**: The primary goal is to validate that the system's redundancy and failover mechanisms are effective. If an instance is terminated, the system should automatically reroute traffic or spin up new instances to handle the load.

4. **Continuous Testing**: Chaos Monkey runs continuously in the background, ensuring that the system is constantly being tested for weaknesses.

5. **Building Confidence**: Over time, the practice of regularly injecting faults into the system builds confidence that the system can handle unexpected disruptions gracefully.

6. **Improvement**: When Chaos Monkey exposes a weakness, the team can address it before it becomes a problem in a real-world scenario. This might involve improving the system's architecture, updating deployment practices, or enhancing monitoring and alerting systems.

Chaos Monkey is part of the larger Simian Army, a suite of tools developed by Netflix for stress-testing their infrastructure and services to identify weaknesses. These tools include Latency Monkey, Conformity Monkey, Doctor Monkey, and more, each designed to test different aspects of system resilience.

Chaos Monkey is open-source and can be adapted to fit different cloud environments and operational needs. It has inspired the development of other chaos engineering tools and practices, and it remains a key component in the toolbox of many DevOps and SRE (Site Reliability Engineering) teams focused on building robust and fault-tolerant systems.