---
b: https://blendedfeelings.com/software/dev-ops/three-ways.md
---

# DevOps "Three Ways" 
is a set of principles that guide practices in DevOps, which is a cultural and professional movement that stresses communication, collaboration, integration, and automation in order to improve the flow of work between software developers and IT operations professionals. The Three Ways provide a framework for thinking about how to improve systems and processes. They were introduced by Gene Kim in the book "The Phoenix Project" and later expanded upon in "The DevOps Handbook."

1. The First Way: Flow/Systems Thinking
    emphasizes the performance of the entire system over the performance of individual components or silos. This principle is about understanding and improving the entire value stream from the initial concept to the customer. It requires seeing the big picture and optimizing for the global goals rather than local goals.

    Key aspects of the First Way include:

    - **End-to-end Perspective**: Viewing the entire software delivery process as a single system, from development to operations to delivery, rather than as disjointed stages.

    - **Work-in-Progress (WIP) Limits**: Limiting the amount of work in progress to reduce multitasking and context switching, which can improve focus and throughput.

    - **Reducing Handoffs**: Minimizing the number of times work has to be handed off between different teams or individuals, which can introduce delays and errors.

    - **Amplifying Feedback Loops**: Ensuring that feedback from later stages of the process is used to improve earlier stages, creating a more responsive and adaptive system.

    - **Continuous Delivery**: Automating the build, test, and deployment processes to enable a steady and sustainable flow of work from development to production.

    - **Build Quality In**: Incorporating quality assurance practices throughout the development process, rather than treating it as a separate stage, to prevent defects and ensure that each increment of work is potentially shippable.

    - **Global Optimization**: Making decisions that benefit the entire system, even if they don't optimize individual components or departments.

    Implementing the First Way in a DevOps context often involves cultural changes, process improvements, and the adoption of certain tools that support automation and collaboration. For example, continuous integration and delivery (CI/CD) pipelines are commonly used to automate the testing and deployment of software, reducing the risk of human error and speeding up the flow of work.

    By focusing on the flow of work through the entire system, organizations can reduce lead times, improve quality, and deliver value to customers more quickly and reliably. This systemic view is critical for achieving the goals of DevOps and for the transformation of an organization to a more agile and responsive entity.

2. The Second Way: Amplify Feedback Loops
    is focused on enhancing the feedback mechanisms that exist between different stages of the software development and delivery process. The objective is to ensure that teams can quickly and accurately respond to issues, improve quality, and adapt to changing requirements. 

    Key aspects of the Second Way include:

    - **Shortening Feedback Cycles**: The aim is to reduce the time it takes for feedback to be communicated back to the team that can act on it. This means that developers should know as soon as possible if their code changes have caused a problem, and operations should quickly communicate back any issues encountered in production.

    - **Real-time Monitoring and Alerting**: Implementing tools and practices that provide real-time visibility into the health and performance of applications and infrastructure. This allows teams to detect and address issues before they affect users.

    - **Shared Responsibility**: Encouraging a culture where developers and operations teams share responsibility for the quality and stability of the software. This often means that developers take on-call duties and participate in resolving production issues.

    - **Automated Testing**: Utilizing automated tests at various levels (unit, integration, system) to provide immediate feedback on the quality of the code and to catch issues early in the development process.

    - **Continuous Integration (CI)**: Developers frequently merge their code changes into a shared repository, triggering automated builds and tests. This practice helps to quickly identify integration issues.

    - **Collaborative Culture**: Fostering a culture where information is shared openly and where team members from different disciplines work closely together. This can involve regular cross-functional meetings, shared dashboards, and open communication channels.

    - **Blameless Postmortems**: After an incident, conducting a postmortem that focuses on learning and improving systems rather than assigning blame. This encourages honest feedback and a focus on process improvement.

    - **Value Stream Mapping**: Visualizing the entire delivery process to identify bottlenecks and inefficiencies. This helps teams understand where feedback loops can be shortened or improved.

    By amplifying feedback loops, organizations can become more adaptive and resilient. Teams are able to quickly identify and correct problems, which leads to higher quality software and more satisfied customers. This principle complements the First Way by ensuring that the flow of work is not only fast but also safe and reliable. The Second Way is about building a culture of continuous improvement where feedback is a critical component of daily work.

3. The Third Way: Continuous Experimentation and Learning
    is about fostering a culture that encourages ongoing innovation and the development of new skills. It emphasizes the importance of taking risks and learning from both success and failure. This principle is crucial for sustaining a high pace of improvement and adapting to an ever-changing technological landscape.

    Key aspects of the Third Way include:

    - **Encouraging Experimentation**: Creating an environment where individuals and teams feel safe to experiment with new ideas, tools, and processes without fear of retribution if an experiment fails.

    - **Learning from Failures**: Understanding that failure is a natural part of the learning process and using it as an opportunity to improve. This involves conducting blameless postmortems to analyze what went wrong and how to prevent similar issues in the future.

    - **Repetition and Practice**: Recognizing that mastery comes from repetition and practice. Encouraging teams to continually refine their skills and workflows to become more efficient and effective.

    - **Innovation Time**: Allocating time for individuals to work on projects that interest them, which can lead to innovative solutions and improvements.

    - **Knowledge Sharing**: Promoting the sharing of knowledge and skills within the organization through documentation, training sessions, workshops, and mentorship programs.

    - **Resilience Engineering**: Building systems that are resilient to failure and can recover quickly when an incident occurs. This often involves designing for failure, such as implementing chaos engineering practices to proactively discover weaknesses.

    - **Gamification**: Applying elements of game playing, such as point scoring and competition, to encourage engagement with learning and improvement activities.

    - **Reflective Improvement**: Regularly taking time to reflect on performance and processes to identify areas for improvement. This could be through retrospectives, team discussions, or personal reflection.

    By embracing the Third Way, organizations create a dynamic and adaptive culture that not only accepts change but actively seeks it out. This culture of continuous experimentation and learning is essential for maintaining a competitive edge and for the personal growth of team members. It complements the First and Second Ways by ensuring that the flow of work and the feedback loops are not just efficient but also continuously evolving and adapting to new challenges and opportunities.

These Three Ways are foundational to the DevOps movement and are aimed at improving and accelerating the delivery of software. They encourage collaboration across teams, promote automation of the software delivery process, and foster a culture of continuous improvement.