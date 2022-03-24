-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS familytree WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };


CREATE TYPE IF NOT EXISTS familytree.location (
    country text,
    state text,
    city text
);

-- Create a table
CREATE TABLE IF NOT EXISTS familytree.person (
    person_id uuid PRIMARY KEY,
    first_name text,
    last_name text,
    date_of_birth date,
    place_of_birth frozen<location>,
    father_id uuid,
    mother_id uuid
);

-- Insert some data
INSERT INTO familytree.person (person_id, first_name, last_name, date_of_birth, place_of_birth, father_id, mother_id) VALUES ();


-- INSERT INTO familytree.person JSON '{"person_id": "67532436", "root_person": {"first_name":"Daniel", "last_name": "Melo", "date_of_birth":"1994-10-20", "place_of_birth": {"country":"Brazil", "state": "Sao Paulo", "city": "Sao Paulo"}}, "father": {"first_name":"Valdir", "last_name": "Melo", "date_of_birth":"1994-10-20", "place_of_birth": {"country":"Brazil", "state": "Sao Paulo", "city": "Sao Paulo"}}, "mother": {"first_name":"Izabel", "last_name": "Melo", "date_of_birth":"1994-10-20", "place_of_birth": {"country":"Brazil", "state": "Sao Paulo", "city": "Sao Paulo"}}}';



INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('1234', 5, toTimeStamp(now()));