-- Exercise 1: DVD Rental

-- select * from language
-- select * from film;

-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- select film.title, film.description, language.name as lang 
-- from film left join language on film.language_id= language.language_id;

-- select film.title, film.description, language.name as lang 
-- from film right join language on film.language_id= language.language_id 

-- select title, language_id from film order by language_id desc;


-- create table new_film (
-- id integer primary key,
-- name varchar (50)
-- );

-- INSERT INTO new_film (id, name) VALUES
-- (1, 'Dune'),
-- (2, 'Lost highway'),
-- (3, 'The good, the bad and the ugly'),
-- (4, 'Pulp Fiction'),
-- (5, 'Interstellar');

-- create table customer_review(
-- review_id integer primary key,
-- film_id integer references new_film (id) ON DELETE CASCADE,
-- language_id integer references language (language_id),
-- title  varchar (50),
-- score smallint CHECK (score BETWEEN 1 AND 10),
-- review_text text,
-- last_update TIMESTAMP
-- );


-- INSERT INTO customer_review (review_id, film_id, language_id, title, score, review_text, last_update)
-- VALUES(1, 1, 1, 'Amazing Movie!', 9, 'Amazing Movie! XXXXXXXXXXXXXXXXXXX XXXXXXXXXXXXX XXXXXXXXXXXXXXXX. Highly recommended!', CURRENT_TIMESTAMP);

-- INSERT INTO customer_review (review_id, film_id, language_id, title, score, review_text, last_update)
-- VALUES(2, 1, 2, 'Sharman!!!', 9, 'Sharman! Sharman!', CURRENT_TIMESTAMP);


-- INSERT INTO customer_review (review_id, film_id, language_id, title, score, review_text, last_update)
-- VALUES(3, 5, 1, 'fgrtgr!!!', 9, 'rtretr gjtyuty ftgjtytr', CURRENT_TIMESTAMP);

--  delete from new_film where id=5;
--!!!!!!!!!!!!!!!! review #3 on film id=5 was deleted from customer_review table !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

--  Exercise 2 : DVD Rental

--!!!!!!!!!!!!!!!! 
-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- update film
-- set language_id = 2 where film_id BETWEEN 5 and 10;
-- update film
-- set language_id = 3 where film_id BETWEEN 15 and 20;
-- update film
-- set language_id = 4 where film_id BETWEEN 25 and 30;

-- !!!!!!!!!!!!!!!!
-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- store id, address_id
-- Data inserted into columns store id and address_id in "Customer" table 
-- must be valid and exist in the referenced tables (store and address). Otherwise, there will be an error.

-- !!!!!!!!!!!!!!!!
-- 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- 	drop table customer_review;

-- On this step shoul be considered:
-- Data Loss. All data of dropping table will be lost.
-- Cascading Deletes: if dropping table has foreign key relationships with other tables could be cascading deletes.

-- !!!!!!!!!!!!!!!!
-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- select count (*) as Number_of_films_to_return from rental where return_date is Null;

-- 183
-- !!!!!!!!!!!!!!!!
-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- select * from film where film_id in 
-- (select film_id from inventory where inventory_id in 
--  (select inventory_id from rental where return_date is Null)) order by replacement_cost limit 30;
 
 -- !!!!!!!!!!!!!!!!
--  6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
--  but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
 
 -- !!!!!!!!!!!!!!!!
 
-- select * from film 
-- where film_id in (select film_id from film_actor 
-- where actor_id = (select actor_id from actor where first_name ilike 'Penelope' and last_name ilike 'Monroe')) 
-- and description ilike '%sumo%';

 -- !!!!!!!!!!!!!!!!

-- select * from film where rating= 'R' and length<120 and description ilike '%documentary%';

 -- !!!!!!!!!!!!!!!!

-- select * from film where film_id =
-- (select film_id from inventory where inventory_id = 
-- (select inventory_id from rental where rental_id in (select rental_id from payment where customer_id =
-- (select customer_id from customer where first_name = 'Matthew' and last_name ='Mahan')
-- and amount>4) and return_date BETWEEN '2005-07-28' AND '2005-08-01'));

 -- !!!!!!!!!!!!!!!!

-- SELECT MAX(replacement_cost) AS max_replacement_cost FROM film where film_id in 
-- (select film_id from inventory where inventory_id in 	
-- (select inventory_id from rental where rental_id in (select rental_id from payment where customer_id =
-- (select customer_id from customer where first_name = 'Matthew' and last_name ='Mahan'))))
-- and description ilike '%boat%' or title ilike '%boat%'

 -- !!!!!!!!!!!!!!!!




