---
b: https://blendedfeelings.com/software/dev-ops/continuous-delivery.md
---

# Continuous Delivery (CD) 
is a software development practice where code changes are automatically built, tested, and prepared for a release to production. It is an extension of continuous integration (CI), aiming to make releases much quicker and more frequent. This approach enables developers to ensure that software can be reliably released at any time, helping teams to reduce the time between conceiving an idea and making it available to users.

Here's a breakdown of the key principles and components of Continuous Delivery:

1. **Automated Testing**: CD relies heavily on automated testing to ensure that new code changes do not break any aspect of the application. This includes unit tests, integration tests, system tests, and acceptance tests.

2. **Build Automation**: The process of compiling code into binary artifacts (such as executables or libraries) is automated so that it can be done quickly and consistently.

3. **Environment Consistency**: CD requires maintaining consistent environments for development, testing, and production to reduce the chances of bugs caused by environmental differences.

4. **Deployment Automation**: The steps required to deploy the application are automated, allowing for frequent and reliable deployments with minimal human intervention.

5. **Version Control**: All production-ready artifacts are version-controlled, ensuring that any version of the software can be deployed at any time.

6. **Trunk-Based Development**: Developers work on a single branch (often called the 'trunk' or 'master'), which is always kept in a deployable state.

7. **Release Strategy**: CD doesn't necessarily mean that every change is released to users immediately. It means that every change is *releasable*, and the decision to release can be based on business strategy.

8. **Monitoring and Feedback**: Continuous monitoring of the system in production is essential to quickly identify any issues. Feedback from monitoring is used to improve the development and deployment processes.

The goal of Continuous Delivery is to make deployments predictable and routine affairs that can be performed on demand. By automating the build, test, and deployment processes, CD minimizes manual errors and provides a rapid feedback loop for developers. This leads to improved software quality and a more agile response to market changes or customer feedback.