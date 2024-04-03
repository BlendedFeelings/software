---
b: https://blendedfeelings.com/software/programming-patterns/chain-of-responsibility-pattern.md
---

# Chain Of Responsibility Pattern 
is a behavioral design pattern that allows an object to pass a request along a chain of handlers. Within the chain, each handler decides either to process the request or to pass it to the next handler in the chain.

Here's an overview of how the Chain of Responsibility pattern works:

**Handler Interface**: This defines a common interface for all concrete handlers. It usually includes a method to set the next handler in the chain and another method to process the request.

**Concrete Handlers**: These are classes that implement the Handler interface. Each handler has the logic to decide whether to process the request or pass it to the next handler. If a handler can handle the request, it does so; otherwise, it forwards the request to the next handler in the chain.

**Client**: The client configures the chain by linking the handlers together. It then initiates the request to the chain.

**Request**: This is the object that contains the data or instructions that need to be processed by the handlers.

The benefits of using the Chain of Responsibility pattern include:

Decoupling: The client that sends the request is decoupled from the code that processes it. This means that the client doesn't need to know which part of the system will handle the request.
Flexibility: It's easy to add new handlers or change the order of existing handlers without changing the client code.
Responsibility Segregation: Different parts of the code can be responsible for different tasks, which can make the code more manageable and easier to maintain.

```java
// Define the Handler interface
interface Handler {
    void setNext(Handler handler);
    void handleRequest(Request request);
}

// Define the ConcreteHandler classes
class ConcreteHandlerA implements Handler {
    private Handler next;

    public void setNext(Handler handler) {
        next = handler;
    }

    public void handleRequest(Request request) {
        if (request.getLevel() == Level.LEVEL_A) {
            // Handle the request
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

class ConcreteHandlerB implements Handler {
    private Handler next;

    public void setNext(Handler handler) {
        next = handler;
    }

    public void handleRequest(Request request) {
        if (request.getLevel() == Level.LEVEL_B) {
            // Handle the request
        } else if (next != null) {
            next.handleRequest(request);
        }
    }
}

// Define the Request class
class Request {
    private Level level;

    public Request(Level level) {
        this.level = level;
    }

    public Level getLevel() {
        return level;
    }
}

// Define the Level enum
enum Level {
    LEVEL_A,
    LEVEL_B,
    LEVEL_C
}

// Usage
Handler handlerA = new ConcreteHandlerA();
Handler handlerB = new ConcreteHandlerB();

handlerA.setNext(handlerB);

Request request1 = new Request(Level.LEVEL_A);
handlerA.handleRequest(request1);

Request request2 = new Request(Level.LEVEL_B);
handlerA.handleRequest(request2);

```