---
b: https://blendedfeelings.com/software/programming-patterns/command-pattern.md
---

# Command Pattern
is used to separate the request for an action from the execution of the action. It encapsulates a request as an object, which can be stored, queued, or undone.
It works by defining a Command interface that declares the execute() method, which all commands must implement. Each command encapsulates a request and the information necessary to execute the request. The commands can be stored in a queue, which allows them to be executed in a specific order. 
Receiver encapsulates the business logic of the action.

Here's a basic breakdown of the Command Pattern:

**Command Interface**: This defines a method for executing a command. Often, this is just a single method called execute().

**Concrete Command**: This class implements the Command interface and defines the binding between a Receiver object and an action. It implements the execute() method by invoking the corresponding operation(s) on the Receiver.

**Receiver**: The Receiver class contains the actual business logic that handles the command's job.

**Invoker**: The Invoker holds a command and can call the command's execute() method to perform the command.

**Client**: The Client creates a ConcreteCommand object and sets its receiver.

```java
// Command interface
interface Command {
    void execute();
}

// Concrete command
class ConcreteCommand implements Command {
    private Receiver receiver;
    private String data;

    ConcreteCommand(Receiver receiver, String data) {
        this.receiver = receiver;
        this.data = data;
    }

    void execute() {
        receiver.action(data);
    }
}

// Receiver
class Receiver {
    void action(String data) {
        // ...
    }
}

// Invoker
class Invoker {
    private Command command;

    void setCommand(Command command) {
        this.command = command;
    }

    void executeCommand() {
        command.execute();
    }
}

// Usage
Receiver receiver = new Receiver();
Command command = new ConcreteCommand(receiver, "some data");
Invoker invoker = new Invoker();
invoker.setCommand(command);
invoker.executeCommand();

```