---
b: https://blendedfeelings.com/software/testing/system-testing.md
---

# System testing 
is a critical phase in the software development lifecycle, where the software is evaluated to ensure that it meets the specified requirements and to identify any defects or issues before the software is released to users. It is a comprehensive process that involves several types of testing, each with its own focus and techniques. Here's an overview of the main types of system testing:

1. **Functional Testing**: This type of testing verifies that each function of the software operates in conformance with the requirement specification. It includes testing of user interfaces, APIs, databases, security, client/server communication, and other functionality.

2. **Non-Functional Testing**: This is concerned with the non-functional aspects of the system such as performance, usability, reliability, and scalability. It includes:
   - **[Performance Testing](performance-testing.md)**: To ensure the system meets performance criteria.
   - **[Load Testing](load-testing.md)**: To check how the system behaves under a heavy load.
   - **[Stress Testing](stress-testing.md)**: To determine the system's robustness and error handling under extremely heavy load conditions.
   - **[Usability Testing](usability-testing.md)**: To ensure the system is user-friendly and intuitive.
   - **[Security Testing](security-testing.md)**: To uncover vulnerabilities and ensure that data is protected.

3. **Regression Testing**: This is performed after enhancements or patches have been applied to the system to ensure that no new defects have been introduced and that the existing functionality continues to work as expected.

4. **Integration Testing**: This type of testing is focused on the points of interaction between integrated units/modules to detect interface defects.

5. **System Testing**: This is a high-level testing phase where the complete and integrated software is tested. The purpose is to evaluate the system's compliance with the specified requirements.

6. **Acceptance Testing**: This is the final testing phase before the system is released for operational use. It is intended to ensure that the system meets the business needs and that the users can perform their jobs with the system.

7. **Sanity Testing**: A quick, non-exhaustive testing to ensure that the particular function or bug fix works as expected.

8. **Smoke Testing**: Also known as "Build Verification Testing", it is a subset of test cases that cover the most important functions of the system to ascertain that the most crucial aspects of the program are working after minor changes.

9. **Exploratory Testing**: An approach to testing that is more informal and unstructured, designed to allow the tester to explore the software's capabilities without specific expectations or test cases.

10. **Alpha and Beta Testing**: Alpha testing is done in-house before releasing the product to external users, while beta testing is done by releasing a beta version to a limited audience outside of the company.

Each of these testing types may employ manual or automated testing methods. Automated testing uses software tools to run tests repeatedly, whereas manual testing involves human testers executing the tests.

The goal of system testing is to ensure that the software system is defect-free, meets the user's requirements, and performs its intended functions within all specified conditions. It's a crucial step that helps to reduce the risk of failures and enhances the quality of the software product.