---
b: https://blendedfeelings.com/software/dev-ops/trunk-based-development.md
---

# Trunk-Based Development (TBD) 
is a software development strategy where all developers commit their code changes to a single branch in the version control system, commonly known as the "trunk" or "main" branch. This approach emphasizes short-lived feature branches (if they are used at all), frequent commits, and continuous integration. The goal of TBD is to reduce the complexity of merging and integrating changes, thereby allowing for more frequent deployments and better collaboration among team members.

Here are some key principles of Trunk-Based Development:

1. **Single Source of Truth**: The trunk is the authoritative version of the codebase. All changes are integrated into this branch.

2. **Short-Lived Feature Branches**: If feature branches are used, they should be kept short-lived, typically no longer than a day or two, before they are merged back into the trunk.

3. **Frequent Commits**: Developers are encouraged to commit their changes to the trunk frequently, ideally multiple times a day. This reduces the risk of conflicts and makes integration easier.

4. **Continuous Integration**: With frequent commits, continuous integration (CI) is a must. Automated builds and tests are run with every commit to ensure that the trunk is always in a releasable state.

5. **Feature Toggles**: Instead of relying on long-lived branches to manage the release of new features, TBD often uses feature toggles (also known as feature flags) to control the visibility and activation of new features within the trunk.

6. **Team Collaboration**: TBD requires good communication and collaboration within the team to ensure that changes are integrated smoothly and that any potential conflicts or issues are resolved quickly.

7. **Release Readiness**: The code in the trunk should always be in a state that is ready to be released. This requires a strong emphasis on code quality, testing, and automation.

8. **No Code Freeze**: Since the trunk is always in a releasable state, there is no need for a code freeze period before a release. Teams can release at any time without a prolonged stabilization phase.

Implementing Trunk-Based Development typically involves the following practices:

- Version control system setup that supports the TBD workflow (e.g., Git)
- Automated testing and build pipelines
- Code review processes to maintain code quality
- Monitoring and alerting to quickly identify issues in production
- Adoption of DevOps culture and practices

TBD is often contrasted with Gitflow, another popular branching strategy that involves multiple long-lived branches for features, releases, and hotfixes. While Gitflow can be suitable for certain development workflows, Trunk-Based Development aims to streamline the process and accelerate the delivery of value to users.