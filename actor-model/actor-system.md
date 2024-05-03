---
b: https://blendedfeelings.com/software/actor-model/actor-system.md
---

# Actor system
is a framework that manages the lifecycle of actors, providing messaging, supervision, and concurrency control for building concurrent and distributed applications.

An actor system is an implementation of the actor model. It provides a platform where actors live and execute. It handles the creation of actors, delivers messages to them, and provides various services that help in managing the actors' life cycle and the resources they need.

Key components and features of an actor system typically include:

- **Actor Creation**: A facility to create and manage actors within the system.
- **Messaging System**: A reliable message-passing system that allows actors to communicate with each other.
- **Mailboxes**: Queues that store incoming messages to an actor until they can be processed.
- **Supervision**: A hierarchy where actors can supervise the execution of other actors, restarting or stopping them in case of failures.
- **Location Transparency**: Actors can communicate with each other without needing to know the actual location of the other actors, whether they're local or remote.
- **Concurrency Control**: The system ensures that actors can run concurrently without the need for traditional locking mechanisms.
- **Fault Tolerance**: The system often includes strategies for dealing with failures in a graceful manner, allowing the system to recover from actor failures.
- **Scheduling**: An internal scheduler that decides when each actor gets to process messages.

### Examples of Actor Systems

There are several implementations of actor systems in various programming languages:

- **Akka**: A popular actor system implemented in Scala and usable from other JVM languages like Java. It provides a comprehensive toolkit for building concurrent, distributed, and resilient message-driven applications.
- **Erlang/OTP**: Erlang is a programming language that has built-in support for the actor model through its OTP (Open Telecom Platform) framework. It's known for its use in systems that require high availability.
- **Orleans**: A framework that provides a straightforward approach to building distributed high-scale computing applications, without the need to learn and apply complex concurrency or other scaling patterns. It's designed for use with .NET.
- **Proto.Actor**: A cross-platform actor model framework with support for C# and Go, among other languages. It aims to be lightweight and fast.

When developing applications using the actor model, it's essential to embrace the asynchronous, non-blocking, and message-driven nature of the system. This can lead to systems that are more scalable and resilient to failure, but it also requires a different approach to design and debugging compared to traditional sequential programming models.