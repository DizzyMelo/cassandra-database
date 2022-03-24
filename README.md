# Overview

This software is a family tree where the user can add a person with information such as firt name, last name, date and place of birth, etc. 

In order to store information, Apache Cassandra was chosen as the database. The database is responsible for organizing the data, and handle all sorts of manipulation, such as insert, delete, update, and retrieve.

This software was written to show how to user Apache Cassandra as a database and how to connect with a software written in Python.

You can watch the software demo here: [Software Demo Video](https://youtu.be/znd6X1HB4Hc)

# Distributed Database

Apache Cassandra

The database contains 1 table and 1 type. The database, or keyspace as called in cassandra, has the following structure:

- Person (table):
    -   person_id uuid primary key
    -   first_name text
    -   last_name text
    -   date_of_birth datetime
    -   place_of_birth location
    -   father_id uuid
    -   mother_id uuid

- Location (type):
    -   country text
    -   state text
    -   city text

# Development Environment

* Visual Studio Code
* Docker 20.10.10
* Apache Cassandra 4.0.3
* Python 3.10.0
* cassandra-driver 3.25.0

# Useful Websites

* [Cassandra Official Website](https://cassandra.apache.org/_/index.html)
* [DataStax Cassandra Driver Documentation](https://docs.datastax.com/en/developer/python-driver/3.25/)

# Future Work

* Implement Person information update
* Add new tables to manage more detailed information related to whether the person is dead or alive
* Add new field to allow notes to be added to a person