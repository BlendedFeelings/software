---
b: https://blendedfeelings.com/software/dev-ops/andon.md
---

# Andon in the context of DevOps
an "Andon" system refers to a principle adapted from manufacturing that is aimed at bringing immediate attention to problems as they occur, so they can be promptly addressed. The term "Andon" originates from Japanese manufacturing systems, particularly the Toyota Production System, where it denotes a visual aid (like a light or a board) that signals the status of the production line, typically to indicate a problem at a specific station.

In software development, an Andon system is a metaphor for a process where any team member can raise a concern or report an issue that they believe is critical enough to require immediate attention or ask for help or opinion about a problem is facing. This could be a bug, a problem with the development environment, a failure in the build process, or anything else that impedes progress and threatens the quality of the product.

In software development and IT operations, an Andon system can be implemented as part of the DevOps culture to improve the continuous delivery pipeline. Here's how it works:

1. **Visibility**: The system provides real-time visibility into the health and status of the application, infrastructure, and delivery pipeline. This is often done through dashboards, monitoring tools, and alerting systems.

2. **Immediate Feedback**: When an issue arises, such as a failed build, a test failure, or a production incident, the Andon system alerts the relevant team members immediately. This feedback is crucial for quick response times.

3. **Empowerment**: Team members are empowered to "stop the line" or halt the deployment pipeline when a critical issue is detected. This is similar to a manufacturing worker pulling the Andon cord to stop production when a defect is found.

4. **Collaboration**: The system encourages collaboration among developers, QA engineers, and operations staff to investigate and resolve the issue as a team.

5. **Continuous Improvement**: After resolving the issue, teams perform a retrospective analysis to understand the root cause and implement improvements to prevent similar issues in the future.

Implementing an Andon system in DevOps requires a combination of cultural practices and technological solutions, such as:

- Continuous Integration/Continuous Deployment (CI/CD) tools that can be paused or stopped when issues are detected.
- Monitoring and alerting tools that can detect and communicate issues in real-time.
- Incident management practices that ensure quick and effective response to problems.
- A culture that values transparency, quick feedback, and continuous learning.

By adopting an Andon system, DevOps teams aim to reduce downtime, improve the quality of releases, and foster a culture of continuous improvement and rapid response to issues.