---
b: https://blendedfeelings.com/software/dev-ops/forking-workflow.md
---

# Forking Workflow 
is a distributed workflow commonly used in collaborative software development, particularly when contributing to open-source projects. It is often seen in platforms like GitHub, where it allows multiple developers to work on a project without the need to coordinate closely. Here's an overview of how the Forking Workflow operates:

1. **Fork the Repository**: A developer creates a copy of the project repository by forking it on the hosting service (e.g., GitHub). This forked repository is owned by the developer and serves as their personal public workspace.

2. **Clone the Fork**: The developer clones their forked repository to their local machine. This gives them a private local workspace where they can make changes.

3. **Add the Original Repository as a Remote**: To keep their local copy up to date with the original project (often called the "upstream" repository), the developer adds it as a remote repository.

4. **Create a Feature Branch**: When starting work on a new feature or bug fix, the developer creates a new branch in their local repository. This isolates the work on the feature from other changes.

5. **Make Changes Locally**: The developer implements the changes on their feature branch and commits them to their local repository.

6. **Fetch the Latest Upstream Changes**: Before pushing their changes, the developer fetches the latest changes from the upstream repository to ensure that their branch is up to date.

7. **Rebase or Merge Upstream Changes**: The developer rebases or merges the upstream changes into their feature branch to ensure that there are no conflicts with the main project.

8. **Push Branch to Fork**: Once the local feature branch has the latest upstream changes and the new work, the developer pushes it to their forked repository.

9. **Create a Pull Request**: The developer creates a pull request (PR) from their feature branch in the forked repository to the main project. This is a request to the maintainers to review and potentially merge the changes.

10. **Code Review and Discussion**: Maintainers and other contributors review the PR, discuss changes, request modifications, and eventually approve the PR.

11. **Merge the Pull Request**: Once the PR is approved, a project maintainer merges the changes from the feature branch into the main project's repository.

12. **Pull and Sync Local Repository**: After their changes have been merged, the developer pulls the changes from the upstream repository to their local repository and syncs their fork as well.

13. **Clean up Feature Branches**: After the feature branch has been merged, it's often a good practice to delete the local and remote branches to keep the repository tidy.

The Forking Workflow is advantageous because it allows for a clean separation of work and reduces the risk of disrupting the main project. It's particularly useful when contributors do not have write access to the original repository. However, it can lead to a more complex history if not managed correctly, and it requires contributors to be diligent about keeping their forks up to date.