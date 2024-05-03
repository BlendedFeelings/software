---
b: https://blendedfeelings.com/software/data-warehouse/architecture-layers.md
---

# Data warehouse architecture 
is a system that is designed to store, manage, and retrieve large volumes of data for analysis and reporting purposes. It typically consists of several layers, each with a specific function. Here are the common layers in a traditional data warehouse architecture:

1. **Data Source Layer:**
   - This is the layer where data originates. It includes various source systems such as operational databases, CRM systems, ERP systems, flat files, web logs, and external data sources.
   - Data extraction processes pull or receive data from these sources for further processing.

2. **Data Staging Layer:**
   - This layer serves as a temporary storage area where data from different sources is collected, cleansed, transformed, and prepared for loading into the data warehouse.
   - Tasks such as data cleaning, data integration, transformation, and ETL (Extract, Transform, Load) processes occur here.
   - The staging area is often a relational database designed to process large volumes of data efficiently.

3. **Data Storage Layer:**
   - Also known as the Data Warehouse Database Layer, this is where the processed data is stored for long-term retention.
   - It typically consists of a relational database designed to handle complex queries and large-scale analytics.
   - This layer may include a combination of fact tables, dimension tables, and aggregates, which are organized in schemas like star schema or snowflake schema.

4. **Data Presentation Layer:**
   - This layer organizes data into a format that is understandable and accessible to end-users for reporting and analysis.
   - It may include views, cubes, and virtual schemas that present data in a more business-friendly format.
   - The presentation layer often includes tools for creating reports, dashboards, and data visualizations.

5. **Data Access Layer:**
   - This layer provides mechanisms for users and applications to access the data stored in the data warehouse.
   - It includes query tools, reporting tools, analytical applications, and any other software that facilitates access to the data for business intelligence purposes.
   - Security and user authentication are also managed at this layer to ensure that access to data is controlled and monitored.

6. **Data Management Layer:**
   - This layer is responsible for maintaining the data warehouse's overall health and performance.
   - It includes tasks such as data warehouse administration, monitoring, backup and recovery, tuning, and capacity planning.
   - Data governance, data quality management, and metadata management are also part of this layer.

7. **Business Intelligence Tools Layer:**
   - While not always considered a separate layer, this includes the tools and applications that leverage the data in the warehouse to provide business insights.
   - It encompasses tools for reporting, online analytical processing (OLAP), data mining, predictive analytics, and more.

8. **Metadata Layer:**
   - This layer stores information about the data, such as its source, structure, transformations applied, and usage.
   - Metadata is essential for understanding the data's lineage, for auditing, and for simplifying the management of the data warehouse.

In modern data warehouse architectures, especially with the advent of cloud-based solutions and big data technologies, additional components such as data lakes, real-time streaming analytics, and advanced data processing frameworks may also be included. These elements expand the capabilities of traditional data warehouses to handle a wider variety of data types and to perform more sophisticated analytics.