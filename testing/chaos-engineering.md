---
b: https://blendedfeelings.com/software/testing/chaos-engineering.md
---

# Chaos Engineering 
is a discipline in software engineering that aims to improve system resilience by proactively introducing disturbances or stressors into a system to identify and fix weaknesses before they manifest as problems for users. It's often described as "breaking things on purpose" to learn how to build more robust systems. Here are some key components and practices associated with Chaos Engineering:

### Core Principles

1. **Define 'Steady State'**: A measurable output of a system that indicates normal behavior. Chaos Engineering experiments compare the steady state during and after introducing turbulence to determine the impact.

2. **Hypothesize**: Based on the steady state, hypothesize that the system will continue to operate normally in both the control group and the experimental group.

3. **Introduce Variables**: Introduce variables that reflect real-world events like server crashes, spikes in traffic, network latency, or data corruption.

4. **Run Experiments in Production**: To get the most accurate results, Chaos Engineering is often conducted in the live production environment, albeit with necessary precautions.

5. **Automate Experiments**: Automate the process of introducing chaos to ensure consistency and to allow for regular testing.

6. **Minimize Blast Radius**: Start with the smallest possible experiment to limit the impact and gradually increase the scope as confidence in the system's resilience grows.

### Practices

1. **Chaos Monkey**: Perhaps the most famous tool in Chaos Engineering, originally developed by Netflix. It randomly terminates instances in production to ensure that engineers implement their services to be resilient to instance failures.

2. **GameDays**: Scheduled events where teams proactively create disruptions and work together to address them in real-time.

3. **Fault Injection**: Deliberately introducing faults such as server crashes, API throttling, or database outages to observe how the system responds.

4. **Latency Injection**: Introducing delays in network communication to simulate outages or degraded performance.

5. **Chaos Toolkit**: An open-source toolkit that provides a way to perform chaos experiments against infrastructure, platforms, and applications.

6. **Gremlin**: A commercial tool that offers a more controlled platform for running chaos experiments.

### Benefits

1. **Resilience**: Identifying and fixing systemic weaknesses improves the overall resilience of the system.

2. **Confidence**: Regularly testing how the system behaves under failure conditions builds confidence in its stability and the effectiveness of monitoring and alerting systems.

3. **Performance**: Discovering and addressing bottlenecks can lead to performance improvements.

4. **Disaster Recovery**: Better preparation for unexpected disasters by having tested failure scenarios.

5. **Documentation**: Improved and updated documentation as a result of understanding the system through chaos experiments.

6. **Culture**: Fosters a culture of responsibility and awareness around reliability and system behavior.

### Challenges

1. **Risk**: There is inherent risk in intentionally causing system failures, especially in production environments.

2. **Buy-in**: Requires organizational buy-in to invest time and resources into potentially breaking a working system.

3. **Complexity**: Systems are complex, and it can be challenging to understand all the potential impacts of an experiment.

4. **Monitoring**: Requires robust monitoring and alerting to ensure that experiments do not cause unintended damage.

Chaos Engineering is not about causing random, unplanned outages, but about controlled and thoughtful experiments that lead to a more robust and resilient system. It's a practice that complements other testing and reliability practices and should be integrated into the development and operations lifecycle of a system.