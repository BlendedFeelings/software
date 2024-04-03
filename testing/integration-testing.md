---
b: https://blendedfeelings.com/software/testing/integration-testing.md
---

# Integration testing 
is a level of software testing where individual units are combined and tested as a group. The purpose of this testing is to expose faults in the interaction between integrated units. Test drivers and test stubs are used to assist in integration testing.

Here's a brief overview of the process and concepts involved in integration testing:

1. **Integration Testing Levels**:
   - **Component Integration Testing**: Testing the interactions between software components or units.
   - **System Integration Testing**: Testing the integration between different systems and may involve third-party systems.
   - **Service Integration Testing**: Specifically focuses on the integration of service-oriented architecture (SOA) components.

2. **Approaches**:
   - **Big Bang Approach**: All or most of the units are combined together and tested at one go. This can be challenging due to the difficulty in isolating errors.
   - **Incremental Approach**: Units are integrated and tested one by one until all units are integrated. This can be top-down, bottom-up, or functional incrementation.
     - **Top-Down**: Integration testing takes place from top to bottom following the control flow of the software system.
     - **Bottom-Up**: Integration testing takes place from the bottom up to the top.
     - **Functional Incrementation**: Units are integrated according to functionality.

3. **Techniques**:
   - **Stub and Driver**: Stubs and drivers are used to simulate missing components in top-down and bottom-up approaches, respectively.
   - **Back-to-Back Testing**: Two versions of a component (old and new) are tested under similar conditions and outputs are compared.

4. **Tools**: There are various tools available that support integration testing, including:
   - **Continuous Integration Tools**: Such as Jenkins, TeamCity, and Bamboo.
   - **Service Virtualization Tools**: To simulate the behavior of components that are not yet developed or accessible.
   - **Test Automation Tools**: Such as Selenium, TestComplete, and QTP for automating the execution of tests.

5. **Challenges**:
   - **Interface Compatibility**: Ensuring that interfaces between modules are compatible.
   - **Data Flow Problems**: Ensuring that data flows correctly between modules.
   - **Error Handling**: Testing the system's ability to handle errors that occur during interaction between modules.

6. **Best Practices**:
   - **Define Clear Integration Points**: Clearly define how and where the modules will interact.
   - **Use a Version Control System**: This helps manage the different versions of components being integrated.
   - **Automate Where Possible**: Automated tests can increase the efficiency and reliability of the testing process.
   - **Monitor and Measure**: Keep track of what has been tested and what has not, and measure code coverage.

Integration testing is an essential part of the software development lifecycle, ensuring that the combined parts of an application function together as expected. It is typically performed after unit testing and before system testing.