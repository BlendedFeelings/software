---
b: https://blendedfeelings.com/software/security/dynamic-application-security-testing-dast.md
---

# Dynamic Application Security Testing (DAST) 
is a security testing methodology that involves testing an application from the outside in by simulating cyber attacks against it. DAST is performed while the application is running (hence "dynamic") and is often referred to as black-box testing because the tester does not have access to the internal structure, design, or implementation of the application.

Key features of DAST include:

1. **External Testing**: DAST tools interact with an application through its front-end, just as a user or an attacker would. This means that DAST does not require access to the source code or the application's architecture.

2. **Simulated Attacks**: DAST tools simulate various types of attacks such as SQL injection, cross-site scripting (XSS), and other common vulnerabilities listed in the OWASP Top Ten.

3. **Real-time Analysis**: Since DAST tests the application in its running state, it can identify issues that only appear when a user is interacting with the application or when certain features are being executed.

4. **Platform Agnostic**: DAST tools are generally not dependent on the technology stack used to build the application. They can be used to test web applications, web services, and APIs regardless of the programming languages and frameworks.

5. **Automated Scanning**: Many DAST tools offer automated scanning capabilities, which can regularly scan the application for vulnerabilities without manual intervention.

6. **Late Stage Testing**: DAST is typically performed after an application has been deployed to a staging or production-like environment, which makes it suitable for catching issues that may not have been identified during earlier testing phases.

7. **Complementary to SAST**: DAST is often used in conjunction with Static Application Security Testing (SAST), which analyzes the source code for vulnerabilities. While SAST is performed early in the development lifecycle, DAST provides a safety net by identifying issues that manifest during the application's runtime.

8. **Reporting and Metrics**: DAST tools provide reports that detail the vulnerabilities discovered, their severity, and often include guidance on how to remediate them.

Challenges with DAST:

- **False Positives/Negatives**: DAST tools can generate false positives (reporting a vulnerability that doesn't exist) and false negatives (failing to detect an actual vulnerability).
- **Limited Coverage**: DAST cannot identify issues that are not exposed through the web interface, such as certain types of business logic errors.
- **Performance Impact**: Since DAST involves sending potentially harmful requests to the application, it can impact the performance of the application during testing.

DAST is an important part of a comprehensive application security program, providing a different perspective on application security by focusing on the application as an attacker would see it. It is most effective when integrated into a DevSecOps practice, where security testing is automated and integrated into the continuous integration and delivery pipeline.