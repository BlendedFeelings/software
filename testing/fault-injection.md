---
b: https://blendedfeelings.com/software/testing/fault-injection.md
---

# Fault injection 
is a testing technique used to evaluate the robustness of a system by deliberately introducing faults to see how the system behaves under such conditions. It's an essential part of both Chaos Engineering and more traditional testing approaches. The purpose of fault injection is to mimic operational failures and observe how well a system can cope with them.

Fault injection can be applied at various levels of the system:

1. **Hardware Level**: Introducing faults into hardware components like CPUs, memory, or I/O devices to simulate hardware failures.

2. **Software Level**: Injecting bugs or errors into the software to test error-handling code paths, such as exceptions or error messages.

3. **Network Level**: Simulating network issues such as high latency, packet loss, or disconnections to test the system's ability to handle network instability.

4. **System Level**: Manipulating system resources like CPU, memory, and disk space to create resource contention and test the system's response to resource exhaustion.

5. **Application Level**: Disrupting application processes, such as terminating processes or introducing delays in execution to validate the resilience of application-level fault tolerance.

The goals of fault injection include:

- **Identifying Weaknesses**: Discovering areas where the system does not handle failure gracefully.
- **Validating Assumptions**: Ensuring that the system behaves as expected under failure scenarios, based on its design and assumptions.
- **Improving Reliability**: Using the findings from fault injection tests to improve system reliability through code enhancements, better error handling, and improved architecture.
- **Ensuring Failover**: Testing that failover mechanisms and redundancy systems work as intended when parts of the system fail.
- **Increasing Confidence**: Building confidence in the system's ability to operate correctly in the presence of faults, which is especially important for critical systems.

Fault injection can be performed manually by engineers or automatically using tools designed for Chaos Engineering, such as Chaos Monkey or Gremlin. It is often carried out in a controlled environment, such as a staging area, but can also be done in production with the necessary precautions to minimize potential impact on users.