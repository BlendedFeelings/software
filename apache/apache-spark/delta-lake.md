---
b: https://blendedfeelings.com/software/apache/apache-spark/delta-lake.md
---

# Delta Lake 
is an open-source storage layer that brings reliability to Data Lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of your existing data lake and is fully compatible with API's from Apache Spark, Apache Hive, Presto, and other data processing engines.

Key features of Delta Lake include:

1. **ACID Transactions**: Ensures data integrity with ACID transactions on Spark.

2. **Scalable Metadata Handling**: Processes a large number of metadata operations in your data lake very quickly.

3. **Unified Batch and Streaming Source and Sink**: A table in Delta Lake can be used both as a batch source and a streaming source and sink.

4. **Schema Enforcement and Evolution**: Automatically handles schema variations to prevent insertion of bad records during ingestion.

5. **Time Travel (Data Versioning)**: Allows you to query an older snapshot of data, providing a historical view of your data.

6. **Deletes and upserts (Merge)**: Supports deleting and upserting into tables with programmatic APIs.

7. **Open Format**: Stored as Parquet format in blob storage.

8. **Audit History**: History of all the operations that happened in the table.

9. **Full DML Support**: Supports standard DML including `UPDATE`, `DELETE`, and `MERGE INTO`.

10. **Z-Ordering (Multi-Dimensional Clustering)**: Optimize queries by co-locating related information in the same set of files.

Delta Lake is designed to work with large-scale data and provides a more efficient and reliable way to manage data lakes. It can be deployed on various cloud platforms or on-premises and integrates with many data processing tools and frameworks, making it a versatile choice for organizations looking to improve their data lake architecture.