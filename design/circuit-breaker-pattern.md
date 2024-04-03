---
b: https://blendedfeelings.com/software/design/circuit-breaker-pattern.md
---

# Circuit Breaker pattern 
is a design pattern used in software architecture to prevent a system from performing operations that are likely to fail. This pattern is particularly useful when dealing with remote services or inter-process communication. When these operations fail repeatedly, it can lead to system instability and cascading failures. The Circuit Breaker pattern helps to protect the system and manage failures gracefully.

Here's how the Circuit Breaker pattern works:

1. **Closed State**: Initially, the circuit breaker is in the "Closed" state, where operations are allowed to pass through to the service or operation being protected. The failures are counted by the circuit breaker.

2. **Open State**: When the number of failures reaches a predefined threshold within a certain time period, the circuit breaker trips, and it moves to the "Open" state. In this state, it blocks all attempts to perform the operation and usually returns an error or a fallback response immediately without executing the operation.

3. **Half-Open State**: After a predefined timeout period, the circuit breaker moves to the "Half-Open" state, where it allows a limited number of test requests to pass through. If these requests succeed, it indicates that the issue with the service has been resolved.

4. **Reset**: If the test requests in the "Half-Open" state are successful, the circuit breaker resets to the "Closed" state, and normal operation is resumed. If the test requests fail, the circuit breaker goes back to the "Open" state, and the timeout period begins again.

The Circuit Breaker pattern provides the following benefits:

- **Fault Tolerance**: It prevents an application from repeatedly trying to execute an operation that's likely to fail, thus protecting the system from unnecessary load and potential increased failure rates.
- **Fail Fast**: The pattern allows the system to detect failures quickly and stop making failing requests for a period, giving the faulting system time to recover.
- **Fallback Mechanisms**: It allows developers to provide alternative paths of execution when operations fail, which can improve user experience by not leaving the user waiting for a response that might never come.
- **System Recovery**: By isolating failures and giving the faulting system time to recover, the Circuit Breaker pattern helps to prevent the system from being overwhelmed, which can aid in recovery.

The Circuit Breaker pattern is often used in microservices architectures where it's common to have many services communicating over the network. It's also a key component in resilience engineering and is supported by many frameworks and libraries, such as Netflix's Hystrix, which provides an implementation of the pattern for Java applications.