-- Create separate jan/feb sales views with customer ID’s and products
-- Create a unified view with all jan/feb sales and associated customer ID’s (return 2 columns only: CustomerID and Product

use new_table;

CREATE VIEW jan_sales_with_customers AS
SELECT c.CustomerID, s.Product
FROM new_table.customers2 AS c
JOIN new_table.sales_january_2019 AS s
ON c.OrderID = s.`Order ID`;

select * from jan_sales_with_customers;

CREATE VIEW feb_sales_with_customers AS
SELECT c.CustomerID, s.Product
FROM new_table.customers2 AS c
JOIN new_table.sales_february_2019 AS s
ON c.OrderID = s.`Order ID`;

select * from feb_sales_with_customers;

CREATE VIEW unified_jan_feb_sales AS
SELECT * FROM jan_sales_with_customers
UNION ALL
SELECT * FROM feb_sales_with_customers;

select * from unified_jan_feb_sales;







