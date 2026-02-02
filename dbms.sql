CREATE DATABASE CDB;
USE CDB;

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    join_date DATE
);
INSERT INTO Employees VALUES
(101, 'Rohith', 22, 'IT', 35000.00, '2024-06-15'),
(102, 'Anjali', 25, 'HR', 30000.00, '2023-09-10'),
(103, 'Kiran', 28, 'Finance', 40000.00, '2022-12-01'),
(104, 'Sneha', 24, 'Marketing', 32000.00, '2024-01-20');
SELECT * FROM Employees WHERE age > 24;
UPDATE Employees SET salary = salary * 1.1 WHERE department = 'IT';
DELETE FROM Employees WHERE emp_id = 102;       
SELECT * FROM Employees;

CREATE TABLE staff_list (
    staff_id INT PRIMARY KEY,
    staff_name VARCHAR(50),
    position VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10,2)
);
INSERT INTO staff_list VALUES
(222,'Rohith','Manager','01/12/2002',50000.00),   
(224,'Kiran','Clerk','20/07/2019',35000.00),
(225,'Sneha','Executive','05/11/2021',45000.00);
SELECT * FROM staff_list WHERE position = 'Manager';
UPDATE staff_list SET salary = salary + 5000 WHERE staff_id = 223;
DELETE FROM staff_list WHERE staff_id = 224;




create table workers (
    worker_id INT primary key,
    worker_name VARCHAR(50),
    role VARCHAR(50),
    start_date DATE,
    wage DECIMAL(10,2)
    );
INSERT INTO workers VALUES
(301, 'rohith','owner','12/10/2025','10.5')
,(302, 'anjali','employee','15/08/2023','8.0')          
,(303, 'kiran','manager','20/05/2020','12.0');
SELECT * FROM workers WHERE wage > 9.0;