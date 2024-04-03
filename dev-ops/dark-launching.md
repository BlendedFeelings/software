---
b: https://blendedfeelings.com/software/dev-ops/dark-launching.md
---

# Dark launching 
is a deployment strategy used to release new features or services to production without exposing them to end-users. This technique allows developers to test new functionalities under real-world conditions with actual production traffic, but without affecting the user experience. The term "dark" refers to the fact that the feature is "in the dark" or hidden from the users' view.

Here's how dark launching typically works:

1. **Code Deployment**: The new feature is coded behind feature toggles (also known as feature flags) and deployed into the production environment as part of the application, but it remains disabled.

2. **Selective Activation**: The feature can be selectively enabled for certain users, user groups, or internal testers without making it available to the entire user base. This can be controlled through configuration settings or the feature toggle system.

3. **Monitoring**: While the feature is dark launched, developers monitor the system for any issues such as performance degradation, errors, or bugs. They can also assess the impact on system resources and gather data on how the feature behaves in a live environment.

4. **Gradual Rollout**: Once confident in the feature's stability and performance, developers can gradually enable the feature for more users. This incremental approach allows for careful monitoring of the feature's impact as it becomes more widely used.

5. **Full Release**: After a successful dark launch phase, the feature can be fully released to all users, becoming a visible and active part of the application.

6. **Rollback**: If any issues are detected during the dark launch, developers can quickly disable the feature without needing to deploy new code or rollback the entire application.

The main advantages of dark launching are:

- **Risk Reduction**: By testing features in production without affecting all users, the risk of widespread issues is minimized.
- **Real-world Feedback**: Developers can observe how features perform under actual usage conditions, which can be different from test environments.
- **User Experience**: The user experience remains uninterrupted during the testing phase, as users are not exposed to potentially unstable features.
- **Gradual Exposure**: It allows for a controlled and gradual exposure of the feature to the user base, which can be helpful for managing load and user education.

However, dark launching also comes with its challenges:

- **Complexity**: Implementing feature toggles and managing configurations for dark launching can add complexity to the codebase and deployment processes.
- **Resource Overhead**: Running additional features, even in the dark, may consume more resources and require careful capacity planning.
- **Data Integrity**: Ensuring that dark launched features do not interfere with user data or application state is crucial.

Dark launching is particularly useful for large-scale web applications and services where new features can significantly impact the system and user experience. It provides a safe way to validate new functionalities and gather performance data before a full public rollout.