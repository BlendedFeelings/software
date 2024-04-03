---
b: https://blendedfeelings.com/software/clean-architecture/index.md
---

# Clean architecture 
is a software design philosophy that emphasizes the separation of concerns among the different components of a system. This approach was introduced by Robert C. Martin (also known as Uncle Bob) and is intended to make software systems more maintainable, scalable, and testable by organizing code into layers with clear responsibilities and controlled dependencies.

Here are the key principles and components of clean architecture:

1. **Independent of Frameworks**: The architecture does not depend on the existence of some library or framework. This allows you to use such frameworks as tools, rather than having to cram your system into their limited constraints.

2. **Testable**: The business rules can be tested without the UI, database, web server, or any other external element.

3. **Independent of UI**: The UI can change easily, without changing the rest of the system. A web UI could be replaced with a console UI, for example, without changing the business rules.

4. **Independent of Database**: You can swap out Oracle or SQL Server for MongoDB, BigTable, CouchDB, or something else. Your business rules are not bound to the database.

5. **Independent of any external agency**: In fact, your business rules simply don’t know anything at all about the outside world.

The typical structure of clean architecture involves several concentric circles representing different areas of software:

- **Entities**: These are the business objects of the application. They encapsulate the most general and high-level rules. They are the least likely to change when something external changes.

- **Use Cases**: These encapsulate all of the business rules and use cases of the application. They orchestrate the flow of data to and from the entities, and direct those entities to use their enterprise-wide business rules to achieve the goals of the use case.

- **Interface Adapters**: This layer adapts data from the format most convenient for the use cases and entities to the format most convenient for some external agency such as the database or the web. It includes things like controllers, presenters, gateways, and data repositories.

- **Frameworks and Drivers**: This is where all the details go. The web is a detail, the database is a detail, any external agency is a detail. This layer is kept separate from the rest of the application so that it can change without affecting the rest of the application.

The dependencies between these circles are strictly controlled. For example, code in the inner circles cannot know anything at all about the outer circles. This is achieved through the Dependency Rule: source code dependencies can only point inwards, nothing in an inner circle can know anything at all about something in an outer circle.

In practice, this architecture involves creating interfaces and using dependency injection to invert dependencies, which allows the core application to be agnostic of the implementation details in the outer layers. This separation allows developers to modify the outer layers without affecting business logic and makes the system easier to maintain and adapt to changing requirements.