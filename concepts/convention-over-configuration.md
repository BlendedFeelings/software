---
b: https://blendedfeelings.com/software/concepts/convention-over-configuration.md
---

# Convention over Configuration
also known as "Coding by Convention" is a software design paradigm that aims to decrease the number of decisions that developers need to make, gaining simplicity without necessarily losing flexibility. The idea is that by following certain conventions, the amount of configuration (specification of parameters) required to set up a system is reduced.

Here's how "Convention over Configuration" benefits software development:

1. **Simplification**: By adhering to predefined conventions, developers can avoid writing boilerplate code and configuration files, making the development process faster and more straightforward.

2. **Ease of Use**: New developers can quickly understand the structure and behavior of an application because it follows widely accepted standards.

3. **Reduced Decision Fatigue**: Developers don't need to spend time on trivial decisions about the structure of the project or naming of elements.

4. **Focus on Business Logic**: Developers can concentrate on the unique aspects of the application (the business logic) rather than the setup and configuration details.

5. **Rapid Development**: This approach allows for faster setup and development of applications, as many of the standard components are already pre-configured.

6. **Consistency**: It promotes consistency across different projects within the same framework or platform, making it easier to maintain and understand codebases.

7. **Less Code**: Less configuration code means a smaller codebase, which is easier to maintain and less prone to bugs.

Examples of "Convention over Configuration" in software frameworks:

- **Ruby on Rails**: This web application framework is a prime example of "Convention over Configuration". It assumes where certain files should be saved, how classes should be named, how database table names should correspond to model class names, etc.

- **Spring Boot**: This Java-based framework uses convention over configuration to set up applications quickly, with minimal setup.

- **Django**: This Python web framework follows the "Don't Repeat Yourself" (DRY) principle, which is complementary to "Convention over Configuration", by assuming certain things about your project structure and behavior.

While "Convention over Configuration" offers many benefits, it is important to note that it can sometimes lead to confusion if the conventions are not well understood or if there is a need to deviate from them. In such cases, frameworks typically provide ways to override the default conventions with explicit configurations.