---
b: https://blendedfeelings.com/software/concurrent-programming/sleeping-barber-problem.md
---

# Sleeping Barber problem 
is a classic synchronization problem that illustrates the challenges of coordinating access to a shared resource (in this case, a barber's time) among multiple concurrent processes (customers). It was introduced by Edsger Dijkstra in 1965 to demonstrate the pitfalls of improper process synchronization and to discuss solutions to avoid deadlocks.

The problem is set in a barber shop with the following characteristics:

1. There is one barber who has one barber chair in a shop.
2. There is a waiting room with a number of chairs in which the customers can wait if the barber is busy.
3. When there are no customers, the barber goes to sleep in his chair.
4. When a customer arrives, they have to wake the barber if he's asleep or sit in the waiting room if the barber is cutting someone else's hair.
5. If the waiting room is full, the customer leaves (the problem is often stated such that the customer waits until a chair is free, but in some variations, they leave if all chairs are occupied).

The challenge is to write a program that coordinates the barber and the customers without running into race conditions, deadlocks, or starvation. The main issues to consider are mutual exclusion (to ensure that only one customer is getting a haircut at a time), synchronization (to make sure the barber is not woken up unnecessarily or customers are not lost), and deadlock prevention (to avoid situations where the barber is sleeping while there are customers waiting).

A typical solution involves using semaphores or other synchronization primitives to manage the access to the barber chair and the waiting room. Here's a high-level outline of a possible solution:

1. A semaphore `barberReady` is used to indicate whether the barber is ready to give a haircut. Initially, it is set to 0 (barber is asleep).
2. A semaphore `accessWaitingRoom` is used to ensure mutual exclusion when customers are modifying the number of people in the waiting room.
3. A semaphore `customersWaiting` is used to indicate the number of customers waiting for a haircut. Initially, it is set to 0.

Here's a pseudocode representation of the problem:

```pseudocode
Semaphore barberReady = 0
Semaphore accessWaitingRoom = 1
Semaphore customersWaiting = 0
int numberOfFreeSeats = N // Total number of seats in the waiting room

Barber:
while true:
    wait(customersWaiting) // Go to sleep if no customers
    wait(accessWaitingRoom) // Lock access to waiting room
    numberOfFreeSeats += 1 // One waiting seat becomes free
    signal(barberReady) // Barber is ready to give a haircut
    signal(accessWaitingRoom) // Release access to waiting room
    // Give a haircut

Customer:
wait(accessWaitingRoom) // Lock access to waiting room
if numberOfFreeSeats > 0:
    numberOfFreeSeats -= 1 // Sit down in a waiting seat
    signal(customersWaiting) // Notify the barber that there is a customer
    signal(accessWaitingRoom) // Release access to waiting room
    wait(barberReady) // Wait until the barber is ready
    // Get a haircut
else:
    signal(accessWaitingRoom) // Release access to waiting room
    // Leave without a haircut
```

In this solution, the semaphores and the variable `numberOfFreeSeats` are used to ensure that the barber and customers interact correctly. The barber sleeps when there are no customers and is woken up when a customer arrives. The customers either wait in the waiting room if there's a free seat or leave if it's full. The mutual exclusion on the waiting room ensures that the count of free seats is accurate and not subject to race conditions.