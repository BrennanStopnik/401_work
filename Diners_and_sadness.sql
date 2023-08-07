#1)
#a) create two tables: ‘diners’ with the columns ID (primary key, ascending from 1,2,3...), name, and order_id,
#and ‘orders’ with the columns ID (same as order_id), and food (eg chicken, bread). add 2-3 entries.
#b) join the two tables based on the common key: order_id
#c) run a select statement to output a list of all the customer names and associated food orders
#2)
#a) add a primary key to the tips table for each party. Label it ‘ID’
#b) Join the above table from question 1 to the tips table using a full outer join. You will have many null values and that is OK!
#c) Run a query with ‘Union’ to join select * results from all 3 tables: diners, orders, and tips. See how this compares to your answer from b). What differs?

CREATE SCHEMA Restaurants;

USE Restaurants;

CREATE TABLE diners (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    order_id INT
);

CREATE TABLE orders (
    ID INT PRIMARY KEY,
    food VARCHAR(255)
);

INSERT INTO orders (ID, food) VALUES (1, 'chicken');
INSERT INTO orders (ID, food) VALUES (2, 'bread');
INSERT INTO orders (ID, food) VALUES (3, 'steak');
INSERT INTO orders (ID, food) VALUES (4, 'broccoli');

INSERT INTO diners (ID, name, order_id) VALUES (1001, 'Brian', 1);
INSERT INTO diners (ID, name, order_id) VALUES (1002, 'Francis', 2);
INSERT INTO diners (ID, name, order_id) VALUES (1003, 'Betty', 3);
INSERT INTO diners (ID, name, order_id) VALUES (1004, 'Archibald', 4);


SELECT diners.ID, diners.name, orders.food
FROM diners
JOIN orders
ON diners.order_id = orders.ID;

select * from tips;

ALTER TABLE Restaurants.tips
ADD ID INT AUTO_INCREMENT PRIMARY KEY;

SELECT *
FROM diners
LEFT JOIN orders ON diners.order_id = orders.ID
LEFT JOIN tips ON diners.ID = tips.ID
UNION
SELECT *
FROM diners
RIGHT JOIN orders ON diners.order_id = orders.ID
RIGHT JOIN tips ON diners.ID = tips.ID;






