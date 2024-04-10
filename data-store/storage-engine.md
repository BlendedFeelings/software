---
b: https://blendedfeelings.com/software/data-store/storage-engine.md
---

# Storage engine
refers to the underlying software component that a database management system (DBMS) uses to create, read, update, and delete (CRUD) data from a database. It is responsible for managing how data is stored on disk or in memory, how it is indexed for quick retrieval, and how transactions are handled for consistency and integrity.

Different storage engines are designed with various strengths and trade-offs in mind, such as performance, reliability, data compression, transaction support, and the ability to handle different types of workloads (e.g., read-heavy, write-heavy, or mixed).

Here are some common types of storage engines:

1. **InnoDB (MySQL/MariaDB)**: A transaction-safe storage engine with commit, rollback, and crash-recovery capabilities to protect user data. It supports foreign keys and row-level locking.

2. **MyISAM (MySQL/MariaDB)**: A storage engine that provides high-speed storage and retrieval but does not support transactions. It is good for read-heavy workloads but not for write-heavy or transactional applications.

3. **RocksDB (used in various systems)**: An embeddable, persistent key-value store for fast storage, which is optimized for fast storage on flash and RAM. It is often used in systems that require high performance and low latency.

4. **MongoDB WiredTiger**: The default storage engine for MongoDB, designed for high performance, multi-core scalability, and additional compression options.

5. **LevelDB (used in various systems)**: An open-source on-disk key-value store, which is optimized for read-heavy workloads with efficient range queries.

6. **PostgreSQL engines**: PostgreSQL uses a single storage engine but allows for table-level customization through table access methods, which can be seen as a form of pluggable storage engines.

7. **Microsoft SQL Server engines**: SQL Server uses a single type of storage engine that is highly optimized for transactional workloads and integrates tightly with the rest of the SQL Server features.

8. **SQLite**: An embedded SQL database engine that is self-contained, serverless, and requires no configuration. It is widely used in mobile applications and small to medium-sized applications.

The choice of a storage engine can significantly affect the performance, scalability, and reliability of a database system, and it is often chosen based on the specific requirements of an application.