---
b: https://blendedfeelings.com/software/dev-ops/gitflow-workflow.md
---

# Gitflow Workflow
is a branching model for Git, created by Vincent Driessen. It provides a robust framework for managing larger projects and is designed to provide a strict branching structure suited to collaboration and scaling the development team.

Gitflow's key features include:

1. **Main Branches**: 
   - `master`: The source of the code reflecting the production-ready state.
   - `develop`: The integration branch for features, fixes, and other branches in preparation for the next release.

2. **Supporting Branches**: 
   - `feature`: Branch off from `develop` and merge back into `develop`. Each new feature should reside in its own branch, which can be pushed to the central repository for backup/collaboration.
   - `release`: Branch off from `develop` and merge into both `develop` and `master`. This branch is for the next planned release and allows for final bug fixes and preparation for release.
   - `hotfix`: Branch off from `master` and merge back into both `master` and `develop`. These branches are for quick fixes to the production version.

The Gitflow process typically follows these steps:

1. A `develop` branch is created from `master`.
2. A `feature` branch is created from `develop` whenever new feature development is started.
3. When the feature is complete, it is merged back into `develop`.
4. When it's time to make a release, a `release` branch is created from `develop`.
5. Once the `release` branch is ready to be deployed to production, it is merged into `master` and tagged with a version number. Additionally, it should be merged back into `develop` to ensure that any changes made on the release branch are not lost.
6. If a critical bug is found in production, a `hotfix` branch is created from `master`. Once the fix is complete, it is merged into both `master` and `develop`.

Advantages of Gitflow:

- It provides a clear structure for managing releases, which can be particularly useful in a continuous delivery environment.
- It separates development work from released code, allowing for development to continue while a release is being prepared or a hotfix is being applied.
- It's well-suited for projects that have a scheduled release cycle.

Disadvantages of Gitflow:

- It can be complex and may involve more branching and merging than other workflows, which can be cumbersome for smaller teams or projects.
- It's not well-suited for continuous deployment environments where features are released to production as soon as they are ready.

While Gitflow is widely used, it's important to choose a branching strategy that fits the team's workflow and project requirements. Some teams may prefer simpler workflows, such as Trunk-Based Development, especially if they aim for continuous deployment and rapid iterations.