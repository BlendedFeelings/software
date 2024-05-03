---
b: https://blendedfeelings.com/software/data-warehouse/star-schema.md
---

# Star schema 
is a popular data warehouse schema that simplifies the design of a database by structuring data into fact and dimension tables in a way that resembles a star. In this schema, a central fact table is surrounded by dimension tables, each of which is linked to the fact table by a foreign key. Here's a breakdown of the components and characteristics of the star schema:

1. **Fact Table:**
   - The fact table is the core of the star schema and contains quantitative data for analysis.
   - It typically includes numeric measures (facts) and keys to each of the related dimension tables.
   - Facts are often additive and can be aggregated along any of the dimensions associated with them.

2. **Dimension Tables:**
   - Dimension tables contain descriptive attributes (dimensions) that are used to query and categorize data.
   - Each dimension table has a primary key that uniquely identifies each dimension record.
   - The dimension tables are denormalized, meaning they may contain redundant data to improve query performance.

3. **Simplicity:**
   - One of the main advantages of the star schema is its simplicity, which makes it easy to understand and navigate.
   - The straightforward design facilitates efficient querying by reducing the number of joins needed to retrieve data.

4. **Performance:**
   - The denormalization of dimension tables and the clear separation between dimensions and facts often result in faster query performance.
   - Star schemas are optimized for read-heavy operations typical in data warehousing and BI applications.

5. **Scalability:**
   - While star schemas are generally easy to expand, the addition of new dimensions or changes to the structure can require significant modifications to the existing schema.

6. **Examples of Queries:**
   - Queries on a star schema often involve aggregations such as sums, averages, and counts across various dimensions.
   - For instance, a query might request the total sales amount by region and product category for a given time period.

Here's a visual representation of the star schema:

```
        Dimension Table
            /    |    \
           /     |     \
          /      |      \
Dimension Table - Fact Table - Dimension Table
          \      |      /
           \     |     /
            \    |    /
        Dimension Table
```

In summary, the star schema is a foundational architecture for data warehousing that enables efficient storage and querying of large volumes of data. It is particularly well-suited for supporting BI tools and applications that require fast read access to support analytics and reporting.