---
b: https://blendedfeelings.com/software/data-warehouse/data-warehouse.md
---

# Data warehouse 
is a centralized repository designed to store integrated data from multiple sources. Data warehouses are optimized for querying and analysis, making them ideal for business intelligence, data analytics, and reporting. They support decision-making processes by providing a consolidated view of an organization's historical data.

Here are some key characteristics of a data warehouse:

1. **Subject-Oriented**: Data is organized by subject, such as sales, finance, or customer information, to provide a comprehensive view of business operations.
2. **Integrated**: Data from various sources is cleaned, transformed, and standardized to ensure consistency.
3. **Non-Volatile**: Once entered into the warehouse, data is not frequently changed or deleted. It provides a stable historical record.
4. **Time-Variant**: Data is stored with a time dimension, allowing for analysis of trends and patterns over time.

In contrast, a database is a system that stores and manages data. It is typically used for the day-to-day operations of an organization, such as transaction processing. Databases are designed to handle frequent updates, deletions, and insertions of data, ensuring data integrity and consistency in real-time.

Key differences between a data warehouse and a database include:

1. **Purpose**: Databases are designed for transactional processing (OLTP - Online Transaction Processing), whereas data warehouses are designed for analytical processing (OLAP - Online Analytical Processing).
2. **Data Structure**: Databases often use normalized data structures to minimize redundancy and optimize update operations. Data warehouses usually use denormalized structures, such as star or snowflake schemas, to optimize read operations and analytical queries.
3. **Query Performance**: Databases are optimized for fast query performance on transactional operations, while data warehouses are optimized for complex queries that aggregate large volumes of data.
4. **Update Frequency**: Databases are updated in real-time as transactions occur. Data warehouses are typically updated on a scheduled basis (e.g., nightly or weekly) during ETL (Extract, Transform, Load) processes.
5. **Data History**: Databases usually contain current data, with limited historical data. Data warehouses store large amounts of historical data to support trend analysis and forecasting.

In summary, the primary distinction between a data warehouse and a database lies in their respective purposes and the types of operations they are optimized for – transactional processing for databases and analytical processing for data warehouses.