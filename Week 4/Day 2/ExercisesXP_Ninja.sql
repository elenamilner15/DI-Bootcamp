-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--	Exercise 1 : Bonus Public Database (Continuation Of XP)
--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- 	select first_name, last_name from customers order by last_name, first_name desc
-- 	limit 2;
-- 	delete from purchases where customer_id = (select id from customers where first_name = 'Scott')
-- select * from customers where first_name='Scott'
-- select * from purchases;
-- select purchases.*, items.*, customers.* from purchases 
-- right join items on purchases.customer_id = items.id 
-- right join customers on purchases.customer_id = customers.id;

-- select purchases.*, customers.* from purchases 
-- right join customers on purchases.customer_id = customers.id;
