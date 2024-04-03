---
b: https://blendedfeelings.com/software/dev-ops/cold-deployment.md
---

# Cold deployment 
refers to the traditional method of deploying new software or updates to a production environment where the existing application or service is taken offline (made "cold") during the deployment process. This is in contrast to modern deployment strategies like rolling updates, blue-green deployment, or canary releases, which aim to minimize downtime and provide a seamless user experience.

Here's how cold deployment typically works:

1. **Downtime Planning**: A maintenance window is scheduled during which the service will be unavailable to users. This window is often chosen based on times of lowest user activity to minimize the impact.

2. **Service Shutdown**: The current running version of the application or service is shut down. This means that the system will not be available to handle user requests during this period.

3. **Deployment**: The new version of the software is deployed to the server or servers. This might involve steps like installing new software packages, updating configuration files, running database migrations, or applying patches.

4. **Testing**: Once the new version is deployed, it is tested to ensure that it is functioning correctly in the production environment. This might be a quick smoke test or a more thorough set of tests, depending on the complexity of the deployment and the changes made.

5. **Service Restart**: If the tests pass, the service is restarted, and the new version becomes available to users.

6. **Monitoring**: After the application is back online, it is closely monitored to ensure that it is performing as expected and that no new issues have arisen as a result of the deployment.

Cold deployments have several disadvantages compared to more modern techniques, including:

- **Downtime**: Users are unable to access the service during the deployment, which can lead to a poor user experience and potential loss of business.
- **Risk**: If issues arise with the new deployment, they can cause extended downtime as the problems are diagnosed and fixed.
- **Resource Intensive**: Cold deployments can require more planning and coordination since they impact service availability.

Due to these drawbacks, cold deployments are less common in environments where high availability is crucial. However, they may still be used in certain scenarios, such as when dealing with legacy systems that cannot support more advanced deployment strategies, or when the deployment changes are so significant that a complete shutdown is necessary to apply them safely.