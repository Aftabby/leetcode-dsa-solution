-- problem_name = Combine Two Tables
-- problem_source = https://leetcode.com/problems/combine-two-tables/description/

-- Algo
--     -

-- ! SQL Schema
Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255));
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255));
DELETE FROM Person;
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');
DELETE FROM Address;
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');

-- % Actual Answer below
-- ! Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person as p
LEFT JOIN Address as a ON p.personId = a.personId;
