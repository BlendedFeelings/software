---
b: https://blendedfeelings.com/software/responsibility-driven-design/responsibility-driven-design.md
---

# Responsibility-Driven Design (RDD) 
is an approach to software design that focuses on the assignment of responsibilities to software objects. It was first described by Rebecca Wirfs-Brock and Brian Wilkerson in a 1989 paper, and later expanded upon in Wirfs-Brock's book "Designing Object-Oriented Software", co-authored with Brian Wilkerson and Lauren Wiener.

The main idea behind RDD is to think about software design in terms of the responsibilities that objects have, rather than simply their attributes and behaviors. Responsibilities are the obligations of an object in terms of its role in the application, including:

1. **Doing**: Objects do things, such as compute values, create other objects, perform actions on behalf of other objects, etc.
2. **Knowing**: Objects know about private encapsulated data and possibly about other objects.
3. **Deciding**: Objects make decisions and choices, often based on their data.
4. **Collaborating**: Objects collaborate with other objects by sending messages to each other, thus delegating tasks and responsibilities.

In RDD, the design process typically involves the following steps:

1. **Identify the primary objects**: Based on the requirements, identify the key concepts that will become objects in the system.
2. **Define responsibilities**: For each object, define what it should do, what it needs to know, and how it makes decisions.
3. **Assign responsibilities to objects**: Determine how objects will collaborate and delegate responsibilities among them.
4. **Define interfaces**: Specify the public interface of each object, which includes the methods that other objects can call.
5. **Design object interactions**: Plan the interactions between objects based on their responsibilities and interfaces.

The benefits of Responsibility-Driven Design include:

- **Encapsulation**: By focusing on responsibilities, designers can better encapsulate the behavior and data of objects, which leads to a more modular and maintainable system.
- **Flexibility**: RDD encourages designing objects that are focused on their roles, which can make the system more adaptable to change.
- **Reusability**: Well-defined responsibilities can lead to objects that are more reusable in different contexts.
- **Testability**: Objects with clear responsibilities are often easier to test because their behavior is more predictable and isolated.

RDD is one of several object-oriented design methodologies, and it is often compared with other approaches like Class-Responsibility-Collaborator (CRC) cards and Domain-Driven Design (DDD). Each of these methodologies emphasizes different aspects of software design but shares the common goal of creating a well-structured object-oriented system.