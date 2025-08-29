# SQL JOIN Challenge
This SQL code is a solution to a JOIN challenge, demonstrating how to combine data from multiple tables in a relational database. It tackles two distinct scenarios: finding customer emails based on their location and listing movies featuring a specific actor.

---

## Project Overview

This project is a practical exercise in using SQL to query a relational database. It focuses on the JOIN clause, which is fundamental for combining data from multiple tables. The two challenges presented simulate real-world scenarios: one involves retrieving customer information for a targeted email campaign, and the other requires finding specific movie data for a customer.

---

## Key learnings

- **Connecting customer and address data**: The first query uses INNER JOIN to link the customer and address tables. By matching customer.customer_id and address.address_id, it retrieves the emails of customers whose district is 'California'. This is a common use case for targeted communication.

- **Joining three tables for complex queries**: The second query demonstrates a more complex join by linking three tables: film_actor, actor, and film. It first joins film_actor with actor on actor_id to find the actor's full name, then joins the result with the film table on film_id to get the movie titles. This multi-join technique is crucial for answering questions that require data from several related entities.

---

## How to Run

- 1. Load the database into PostgreSQL.

- 2. Open your SQL client or command-line tool.

- 3. Copy and paste the queries to execute them.

- 4. Review the results to analyze customer, transaction, and film insights.