---
b: https://blendedfeelings.com/software/clean-architecture/architecture.md
---

# Architecture 
of a software system is the shape given it by those who build it. The purpose of that shape is to facilitate development, deployment, operation and maintenance. The  strategy is to leave as many options as possible, for as long as possible. Policies (business logic) should carefully separate from the details (database access, ui),so policy has no knowledge of the details. The business rules should not depend on the technical details of implementation.

It is closely related to several key principles in software architecture and design, such as the Separation of Concerns (SoC), the Single Responsibility Principle (SRP), and the Dependency Inversion Principle (DIP).

**Separation of Concerns (SoC)**: This principle states that a software system should be divided into distinct sections, each addressing a separate concern or part of the problem. This separation allows for easier maintenance and modification, as changes in one area are less likely to impact others.

**Single Responsibility Principle (SRP)**: SRP, one of the SOLID principles, suggests that a class or module should have one, and only one, reason to change. This means that each class or module should only have one job or responsibility.

**Dependency Inversion Principle (DIP)**: DIP, another SOLID principle, states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Furthermore, abstractions should not depend on details; details should depend on abstractions. This principle aims to reduce the coupling between the policy (business logic) and details (implementation) of a system.