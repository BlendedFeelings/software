---
b: https://blendedfeelings.com/software/testing/stress-testing.md
---

# Stress testing 
is a type of [non-functional testing](non-functional-testing.md) that involves evaluating how a system behaves under extreme conditions, often beyond its normal operational capacity. The goal is to identify the system's breaking point or the point at which it fails to function correctly. Stress testing is sometimes referred to as fatigue testing because it tests the system's ability to handle heavy loads for an extended period, which can cause the system to become fatigued and potentially fail.

### Objectives of Stress Testing:
- **Robustness**: To determine if the system can continue to operate under extreme conditions, even if not correctly.
- **Stability**: To ensure the system does not crash under unfavourable conditions and can recover gracefully once the load is reduced.
- **Data Integrity**: To verify that no data is lost or corrupted during periods of instability.
- **Error Handling**: To check how well the system reports and handles errors under stress.

### Types of Stress Testing:
- **Application Stress Testing**: Focusing on finding defects related to data locking and blocking, network issues, and performance bottlenecks within the application.
- **Systemic Stress Testing**: Testing the entire system's ability to handle stress, which may include multiple applications, databases, and hardware.
- **Distributed Stress Testing**: Testing across all clients and servers in a distributed network to identify network-related issues under stress.

### Process of Stress Testing:
1. **Planning**: Define the stress test goals, identify the key system metrics, and establish the stress test scenarios.
2. **Designing Test Cases**: Develop test cases that impose extreme conditions on the system, such as high loads, limited computational resources, or reduced network bandwidth.
3. **Setting Up the Test Environment**: Create an environment that allows for the monitoring and measurement of system performance under stress.
4. **Executing the Test**: Run the stress tests by gradually increasing the load or conditions until the system reaches its breaking point.
5. **Monitoring and Recording**: Continuously monitor the system's behaviour and record the results, noting when and how the system fails.
6. **Analysis**: Analyse the data to identify bottlenecks, resource limitations, and potential points of failure.
7. **Reporting**: Document the findings, including the conditions under which the system failed and any error messages that were generated.

### Tools Used in Stress Testing:
- **LoadRunner**: A widely used tool for performance and stress testing.
- **JMeter**: An open-source tool used for performance testing, including stress testing.
- **BlazeMeter**: A cloud-based load and performance testing service compatible with JMeter.
- **NeoLoad**: Another performance testing tool that includes stress testing capabilities.

### Importance of Stress Testing:
- **System Reliability**: Helps ensure that the system will not fail under extreme conditions, which is particularly important for critical applications.
- **Capacity Planning**: Provides insight into how much load the system can handle before it needs to be scaled up or optimized.
- **Disaster Recovery**: Helps in developing disaster recovery plans by understanding how the system fails and what is required for it to recover.
- **Performance Tuning**: Identifies the weakest parts of the system that need to be strengthened to improve overall performance and stability.

Stress testing is an essential part of the testing process for systems that are expected to function under high stress or for systems where failure can have serious consequences, such as in financial services, healthcare, and safety-critical systems. It helps to ensure that the system can sustain periods of heavy use without compromising data integrity or user experience.