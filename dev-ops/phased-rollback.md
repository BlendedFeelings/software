---
b: https://blendedfeelings.com/software/dev-ops/phased-rollback.md
---

# Phased rollback 
refers to the process of incrementally reverting a system or application to a previous version or state, typically after the detection of issues or problems with a recent update or release. Instead of rolling back the changes for all users at once, the rollback is done in phases to minimize impact and manage risk.

Here's how a phased rollback might be implemented:

1. **Detection of Issues**: The need for a rollback is usually triggered by the detection of critical bugs, performance issues, security vulnerabilities, or negative user feedback after a new software release.

2. **Planning**: The development and operations teams assess the situation to decide the extent of the rollback and the versions to which the system will be reverted. They also plan the phases, considering factors such as user segments, server regions, and feature sets.

3. **Preparation**: The team prepares the previous stable version of the software to be redeployed. This might involve code checks, database migrations, and ensuring compatibility with current data and systems.

4. **Initial Phase**: The rollback begins with a small segment of the user base or a limited environment. This allows the team to monitor the effects of the rollback and ensure that it resolves the issues without introducing new ones.

5. **Monitoring and Evaluation**: The team closely monitors the initial phase for any issues. If problems persist or new issues arise, they may need to halt the rollback and re-evaluate.

6. **Incremental Rollout**: If the initial phase is successful, the rollback is gradually extended to larger segments of the user base or additional environments, following the predefined phases.

7. **Final Phase**: Once all phases have been successfully rolled out and the system is stable, the rollback is complete. The entire user base should now be on the previous stable version.

8. **Post-Rollback Analysis**: After the rollback, the team analyses what went wrong with the update and implements measures to prevent similar issues in the future. This might involve improving testing procedures, updating deployment strategies, or revising the code.

Phased rollbacks are part of a broader set of strategies for safe deployment and maintenance of software systems, such as canary releases, blue-green deployments, and feature flags, which allow for more granular control over the release process and the ability to respond quickly to issues.