---
b: https://blendedfeelings.com/software/testing/smoke-testing.md
---

# Smoke testing
refers to a preliminary level of testing conducted to check whether the most important functions of a program work correctly. It is a shallow and wide approach to testing, as opposed to deep and narrow thorough testing methods like unit testing.

The term "smoke testing" comes from a hardware testing practice where a device is turned on for the first time, and if it doesn't catch fire (i.e., smoke), it's a good initial indication that it doesn't have any critical faults. In software, the analogy is similar: if the new build can launch and perform its most essential functions, it's stable enough to proceed to more rigorous testing phases.

Here are the key characteristics of smoke testing:

1. **Shallow and Broad**: Smoke tests are designed to touch upon all areas of the application without going into depth. The goal is to verify that all critical paths are working and that there are no showstopper defects that would impede further testing.

2. **Quick to Execute**: Smoke tests are typically automated and can be run quickly, often as part of a continuous integration/continuous delivery (CI/CD) pipeline.

3. **Build Verification**: Smoke tests are often run on new builds to ensure that the build is stable and can be passed on for further testing.

4. **Gatekeeper**: Smoke testing acts as a gatekeeper, preventing broken builds from wasting the time of QA teams with more detailed testing.

5. **Frequent and Routine**: Since smoke tests are quick and automated, they can be run as often as needed — typically, every time a new build is produced.

6. **Critical Functionality**: Smoke tests cover basic functionality of the application, ensuring that the application can launch, that the user can navigate through the main areas, and that key features work as expected.

Smoke testing is an essential part of the software quality assurance process, as it helps to identify major issues early in the development cycle, saving time and resources.