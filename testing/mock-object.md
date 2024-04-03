---
b: https://blendedfeelings.com/software/testing/mock-object.md
---

# Mock object 
in software testing is a simulated object that mimics the behavior of a real object in controlled ways. Mock objects are commonly used in unit testing when it's impractical or impossible to use the actual object the system interacts with. This could be due to reasons such as:

- The real object is not yet implemented.
- The real object is slow or has side effects (e.g., a database or a web service).
- The real object has non-deterministic behavior, which makes tests unreliable.
- The real object is difficult to set up or requires a complex environment.

Mock objects allow developers to simulate the behavior of the real objects to test the interaction between the system under test and its dependencies. They can be programmed to return specific values, throw exceptions, or perform certain actions when their methods are called, thus ensuring the test conditions are under full control.

Mocking frameworks are often used to create mock objects. These frameworks provide a simple and expressive way to create and configure mocks. Some popular mocking frameworks for different programming languages include:

- **Java**: Mockito, EasyMock, JMock
- **C#**: Moq, NSubstitute, Rhino Mocks
- **Python**: unittest.mock, Mock, MagicMock
- **JavaScript/TypeScript**: Jest, Sinon.js, Jasmine

Here's an example of using a mock object in a unit test with the C# Moq framework:

```csharp
using Moq;
using Xunit;

public interface IDependency {
    int Calculate(int input);
}

public class SystemUnderTest {
    private readonly IDependency _dependency;

    public SystemUnderTest(IDependency dependency) {
        _dependency = dependency;
    }

    public int PerformCalculation(int input) {
        return _dependency.Calculate(input) + 10;
    }
}

public class MyTests {
    [Fact]
    public void Test_PerformCalculation() {
        // Arrange
        var mockDependency = new Mock<IDependency>();
        mockDependency.Setup(d => d.Calculate(It.IsAny<int>())).Returns(20);
        var systemUnderTest = new SystemUnderTest(mockDependency.Object);

        // Act
        var result = systemUnderTest.PerformCalculation(5);

        // Assert
        Assert.Equal(30, result); // Because mock returns 20 and we add 10 in the method
    }
}
```

In this example, `IDependency` is an interface that the `SystemUnderTest` depends on. The mock object is created to simulate an implementation of `IDependency`. The `Calculate` method is set up to always return 20 when it's called with any integer. The `PerformCalculation` method of `SystemUnderTest` is then tested to ensure it behaves as expected when the dependency returns 20.