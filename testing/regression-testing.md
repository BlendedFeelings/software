---
b: https://blendedfeelings.com/software/testing/regression-testing.md
---

# Regression testing 
is a type of software testing that ensures that recently developed or modified code has not adversely affected existing features. It verifies that the old code still works after the changes. Regression testing is crucial because it catches bugs that could be introduced into the existing functionality after changes such as enhancements, patches, configuration changes, or other system maintenance, which could lead to software regressions.

Here are some key points about regression testing:

1. **Purpose**: The primary goal of regression testing is to ensure that new changes do not break or degrade any existing functionality.

2. **Scope**: Regression testing can range from testing specific functionalities that are likely to be affected by the change, to testing the entire application if the change is significant enough.

3. **Frequency**: It is often performed every time there is a change in the code, to ensure continuous stability. It can be part of the daily build process in a Continuous Integration/Continuous Deployment (CI/CD) pipeline.

4. **Automation**: Regression tests are good candidates for automation because they are run frequently and need to be executed repeatedly. Automated regression testing can save time and resources and helps in providing quick feedback.

5. **Test Cases**: Regression test cases are derived from the functional specifications of the application and from bug reports. They should be regularly reviewed and updated to reflect changes in the system and to remove obsolete tests.

6. **Maintenance**: As the system evolves, the regression test suite should also evolve. Test cases may need to be added, modified, or deleted to remain effective.

7. **Tools**: There are various tools available that support automated regression testing, such as Selenium, QTP (Quick Test Professional), and TestComplete.

8. **Challenges**: One of the challenges in regression testing is selecting the right set of test cases to run—neither too few (which might miss some defects) nor too many (which can waste resources and time).

9. **Best Practices**: To optimize regression testing, it's recommended to prioritize test cases based on the risk and impact of changes, to use test automation where possible, and to maintain a good balance between new tests and existing ones.

10. **Integration with Development**: Regression testing should be tightly integrated with the development process to ensure that any code change can be verified immediately for potential regressions.

In summary, regression testing is an essential part of the software development lifecycle to maintain the quality and reliability of the software as it evolves.