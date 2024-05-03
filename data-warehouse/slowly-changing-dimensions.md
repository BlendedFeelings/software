---
b: https://blendedfeelings.com/software/data-warehouse/slowly-changing-dimensions.md
---

# Slowly Changing Dimensions (SCDs) 
are a common data warehousing concept that deals with managing the changes in dimension data over time. Dimensions are the descriptive attributes of data in a data warehouse, which are used for grouping, filtering, and labeling; examples include time, geography, products, and customers.

In the context of data warehousing, dimensions can change over time, and the way these changes are handled can significantly impact the ability to historically analyze data. There are several types of SCDs:

### Type 0: Fixed Dimension
No changes are allowed; the data is static and historical data is not tracked.

### Type 1: No History
When changes occur, the old data is overwritten with the new data. There is no record of historical data, which means it is impossible to see historical changes.

### Type 2: Row Versioning
This is the most common type of SCD. It involves creating a new record with a new surrogate key each time a change occurs, thus preserving historical data. Each record typically includes a version number or effective dates to indicate the time validity of that record.

### Type 3: Previous Value Column
Instead of creating a new record, a new column is added to the existing record to capture the previous value of the changed attribute. This method has the limitation of only being able to track a single change.

### Type 4: History Table
Changes are stored in a separate history table, while the current data is kept in the original dimension table. This allows for a clean current view and a detailed historical view.

### Type 6: Hybrid (Type 1 + Type 2 + Type 3)
This is a combination of Types 1, 2, and 3 (sometimes humorously referred to as Type 6, as in 1+2+3), which allows for current data to overwrite old data, keeps historical data in additional columns, and uses row versioning for full historical tracking.

### Type 7: Dual Type 1 and Type 2
This is a hybrid approach where some attributes are managed as Type 1 and others as Type 2 within the same dimension.

The choice of SCD type depends on the business requirements for historical data tracking and the complexity the organization is willing to manage. SCDs are implemented in ETL (Extract, Transform, Load) processes that populate and maintain data warehouses.