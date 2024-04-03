---
b: https://blendedfeelings.com/software/concepts/principle-of-least-surprise.md
---

# Principle of Least Surprise
also known as the Principle of Least Astonishment, is a design principle that states that a system should behave in a way that is least surprising to its users. In other words, the system's behavior should be consistent with user expectations, and it should operate in a manner that is predictable and intuitive.

### Understanding the Principle of Least Surprise

The principle applies to various aspects of software design, from user interface design to the design of software components and APIs. The idea is that software should be designed so that users can quickly learn and understand its behavior, leading to a more user-friendly and efficient experience.

When users interact with software, they bring with them a set of expectations based on their previous experiences, conventions, and standards. The Principle of Least Surprise suggests that software should align with these expectations as much as possible.

### Benefits of the Principle of Least Surprise

- **Usability**: Software that aligns with user expectations is easier to use and requires less learning time.
- **Productivity**: Users can accomplish tasks more efficiently when software behaves as expected.
- **Fewer Errors**: Predictable software reduces the likelihood of user mistakes and misunderstandings.
- **Satisfaction**: Users are more satisfied with software that works in a way they anticipate, leading to a better overall experience.

### Examples of the Principle of Least Surprise

1. **User Interface**: A trash bin icon should represent a place to delete files, as this is a widely understood convention.
2. **API Design**: A function named `calculateTotal` should return the total amount and not modify the state of the object, as the word "calculate" implies a read-only operation.
3. **Programming**: A method called `saveToFile` should not also send an email as a side effect, as the name does not imply any emailing functionality.

### Applying the Principle of Least Surprise

To apply this principle effectively, designers and developers should:

- Understand the expectations and mental models of their users.
- Follow platform and industry conventions and standards.
- Make sure that the names of functions, methods, and variables clearly indicate their purpose and side effects.
- Avoid hidden side effects in methods or functions.
- Provide clear and consistent feedback to the user for their actions.
- Document any behavior that might be unexpected to users.

It's important to note that what is surprising can be subjective and may vary based on the user's level of expertise and cultural background. Therefore, it's essential to know your audience and design with their expectations in mind. The Principle of Least Surprise serves as a reminder to keep the user's perspective at the forefront of the design process.