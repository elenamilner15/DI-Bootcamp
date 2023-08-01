-- Exercise 1: DVD Rental
-- Part I


-- create table customer (
--     id serial primary key,
--     first_name varchar(50) not null,
--     last_name varchar(50) not null
-- );

-- create table customerprofile (
--     id serial primary key,
--     isLoggedIn boolean default false,
--     customer_id integer references customer(id)
-- );

-- insert into customer (first_name, last_name)
-- values
--     ('John', 'Doe'),
--     ('Jerome', 'Lalu'),
--     ('Lea', 'Rive');


-- select customer.first_name, customerprofile.isLoggedIn from customer join customerprofile on customer.id = customerprofile.customer_id
-- where customerprofile.isLoggedIn = true;

-- select customer.first_name, customerprofile.isLoggedIn from customer left join customerprofile on customer.id = customerprofile.customer_id;

-- select count(*)as not_LoggedIn_customers from customer
-- left join customerprofile on customer.id = customerprofile.customer_id
-- where customerprofile.isLoggedIn != true;

--	!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--	 Part II:

-- create table book (
--     book_id serial primary key,
--     title varchar(255) not null,
--     author varchar(255) not null
-- );


-- insert into book (title, author)
-- values
--     ('Alice In Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K Rowling'),
--     ('To Kill a Mockingbird', 'Harper Lee');



-- create table student (
--     student_id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL UNIQUE,
--     age INTEGER CHECK (age <= 15)
-- );

-- insert into student (name, age)
-- values 
--     ('John', 12),
--     ('Lera', 11),
--     ('Patrick', 10),
--     ('Bob', 14);


-- CREATE TABLE Library (
--     book_fk_id INTEGER REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     student_fk_id INTEGER REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id)
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
--     ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
--     ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
--     ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- select student.name, book.title from student 
-- join library on student.student_id = library.student_fk_id
-- join book on book.book_id = library.book_fk_id;

-- select round(avg(student.age),1) from student 
-- join library on student.student_id = library.student_fk_id
-- join book on book.book_id = library.book_fk_id
-- where book.title ilike '%alice%';


-- 	DELETE FROM Student WHERE name = 'Bob';
--	!!!!!!!!!! 		Library was updated . There is no data about Bob anymore.



-- select * from student;

-- 	select * from library
