-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Exercise 1: DVD Rental
-- Instructions
-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.

-- Get a list of all the movies that have a rating of G or PG-13.
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- 	select rating, count(*) as num_films from film group by rating;
-- 	select * from film where rating in ('G', 'PG-13');
-- 	select * from film where rating in ('G', 'PG-13') and length <120 and rental_rate<3 order by title;
	
-- 	update customer
-- 	set first_name = 'Elena', last_name = 'Milner', email = 'elenamilner@sakilacustomer.org' where customer_id = 4;

-- 	update address
-- 	set address = '123 Rav Levi', district = 'Tel Aviv', city_id = (select city_id from city where city = 'Bat Yam') 
-- 	where address_id = (select address_id from customer where customer_id =4);


--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Exercise 2: Students Table
-- Instructions
-- Continuation of the Day1 Exercise XPGold : students table
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	
-- 	update students
-- 	set birth_date = '02/11/1998'
-- 	where last_name= 'Benichou';

-- 	update students
-- 	set last_name= 'Guez'
-- 	where first_name= 'David' and last_name= 'Grez';
	
-- 	delete from students
-- 	where first_name= 'Lea' and last_name= 'Benichou'
	
-- 	select count (*) from students;
-- 	select count (*) from students where birth_date > '01/01/2000';
	
-- 	alter table students
-- 	add column math_grade integer;

-- 	update students
-- 	set math_grade = 80
-- 	where id = 1;

-- 	update students
-- 	set math_grade = 90
-- 	where id in (2, 4);

-- 	update students
-- 	set math_grade = 40
-- 	where id = 6;

-- 	select count (*) from students where math_grade > 83;

-- insert into students (first_name, last_name, birth_date, math_grade)
-- values ('Omer', 'Simpson', (select birth_date from students where first_name = 'Omer' and last_name = 'Simpson'), 70);

--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. 
-- If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
-- Hint : Use GROUP BY.
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	

-- 	select first_name, last_name, count(*) as total_grade from students group by first_name, last_name;
	
-- 	select sum(math_grade) as total_sum from students;
	

--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Exercise 3 : Items And Customers
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- 	create table purchases(
-- 	id serial primary key,
-- 	customer_id integer references customers(id),
-- 	item_id integer references items (id),
-- 	quantity_purchased integer
-- 	);

-- insert into purchases (customer_id, item_id, quantity_purchased)
-- values (
--     (select id from customers where first_name = 'Scott' and last_name = 'Scott'),
--     (select id from items where name ilike 'fan'),
--     1
-- );
-- insert into purchases (customer_id, item_id, quantity_purchased)
-- values (
--     (select id from customers where first_name = 'Melanie' and last_name = 'Johnson'),
--     (select id from items where name ilike'large desk'),
--     10
-- );

-- insert into purchases (customer_id, item_id, quantity_purchased)
-- values (
--     (select id from customers where first_name = 'Greg' and last_name = 'Jones'),
--     (select id from items where name ilike'small desk'),
--     2
-- );
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- Part II
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- select * from purchases
-- select purchases.*, customers.first_name, customers.last_name from purchases 
-- join customers on purchases.customer_id = customers.id;
-- select * from purchases where customer_id=5;
-- select * from purchases where item_id = (select id from items where name ilike 'large desk') or item_id = (select id from items where name ilike 'small desk');

-- select customers.first_name, customers.last_name, items.name from purchases 
-- join customers on purchases.customer_id = customers.id join items on purchases.item_id = items.id;

-- insert into purchases (customer_id, item_id, quantity_purchased)
-- values (11, NULL, 5);