---
b: https://blendedfeelings.com/software/testing/game-day.md
---

# GameDay 
is a term borrowed from sports to describe a type of resilience testing event. It's a day where the engineering team simulates failures in a system to test its reliability, fault tolerance, and recovery procedures. The idea is to create a controlled environment where the team can observe how the system behaves under stress or failure conditions and to validate that monitoring, alerting, and disaster recovery strategies work as expected.

During a GameDay, the team might:

1. **Plan Scenarios**: Decide on which parts of the system to test, such as databases, networks, or services.
2. **Simulate Outages**: Intentionally cause failures, such as shutting down servers, introducing network latency, or creating resource contention.
3. **Monitor and Observe**: Use monitoring tools to observe the system's behavior and the effectiveness of automated recovery processes.
4. **Document Findings**: Take notes on what works well and what doesn't, including how long it takes for the system to recover.
5. **Improve**: Use the insights gained to improve the system's resilience, such as by fixing bugs, updating runbooks, or improving monitoring and alerting.

GameDays are part of the Chaos Engineering practice, which is a discipline of experimenting on a system to build confidence in the system's capability to withstand turbulent and unexpected conditions. It's a proactive approach to identifying and fixing weaknesses before they lead to outages in production.

The term "GameDay" reflects the idea that, like in sports, the team is coming together to execute their skills under pressure, with the goal of improving their performance when it really counts.