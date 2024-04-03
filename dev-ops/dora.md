---
b: https://blendedfeelings.com/software/dev-ops/dora.md
---

# DORA (DevOps Research and Assessment) capabilities and practices 
are a set of metrics and principles that aim to measure the effectiveness of software development and delivery processes. They were developed by the DORA team, which was acquired by Google in 2018. The DORA team conducts annual research and publishes the "State of DevOps" reports, which provide insights into the best practices that lead to high performance in DevOps teams.

The DORA capabilities are divided into four key metrics, known as the "Four Key Metrics," which are used to measure the performance of software delivery:

1. **Deployment Frequency (DF):** This metric measures how often an organization successfully releases to production. High performers deploy more frequently, which allows for faster feedback and improvement.

2. **Lead Time for Changes (LT):** This metric measures the amount of time it takes for a commit to get into production. A shorter lead time is typically an indicator of a more efficient and responsive development process.

3. **Change Failure Rate (CFR):** This metric measures the percentage of deployments causing a failure in production. A lower change failure rate indicates better testing, quality assurance, and risk management practices.

4. **Time to Restore Service (TRS):** This metric measures how long it takes for a team to recover from a failure in production. A shorter time to restore service indicates a team's ability to quickly address and fix issues.

In addition to these metrics, the DORA team has identified several capabilities and practices that contribute to high performance in DevOps:

- **Continuous Integration:** Regularly merging code changes into a central repository, followed by automated builds and tests.

- **Continuous Delivery:** Ensuring that code can be safely deployed to production at any time.

- **Version Control:** All production artifacts, including code, configurations, and scripts, should be in version control.

- **Automated Testing:** Implementing automated testing to ensure that the software is always in a releasable state.

- **Trunk-Based Development:** Developers work on short-lived branches that are merged into a shared trunk frequently, avoiding long-lived feature branches.

- **Shift-Left on Security:** Integrating security practices early in the software development lifecycle.

- **Loosely Coupled Architecture:** Designing systems in a way that individual components or services can be updated independently of one another.

- **Empowered Teams:** Teams are given autonomy to make decisions about tools, processes, and architectures.

- **Monitoring and Observability:** Implementing comprehensive monitoring and observability to understand the state of systems and applications.

- **Proactive Notification and Incident Response:** Having processes in place to detect, notify, and respond to incidents in real-time.

- **Learning Culture:** Encouraging continuous learning, experimentation, and a blameless culture where failures are seen as opportunities to improve.

- **Streamlining Change Approval:** Moving away from manual change approvals to automated checks that provide confidence in the release process.

These capabilities and practices are not exhaustive, but they represent key areas that organizations can focus on to improve their DevOps performance and become more competitive in the market. The DORA team's research has shown that organizations that excel in these areas tend to outperform their peers in terms of both stability and velocity.