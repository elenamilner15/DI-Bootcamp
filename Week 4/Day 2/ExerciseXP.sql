-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--  Exercise 1 : Items And Customers
-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)


-- 	select * from items order by price;
-- 	select * from items where price >=80 order by price;
-- 	select * from customers order by price;
-- 	select * from customers order by first_name limit 3;
-- 	select last_name from customers order by last_name;
	
-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
-- Exercise 2 : Dvdrental Database

--  select * from customer;
-- 	select concat(first_name, ' ', last_name) as full_name from customer;
-- 	select distinct create_date from customer;
-- 	select * from customer order by first_name desc;
-- 	select * from film;
-- 	select film_id, title, description, release_year, rental_rate from film order by rental_rate;
-- 	select * from address;
-- 	select address, phone from address where district ='Texas'
-- 	select * from film where film_id in (15, 150);
-- 	select film_id, title, description, length, rental_rate from film where title ilike '%nightmare on the elm street%';
-- 	select film_id, title, description, length, rental_rate from film where title ilike 'ni%';
-- 	select * from film order by replacement_cost limit 10;
-- 	select * from film order by replacement_cost offset 10 rows fetch next 10 rows only;

-- 	select customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer join payment on customer.customer_id = payment.customer_id order by customer.customer_id;
-- 	select *from film right join inventory on film.film_id=inventory.film_id where inventory.film_id is null;
-- 	select city.city, country.country from city join country on city.country_id=country.country_id;

-- !!!!!!!!!!!!!!!!!!!!!
-- Bonus You want to be able to see how your sellers have been doing? 
-- Write a query to get the customer’s id, names (first and last), the amount and the date of payment 
-- ordered by the id of the staff member who sold them the dvd.
	
	select customer.first_name, customer.last_name, payment.amount, payment.payment_date, payment.staff_id from customer join payment on customer.customer_id = payment.customer_id order by payment.staff_id;
