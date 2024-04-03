---
b: https://blendedfeelings.com/software/dev-ops/github-flow.md
---

# GitHub Flow 
is a lightweight, branch-based workflow that supports teams and projects where deployments are made regularly. It is centered around the idea of short-lived branches that facilitate continuous delivery. Here's how it generally works:

1. **Anything in the `main` branch is deployable.** The `main` branch is considered stable at all times. It reflects the production-ready state of your project.

2. **Create descriptive branches off of `main`.** When you start work on a new feature, fix, or experiment, you create a new branch off of `main`. The branch name should be descriptive so that others can see what is being worked on.

3. **Commit to that branch locally and regularly push your work to the same named branch on the server.** This not only backs up your work but also keeps others informed about the progress you're making.

4. **Open a pull request.** When you feel your branch is ready, or you want to discuss your work, you open a pull request. This is where the team can review the code, discuss it, and make further improvements.

5. **Discuss and review your code.** Team members can comment on the pull requests, approve them, request changes, or discuss the proposed changes.

6. **Deploy from the feature branch to a staging environment.** This allows you to test the changes in a production-like environment before merging into `main`.

7. **Merge to `main`.** Once your pull request has been reviewed and the branch passes your tests, you merge it into `main`.

8. **Deploy to production.** Once merged, you can deploy the changes from `main` to production, ensuring that you always have a deployable state.

9. **Keep your branch up to date with `main`.** While working on your feature, regularly rebase or merge the changes from `main` into your branch to keep it up to date and to avoid big merge conflicts later on.

10. **Once the branch is merged, it can be deleted.** After the feature branch has been successfully merged into `main` and deployed, it's no longer needed and can be safely deleted.

GitHub Flow is a very streamlined workflow that allows teams to deploy frequently. It is often compared to Git Flow, which is a more complex workflow that is better suited for projects with scheduled release cycles. GitHub Flow, by contrast, is optimized for teams that deliver changes continuously and value simplicity.