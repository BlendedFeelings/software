---
b: https://blendedfeelings.com/software/dev-ops/canary-releases.md
---

# Canary release 
is a strategy for rolling out updates to a small percentage of users before making them available to everybody. The term "canary" refers to the "canary in the coal mine" concept, where canaries were once used in coal mining as an early warning system for toxic gases. If the canary remained healthy, the environment was considered safe; if the canary showed signs of distress, it was a signal that conditions were unsafe.

Similarly, in software deployment, a canary release involves deploying a new version of an application to a small subset of users to test its stability and performance in a real-world environment. This subset of users acts as the "canary," and their experience is closely monitored to identify any potential issues with the release.

The main goals of canary releases are to:

1. **Detect issues early**: By exposing the new release to a limited audience, developers can identify and fix bugs before they affect the entire user base.
2. **Reduce risk**: By limiting the number of users affected by potential issues, the impact of any problems is minimized.
3. **Gather feedback**: Canary releases allow for the collection of user feedback and usage data, which can inform further improvements or fixes.
4. **Gradual rollout**: If the canary release proves to be stable, it can be gradually rolled out to more users, eventually reaching the entire user base.

Canary releases are often implemented as part of a continuous delivery or continuous deployment pipeline and can be facilitated by feature flags, traffic routing controls, and monitoring tools. They are particularly useful for web services and cloud-based applications where the service provider has control over the version of software that each user accesses.