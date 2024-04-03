---
b: https://blendedfeelings.com/software/agile/acceptance-criteria.md
---

# Acceptance criteria 
are the conditions that a software product must meet to be accepted by a user, a customer, or other stakeholders. They are a set of statements that define the requirements and boundaries of a [user story](user-story.md) or feature, and they help ensure that the development team and stakeholders have a common understanding of what the product should do.

Acceptance criteria are important because they:

- Clarify what the team should build before they start work.
- Provide a way to confirm when a user story has been completed and works as intended.
- Help remove ambiguity from requirements.
- Can be used as a basis for tests.

Acceptance criteria should be specific, clear, and concise. They should be testable and provide enough detail to guide the development process but not so much that they dictate the implementation.

Here's an example of a user story with acceptance criteria:

**User Story**:  
As a website visitor, I want to be able to create an account so that I can save my preferences and access member-only features.

**Acceptance Criteria**:

1. The "Create Account" option is visible on the home page and login page.
2. Clicking the "Create Account" option brings up the account creation form.
3. The account creation form requires the user to provide a username, password, email address, and to confirm the password.
4. The username must be unique and not already in use.
5. The password must be at least 8 characters long and include at least one number and one special character.
6. The email address must be in a valid format.
7. Upon submitting the form with valid information, a confirmation email is sent to the provided email address.
8. The user must verify their email address by clicking a link in the confirmation email to activate the account.
9. The system must not allow login with the new credentials until the email address is verified.
10. After account activation, the user is directed to a welcome page with a successful account creation message.

These criteria define the scope of the user story and provide a checklist that can be used to verify that the functionality meets the customer's needs. During the development process, developers, testers, and the [product owner](product-owner.md) will refer to the acceptance criteria to ensure that the feature is being implemented correctly. After development, the acceptance criteria are used to conduct acceptance testing and confirm that the user story has been completed satisfactorily.