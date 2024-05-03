---
b: https://blendedfeelings.com/software/data-warehouse/kimball.md
---

# Kimball Methodology 
also known as the Kimball Lifecycle, is a set of best practices for building data warehouses and business intelligence systems. It was developed by Ralph Kimball and is one of the most widely adopted methodologies for data warehousing. The Kimball Methodology emphasizes the importance of understanding the business requirements, designing data models that reflect the business processes, and delivering business intelligence iteratively to provide immediate value.

Here's an overview of how the Kimball Methodology can be applied in the context of big data:

1. **Business Requirements Analysis**: This step involves gathering detailed business requirements from stakeholders. In a big data context, this might include identifying the types of data sources (structured, semi-structured, or unstructured) and the volume, velocity, and variety of data.

2. **Data Source Identification**: Identify all potential data sources that will be needed to meet the business requirements. With big data, this could include traditional databases, as well as log files, social media feeds, sensor data, and more.

3. **Conceptual Data Modeling**: Create a high-level conceptual model that represents the business entities and relationships. In big data projects, conceptual modeling might need to accommodate more complex relationships and data types.

4. **Logical Data Modeling**: Develop a logical data model, typically in the form of a star schema or snowflake schema. The star schema consists of fact tables (representing business events) and dimension tables (contextual data). In big data, logical models must be scalable and often denormalized for performance.

5. **Physical Data Modeling**: Translate the logical model into a physical model that takes into account the specific technologies used for storage and processing, such as Hadoop, NoSQL databases, or data warehousing appliances. Considerations for big data include data partitioning, indexing, and storage formats.

6. **ETL Design and Development**: Design and develop the Extract, Transform, Load (ETL) processes that will move and transform data from source systems into the data warehouse. For big data, ETL processes may be replaced or augmented with ELT (Extract, Load, Transform) to leverage the processing power of big data platforms.

7. **Data Warehouse and Business Intelligence Application Development**: Develop the data warehouse, along with the business intelligence applications that will use it. This includes creating dashboards, reports, and analytics tools that can handle big data volumes and provide insights at scale.

8. **Deployment**: Deploy the data warehouse and BI applications into a production environment. With big data, this may involve cloud-based solutions or on-premises clusters that can handle the scale and complexity of the data.

9. **Operations and Maintenance**: Operate and maintain the data warehouse system, ensuring data quality, performance, and security. In a big data environment, this includes monitoring the health of big data platforms and ensuring they are optimized for performance.

10. **Business Intelligence Delivery**: Continuously deliver business intelligence to end-users, often through iterative enhancements and additions to the data warehouse and BI applications. This allows businesses to adapt to changing requirements and leverage new data sources as they become available.

The Kimball Methodology, with its focus on business needs and iterative development, can be adapted to the big data landscape, although it may require some modifications to account for the technical challenges and opportunities presented by big data technologies.