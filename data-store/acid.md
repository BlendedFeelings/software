---
b: https://blendedfeelings.com/software/data-store/acid.md
---

# ACID 
is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee that database transactions are processed reliably. These properties are key concepts in the field of database transaction management and are crucial for ensuring the integrity of data within a database. Here is a brief overview of each of these properties:

1. **Atomicity**: This property ensures that all the operations within a transaction are treated as a single unit. This means that either all operations are completed successfully, and the transaction is committed, or if any operation fails, the entire transaction is rolled back. In other words, a transaction is atomic — it either happens in full or not at all.

2. **Consistency**: Consistency ensures that a transaction can only bring the database from one valid state to another, maintaining the integrity of the database. Before and after the transaction, all database constraints, cascades, triggers, and any other rules must be respected. This means that a transaction must leave the database in a consistent state after it is committed.

3. **Isolation**: This property ensures that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other. Isolation is about controlling the way transaction interleave with each other and ensuring that one transaction does not affect the ongoing operations of another transaction. Different levels of isolation are available, and higher levels prevent phenomena such as dirty reads, non-repeatable reads, and phantom reads.

4. **Durability**: Durability guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure. This means that the changes made by the transaction are permanently recorded in the database and will not be lost even if the system crashes immediately after.

These properties are typically ensured by the database management system (DBMS), which manages the execution of transactions, ensuring that these ACID properties are maintained. The implementation of ACID properties can vary between different types of databases, such as relational databases and NoSQL databases, with some prioritizing performance over strict adherence to ACID principles.