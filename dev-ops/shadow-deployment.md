---
b: https://blendedfeelings.com/software/dev-ops/shadow-deployment.md
---

# Shadow deployment 
is a technique used to test a new version of an application by deploying it alongside the existing version without directing real user traffic to it. The new version, often referred to as the "shadow" version, processes a copy of the live traffic in real-time. This approach allows the team to validate the new version's performance, stability, and behavior under actual workload conditions without affecting the user experience.

Here's how shadow deployment typically works:

1. **Deployment**: The new version of the application is deployed to the production environment but is not made visible or accessible to end-users.

2. **Traffic Duplication**: Traffic to the current production version of the application is mirrored or duplicated and sent to the shadow version as well. This means that for every real request processed by the production system, an identical request is sent to the shadow system.

3. **Monitoring and Analysis**: The shadow version processes the traffic in parallel with the production system, but the results are not used for actual user responses. Instead, the system logs are monitored for errors, performance metrics, and other indicators of the new version's behavior.

4. **Validation**: By comparing the shadow version's responses and behavior with the production version, developers can identify discrepancies, bugs, or performance issues that need to be addressed.

5. **No Impact on Users**: Since the shadow version does not serve responses to real users, any issues with the new deployment do not affect the user experience. Users continue to interact with the stable production version.

6. **Feedback Loop**: The insights gained from the shadow deployment are used to improve the application. If problems are detected, developers can work to resolve them without any pressure from impacting live users.

7. **Transition to Live Deployment**: Once the shadow version has been thoroughly tested and deemed stable, it can be transitioned to serve live user traffic, replacing the old production version.

The main advantages of shadow deployment are:

- **Risk Mitigation**: It significantly reduces the risk of introducing a faulty version to users since any issues can be caught and fixed before affecting the live environment.
- **Real-world Testing**: It provides an opportunity to test how the new version behaves under real traffic conditions without any fabricated or simulated scenarios.
- **Performance Benchmarking**: It allows for performance comparison between the new and current versions under identical conditions.

However, shadow deployment also has its challenges:

- **Resource Intensive**: It requires extra resources to run two versions of the application in parallel.
- **Complex Traffic Duplication**: Mirroring live traffic can be technically challenging and may require sophisticated networking and infrastructure capabilities.
- **Data Handling**: Care must be taken to handle sensitive data properly, ensuring that shadow processing does not result in data leaks or privacy breaches.

Shadow deployment is particularly useful in scenarios where the cost of a failure in the production environment is high, and thorough testing is crucial before fully releasing a new version to users.