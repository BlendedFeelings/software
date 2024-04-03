---
b: https://blendedfeelings.com/software/dev-ops/rolling-deployment.md
---

# Rolling deployment 
is a software release strategy that staggers the deployment of a new version of an application across multiple phases, rather than updating all instances or servers simultaneously. This approach is commonly used in cloud computing and large-scale web services where high availability and minimal customer impact are crucial.

Here's how a rolling deployment typically works:

1. **Preparation**: The new version of the software is ready for deployment after thorough testing.

2. **Partial Deployment**: The update process starts with one or a small subset of servers or instances. This can also mean updating one server at a time in a cluster.

3. **Health Check**: After the update, the application on the updated instance is checked for proper operation. This includes running automated tests, monitoring performance, and ensuring that the new version is stable.

4. **Gradual Rollout**: If the updated instance passes the health check, the process is repeated with additional servers or instances, gradually rolling out the update across the entire infrastructure.

5. **Monitoring**: Throughout the deployment, the application is closely monitored for any issues. If any problems are detected, the deployment can be halted, and the system can be rolled back to the previous stable version.

6. **Completion**: Once all instances have been successfully updated and are running smoothly, the deployment is considered complete.

Advantages of rolling deployments include:

- **Reduced Risk**: By updating a few instances at a time, the risk of widespread issues is minimized. If a problem occurs, it affects only a small portion of the user base.
- **Continuous Availability**: There's no need to take the entire application offline, allowing users to continue using the service with minimal disruption.
- **Easy Rollback**: If the new version has issues, it's easier to rollback changes on a small number of servers than on the entire fleet.
- **Load Balancing**: The load balancer can divert traffic away from instances being updated, maintaining service performance.

However, rolling deployments also have some potential drawbacks:

- **Complexity**: They require more sophisticated deployment processes and monitoring systems.
- **Time-Consuming**: The deployment process is longer than if the update were done on all servers at once.
- **Consistency**: There can be a temporary inconsistency in the application's behavior if different servers are running different versions during the deployment.

Rolling deployments are facilitated by automation tools like Jenkins, Ansible, Kubernetes, and others, which help manage the complexities of the process.