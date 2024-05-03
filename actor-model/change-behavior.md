---
b: https://blendedfeelings.com/software/actor-model/change-behavior.md
---

# Change behavior
known as "becoming" or "state transition."
is a feature that allows an actor to handle messages differently based on its internal state or the context of the messages it has received. 

Here's how it works:

1. **Initial Behavior**: When an actor is created, it starts with an initial behavior. This behavior defines how the actor processes messages at the start.

2. **Processing a Message**: When the actor receives a message, it invokes the behavior it currently has to process the message. The processing may involve updating the actor's state, sending messages to other actors, or performing some computations.

3. **Deciding to Change Behavior**: Based on the outcome of processing the message or the message content itself, the actor may decide to change its behavior. This is often done in response to certain conditions or events.

4. **Changing Behavior**: The actor updates its behavior to a new one. This new behavior will be used to process subsequent messages. The change of behavior is typically done by passing a new function or lambda expression that represents the new behavior.

5. **Subsequent Messages**: Once the behavior has been changed, all subsequent messages will be processed using the new behavior until it is changed again.

The ability to change behavior dynamically allows an actor to model a finite state machine, where each state has a specific behavior associated with it. This is particularly useful in scenarios where the actor's role or responsibility changes over time or in response to certain triggers.

For example, in Akka (a toolkit for building Actor Model systems in Scala and Java), an actor can change its behavior using the `become` method. Here's a simplified Scala example:

```scala
import akka.actor.Actor

class MyActor extends Actor {
  import context._

  def receive = initialState

  def initialState: Receive = {
    case "change" => become(alternateState)
    // Handle other messages for the initial state
  }

  def alternateState: Receive = {
    case "change" => unbecome() // Revert to the initial state
    // Handle other messages for the alternate state
  }
}
```

In the above example, the `MyActor` starts with the `initialState` behavior. Upon receiving a message with the string `"change"`, it switches to the `alternateState` behavior. If it receives another `"change"` message in the alternate state, it reverts to the `initialState` using the `unbecome` method.