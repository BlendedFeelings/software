---
b: https://blendedfeelings.com/software/agile/simple-design.md
---

# Simple Design
is one of the core principles of Extreme Programming (XP) and refers to the practice of designing software in the simplest way possible that still meets the current requirements. The idea behind Simple Design is to avoid complexity and over-engineering, which can lead to harder-to-maintain code and increased risk of defects.

In XP, Simple Design is guided by a few key rules or principles:

1. **Do The Simplest Thing That Could Possibly Work (DTSTTCPW)**: This rule encourages developers to think of the simplest way to implement a feature or fix a problem without getting bogged down by potential future requirements or complexities that aren't currently needed.

2. **You Aren't Gonna Need It (YAGNI)**: This principle suggests that developers should not add functionality until it is necessary. YAGNI is a reminder to avoid implementing features or designs that are not currently required, as they may never be needed, and could waste time and resources.

3. **Once and Only Once (OAOO)**: Code duplication is a common source of waste and errors. OAOO suggests that every piece of knowledge in the system should be represented in a single place. If you find yourself duplicating code, it's a sign that you should refactor.

4. **Pass All Tests**: The design must pass all the required tests, indicating that the software meets the necessary functional requirements. This is a cornerstone of Test-Driven Development (TDD), which is closely associated with XP.

5. **Refactoring**: Continuous improvement of the code is essential. As new features are added and the understanding of the problem domain evolves, the design should be refactored to maintain simplicity.

6. **Maximize Clarity**: The design should be clear and understandable. This includes choosing meaningful names for classes, methods, and variables, as well as writing clean, well-organized code.

7. **Minimal Methods and Classes**: Only create classes and methods that are necessary for the current requirements. Avoid speculative generality by not creating additional layers of abstraction that aren't needed.

8. **Sufficient for Today's Needs**: Focus on what is needed now and not what might be needed in the future. This helps to keep the design focused and avoids the overhead of maintaining unused code.

By adhering to a Simple Design, XP teams aim to produce software that is easier to understand, maintain, and extend. It also enables the team to be more responsive to changes, as there is less complexity to manage when requirements evolve. Simple Design is not about being simplistic or cutting corners; it's about finding the most straightforward solution that works and is maintainable.