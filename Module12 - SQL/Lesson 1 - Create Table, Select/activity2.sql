-- 1) Create a table for Salesman details:
--    a) Use `CREATE TABLE IF NOT EXISTS` to avoid errors if the table already exists.
--    b) Add columns for id, name, city, and commission.
--    c) Set the id column as `PRIMARY KEY`.

CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

-- 2) Insert sample records into the Salesman table:
--    a) Use a single `INSERT INTO ... VALUES` with multiple rows.

INSERT INTO Salesman (Salesman_id, name, city, Comission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);


-- 3) Display all records from the Salesman table:
--    a) Use `SELECT * FROM Salesman;`

SELECT * FROM Salesman;

-- 4) Create a table for Orders details:
--    a) Use `CREATE TABLE IF NOT EXISTS`.
--    b) Add columns for order number, purchase amount, order date, customer id, and salesman id.
--    c) Set the order number as `PRIMARY KEY`.

CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    Salesman_id TEXT
);


-- 5) Insert sample records into the Orders table:
--    a) Use `INSERT INTO ... VALUES` with multiple rows.

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 2400.6, '2012-07-27', '3007', '5006');


-- 6) Display all records from the Orders table:
--    a) Use `SELECT * FROM Orders;`

SELECT * FROM Orders;

-- 7) Select specific columns from Salesman table:
--    a) Use `SELECT name, Comission FROM Salesman;` to show only name and commission.

SELECT name, Comission
FROM Salesman;