---
b: https://blendedfeelings.com/software/data-warehouse/snowflake-schema.md
---

# Snowflake Schema 
is a logical arrangement of tables in a multidimensional database such as a data warehouse. It is a variation of the star schema but with additional normalization. The snowflake schema is designed to improve the performance of certain queries and to save storage space by eliminating redundancy in data.

In a snowflake schema, the fact table remains at the center, surrounded by dimension tables, much like in a star schema. However, the dimension tables are further normalized into multiple related tables, which form a structure resembling a snowflake when visualized. This normalization involves dividing a table into smaller tables based on a primary key-foreign key relationship.

Here's a high-level comparison of the two schemas:

### Star Schema:
- The fact table is at the center, surrounded by denormalized dimension tables.
- Each dimension table is directly linked to the fact table.
- Simple structure and easier to understand.
- Queries are generally faster because they require fewer joins.
- May require more space due to redundancy in dimension tables.

### Snowflake Schema:
- The fact table is still at the center, but dimension tables are normalized into multiple related tables.
- Dimension tables are linked to the fact table and can also be linked to other dimension tables.
- More complex structure, with more tables and relationships.
- Queries may be slower due to the increased number of joins.
- Saves space due to reduced redundancy.

An example of a snowflake schema could involve sales data, where:
- The fact table contains sales transactions with keys to dimension tables.
- A product dimension table is normalized into separate tables for product categories and product attributes.
- A customer dimension table is normalized into separate tables for customer demographics and customer accounts.

The choice between a star schema and a snowflake schema depends on specific requirements, such as query performance, storage considerations, and the complexity of data relationships. In practice, some data warehouses use a combination of both schemas, known as a hybrid schema, to balance the benefits and drawbacks of each approach.