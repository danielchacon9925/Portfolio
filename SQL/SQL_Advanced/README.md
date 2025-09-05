# SQL Advanced Challenge

---

## Project Overview

This project consists of 14 SQL exercises designed to practice advanced query commands, filtering, ordering, aggregation, and joins.  
The exercises use tables from a club database (`cd.facilities`, `cd.members`, `cd.bookings`) and cover common real-world tasks such as retrieving specific data, calculating totals, filtering by conditions, and combining information from multiple tables.

Below is a detailed explanation of each query:

---

### 1. Retrieve all facility information
The query uses `SELECT * FROM cd.facilities` to display every column of the facilities table, returning complete details for all facilities.

---

### 2. Facility names and costs
This query selects only `name` and `membercost` from `cd.facilities`, demonstrating how to limit results to specific columns. An alias is also applied for readability.

---

### 3. Facilities charging a fee
By filtering with `WHERE membercost > 0`, the query lists only facilities that charge members a fee, excluding free ones.

---

### 4. Facilities with low relative fees
This query compares `membercost` to `monthlymaintenance/50` and shows facilities where fees are small compared to upkeep costs.

---

### 5. Facilities containing “Tennis”
Using `LIKE 'Tennis%'`, this query retrieves all facilities whose names start with the word “Tennis.”

---

### 6. Specific facility IDs
The query retrieves facilities where `facid` equals 1 or 5 using `OR`, showing how to filter for multiple exact matches.

---

### 7. Members joining after September 2012
With `WHERE joindate >= '2012-09-01'`, the query lists members who joined on or after this date, returning ID, surname, first name, and join date.

---

### 8. Ordered list of surnames
This query sorts surnames in descending order with `ORDER BY surname DESC` and limits the result to 10 entries using `LIMIT`.

---

### 9. Last signup date
The query uses the aggregate function `MAX(joindate)` to return the most recent join date from the members table.

---

### 10. Count of expensive guest facilities
The query counts rows in `cd.facilities` where `guestcost >= 10`, using `COUNT(*)` to produce a single number.

---

### 11. Slots booked per facility in September 2012
By filtering dates between September 1 and October 1, 2012, and grouping by `facid`, this query sums `slots` for each facility and orders results by usage.

---

### 12. Facilities with more than 1000 slots booked
The query uses `GROUP BY` and `HAVING SUM(slots) > 1000` to display facilities that exceed 1000 bookings, demonstrating the use of conditions on grouped data.

---

### 13. Bookings for tennis courts on 2012-09-21
The query uses an `INNER JOIN` to combine facilities and bookings, filtering by tennis courts (IDs 0 and 1) and booking start times.  
⚠️ The condition currently selects bookings on or after 2012-09-22; to capture only 2012-09-21, the second filter should be corrected to `< '2012-09-22'`.

---

### 14. Bookings by “David Farrel”
Using an `INNER JOIN` between bookings and members, the query filters by `firstname = 'David'` and `surname = 'Farrel'` to show all of his booking start times.

---

## Key learnings

- **Entity relationships**: Queries involve three related entities:  
  - `cd.facilities` → Information about club facilities.  
  - `cd.members` → Information about members.  
  - `cd.bookings` → Records of facility reservations.  

- **Filtering data**: Using `WHERE`, `AND`, `OR`, and `LIKE` conditions to refine results.  

- **Aggregation**: Using functions like `SUM`, `COUNT`, `MAX` combined with `GROUP BY` and `HAVING` to perform calculations on grouped data.  

- **Sorting and limiting**: Applying `ORDER BY` with ascending/descending order and restricting results with `LIMIT`.  

- **Joins**: Leveraging `INNER JOIN` to combine data across tables using shared keys (`facid` and `memid`).  

- **Date handling**: Using date comparisons in `WHERE` clauses to filter records within specific time periods.  



## How to Run

- 1. Load the database into PostgreSQL.

- 2. Open your SQL client or command-line tool.

- 3. Copy and paste the queries to execute them.

- 4. Review the results to analyze customer, transaction, and film insights.