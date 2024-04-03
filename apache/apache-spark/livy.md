---
b: https://blendedfeelings.com/software/apache/apache-spark/livy.md
---

# Livy 
is a service that enables easy interaction with a Spark cluster over a REST interface. It allows users to submit, run, and manage Apache Spark jobs and contexts from various client applications, including web applications, mobile apps, or other services. Livy is designed to be a RESTful middleware service of the Hadoop ecosystem and can be integrated with enterprise security and data governance policies.

Key features and concepts of Livy include:

1. **Interactive Sessions:**
   - Livy allows users to start interactive Spark sessions through its REST API. Once a session is created, users can submit code snippets (in Scala, Python, or R) to be executed interactively within that session.

2. **Batch Jobs:**
   - In addition to interactive sessions, Livy can also submit batch jobs to Spark. This is useful for running longer-lived data processing jobs. Users can submit a Spark job through the REST API and then poll for its completion or retrieve results.

3. **Job Submission:**
   - Livy provides a REST API endpoint for submitting Spark jobs. The job submission can include Spark configuration, file dependencies, and the code to execute.

4. **Session Management:**
   - Livy allows for the management of Spark sessions. Users can create new sessions, list existing sessions, retrieve the status of a session, and stop sessions through the REST API.

5. **Integration with Security:**
   - Livy can be integrated with Apache Hadoop's security model. It supports Kerberos authentication and can be configured to work with Hadoop's access control mechanisms.

6. **REST API:**
   - Livy's REST API is the primary interface for interacting with the service. The API provides endpoints for creating sessions, submitting jobs, checking job status, and retrieving results.

7. **Support for Multiple Languages:**
   - Livy supports executing code in multiple languages supported by Spark, including Scala, Python, and R.

8. **Cluster Support:**
   - Livy can run on clusters managed by YARN, Apache Mesos, Kubernetes, or in a standalone Spark cluster.

9. **State Preservation:**
   - Interactive sessions in Livy can preserve state between code snippets. This allows users to build up a data analysis step-by-step, maintaining variables and imported libraries across different submissions.

Livy simplifies the process of interacting with Spark from applications that may not be able to run Spark in their process or might be written in languages other than Java/Scala/Python/R. It is especially useful in environments where you want to provide a managed Spark service to multiple users or applications without requiring them to manage Spark contexts or sessions directly.