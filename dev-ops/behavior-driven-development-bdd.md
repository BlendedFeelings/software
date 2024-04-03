---
b: https://blendedfeelings.com/software/dev-ops/behavior-driven-development-bdd.md
---

# Behavior-Driven Development (BDD) 
is a development approach that has evolved from Test-Driven Development (TDD). It emphasizes collaboration between developers, QA (Quality Assurance), and non-technical or business participants in a software project. BDD focuses on obtaining a clear understanding of desired software behavior through discussion with stakeholders. It extends TDD by writing test cases in a natural language that non-programmers can read.

### Key Concepts of BDD:

- **Ubiquitous Language:** A common language used by all stakeholders to ensure clear communication. It is usually based on the domain model of the software project.
  
- **User Stories:** A high-level definition of requirements that contain enough information so that the developers can produce a reasonable estimate of the effort to implement them. User stories are often written from the perspective of an end user or user of a system.
  
- **Acceptance Criteria:** The set of conditions that must be met for a user story to be considered complete. These are often written in a format that can be converted into automated tests.
  
- **Executable Specifications:** Detailed, written specifications of the system's behavior that are also automated tests. These are often written in a domain-specific language that translates plain language into executable code.
  
- **Example Mapping:** A technique used to discover and define requirements by giving examples of the desired behavior and turning these into a set of concrete examples that can be used as acceptance criteria.
  
- **Living Documentation:** The system documentation that is kept up-to-date with the software development process. This is often generated from the executable specifications.

### BDD Process:

1. **Discovery:** Work with stakeholders to identify and understand the desired outcomes and ensure that the team has a shared understanding of the requirements.
   
2. **Formulation:** Convert the outcomes into user stories with acceptance criteria. The criteria are often formulated as scenarios using a format like Given-When-Then (Gherkin syntax).
   
3. **Conversation:** Engage in discussions with stakeholders to refine the user stories and acceptance criteria, ensuring that all perspectives are considered.
   
4. **Automation:** Write automated tests based on the acceptance criteria before the feature is implemented. These tests will initially fail.
   
5. **Implementation:** Develop the feature to make the tests pass. This is done iteratively, running the tests frequently to ensure that the implementation matches the acceptance criteria.
   
6. **Demonstration:** Show the working feature to stakeholders to confirm that it meets their expectations.
   
7. **Refinement:** Based on feedback, refine the implementation and tests as needed.

### Tools for BDD:

- **Cucumber:** A tool that supports BDD with a plain language parser called Gherkin. It allows the writing of tests in a way that can be understood by all stakeholders.
  
- **SpecFlow:** A .NET-focused tool similar to Cucumber that integrates with Visual Studio.
  
- **JBehave:** A framework for Java that allows for story/test creation in a natural language.

BDD helps in creating a shared understanding of the functionality between the team members and stakeholders, ensuring that all features are developed with the user's needs in mind. It also helps in creating a robust suite of regression tests that can be used to ensure that future changes do not break existing functionality.