---
b: https://blendedfeelings.com/software/testing/security-testing.md
---

# Security testing 
is a type of [non-functional testing](non-functional-testing.md) that is a type of software testing that's focused on finding vulnerabilities, threats, and risks in software applications that could lead to a loss of information, revenue, reputation, or even legal issues for both the users and the organizations involved. The primary goal of security testing is to identify the weaknesses in the system so that they can be addressed before the software is released or becomes vulnerable to attack in a production environment.

### Objectives of Security Testing:
- **Confidentiality**: Ensuring that the information is accessible only to those authorized to have access.
- **Integrity**: Safeguarding the accuracy and completeness of information and processing methods.
- **Authentication**: Verifying that users are who they say they are and that each input arriving at the system came from a trusted source.
- **Authorization**: Ensuring that users have permission to access, modify, or delete the specific resources.
- **Availability**: Ensuring that the software, systems, and data are available when needed.
- **Non-repudiation**: Guaranteeing that the origin of a transaction cannot deny having participated in the transaction.

### Types of Security Testing:
- **Vulnerability Scanning**: Automated software scans a system against known vulnerability signatures.
- **Penetration Testing (Pen Testing)**: Simulation of an attack by a malicious hacker. The testing involves attempting to exploit system vulnerabilities, including OS, service and application flaws, improper configurations, and risky end-user behavior.
- **Security Auditing**: An internal inspection of applications and operating systems for security flaws. An audit can also be done via line-by-line code inspection.
- **Security Scanning**: Identifying network and system weaknesses, and later providing solutions for reducing these risks.
- **Ethical Hacking**: It's different from malicious hacking in that it's done with permission and as a part of a security assessment.
- **Risk Assessment**: Analyzing the security risks observed in the organization, which could be related to the entire system or specific parts. It involves the classification of assets, threats, and vulnerabilities.
- **Posture Assessment**: Combining security scanning, ethical hacking, and risk assessments to provide an overall security posture of an organization.

### Process of Security Testing:
1. **Test Planning**: Define the scope, objectives, and methods of the security testing.
2. **Gather Information**: Collect information about the system to understand how it operates and where there might be potential security gaps.
3. **Vulnerability Detection**: Use tools and techniques to identify known vulnerabilities.
4. **Exploitation**: Attempt to exploit the identified vulnerabilities to understand the potential impact.
5. **Analysis and Reporting**: Analyze the results of the exploitation to understand the severity of each issue and report the findings.
6. **Remediation**: Address the identified vulnerabilities by patching, configuration changes, or other mitigation measures.
7. **Retesting**: Verify that the vulnerabilities have been properly mitigated or resolved.

### Tools Used in Security Testing:
Many tools can help automate the process of security testing. Some of the widely used tools include:

- **OWASP ZAP**: An open-source web application security scanner.
- **Nessus**: A widely used vulnerability scanner.
- **Burp Suite**: An integrated platform for performing security testing of web applications.
- **Metasploit**: A tool for developing and executing exploit code against a remote target machine.

### Importance of Security Testing:
- Protects users' sensitive data from breaches.
- Helps in gaining trust from the customers and stakeholders.
- Ensures compliance with industry standards and regulations.
- Helps to avoid potential costs associated with a security breach, which can include legal consequences, loss of reputation, and financial losses.

Security testing is an ongoing process and should be integrated into the regular software development life cycle (SDLC) to ensure continuous security and compliance with the latest security best practices and standards. It is crucial in today's environment where security breaches are common and can have severe implications.