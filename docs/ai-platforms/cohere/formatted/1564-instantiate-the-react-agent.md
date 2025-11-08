---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## instantiate the ReAct agent

agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )
```
```python PYTHON
output=agent_executor.invoke({
   "input": 'what tables are available?',
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the sql_db_list_tables tool to find out which tables are available.
{'tool_name': 'sql_db_list_tables', 'parameters': {'tool_input': ''}}
[0m[38;5;200m[1;3mAlbum, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The following tables are available: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track.
Grounded answer: The following tables are available: <co: 0="">Album</co:>, <co: 0="">Artist</co:>, <co: 0="">Customer</co:>, <co: 0="">Employee</co:>, <co: 0="">Genre</co:>, <co: 0="">Invoice</co:>, <co: 0="">InvoiceLine</co:>, <co: 0="">MediaType</co:>, <co: 0="">Playlist</co:>, <co: 0="">PlaylistTrack</co:>, <co: 0="">Track</co:>.[0m

[1m> Finished chain.[0m
```
```python PYTHON
print(output['output'])
```
```txt title="Output"
The following tables are available: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track.
```
The agent uses the list\_tables tool to effectively highlight all the tables in the DB.
```python PYTHON
output=agent_executor.invoke({
   "input": 'show the first row of the Playlist and Genre tables?',
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the sql_db_schema tool to find the first row of the Playlist and Genre tables.
{'tool_name': 'sql_db_schema', 'parameters': {'table_names': 'Playlist, Genre'}}
[0m[33;1m[1;3m
CREATE TABLE "Genre" (
    "GenreId" INTEGER NOT NULL,
    "Name" NVARCHAR(120),
    PRIMARY KEY ("GenreId")
)

/*
3 rows from Genre table:
GenreId	Name
1	Rock
2	Jazz
3	Metal
*/


CREATE TABLE "Playlist" (
    "PlaylistId" INTEGER NOT NULL,
    "Name" NVARCHAR(120),
    PRIMARY KEY ("PlaylistId")
)

/*
3 rows from Playlist table:
PlaylistId	Name
1	Music
2	Movies
3	TV Shows
*/[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: Here is the first row of the Genre table:

| GenreId | Name |
|---|---|
| 1 | Rock |

Here is the first row of the Playlist table:

| PlaylistId | Name |
|---|---|
| 1 | Music |
Grounded answer: Here is the first row of the Genre table:

| <co: 0="">GenreId</co:> | <co: 0="">Name</co:> |
|---|---|
| <co: 0="">1</co:> | <co: 0="">Rock</co:> |

Here is the first row of the Playlist table:

| <co: 0="">PlaylistId</co:> | <co: 0="">Name</co:> |
|---|---|
| <co: 0="">1</co:> | <co: 0="">Music</co:> |[0m

[1m> Finished chain.[0m
```
```python PYTHON
print(output['output'])
```
```txt title="Output"
Here is the first row of the Genre table:

| GenreId | Name |
|---|---|
| 1 | Rock |

Here is the first row of the Playlist table:

| PlaylistId | Name |
|---|---|
| 1 | Music |
```
Here we see that the tool takes a list of tables to query the sql\_db\_schema tool to retrieve the various schemas.
```python PYTHON
output=agent_executor.invoke({
   "input": 'which countries have the most invoices?',
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for the number of invoices per country and then write an answer.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT country, COUNT(*) AS invoice_count FROM invoices GROUP BY country ORDER BY invoice_count DESC'}}
[0m[36;1m[1;3mError: (sqlite3.OperationalError) no such table: invoices
[SQL: SELECT country, COUNT(*) AS invoice_count FROM invoices GROUP BY country ORDER BY invoice_count DESC]
(Background on this error at: https://sqlalche.me/e/20/e3q8)[0m[32;1m[1;3m
I received an error message. I will now use the sql_db_list_tables tool to find out the correct table name.
{'tool_name': 'sql_db_list_tables', 'parameters': {'tool_input': ''}}
[0m[38;5;200m[1;3mAlbum, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track[0m[32;1m[1;3m
I found out that the correct table name is 'Invoice'. I will now rewrite my query and run it again.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT country, COUNT(*) AS invoice_count FROM Invoice GROUP BY country ORDER BY invoice_count DESC'}}
[0m[36;1m[1;3mError: (sqlite3.OperationalError) no such column: country
[SQL: SELECT country, COUNT(*) AS invoice_count FROM Invoice GROUP BY country ORDER BY invoice_count DESC]
(Background on this error at: https://sqlalche.me/e/20/e3q8)[0m[32;1m[1;3m
I received another error message. I will now use the sql_db_schema tool to find out the correct column name.
{'tool_name': 'sql_db_schema', 'parameters': {'table_names': 'Invoice'}}
[0m[33;1m[1;3m
CREATE TABLE "Invoice" (
    "InvoiceId" INTEGER NOT NULL,
    "CustomerId" INTEGER NOT NULL,
    "InvoiceDate" DATETIME NOT NULL,
    "BillingAddress" NVARCHAR(70),
    "BillingCity" NVARCHAR(40),
    "BillingState" NVARCHAR(40),
    "BillingCountry" NVARCHAR(40),
    "BillingPostalCode" NVARCHAR(10),
    "Total" NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY ("InvoiceId"),
    FOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId")
)

/*
3 rows from Invoice table:
InvoiceId	CustomerId	InvoiceDate	BillingAddress	BillingCity	BillingState	BillingCountry	BillingPostalCode	Total
1	2	2021-01-01 00:00:00	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	1.98
2	4	2021-01-02 00:00:00	Ullevålsveien 14	Oslo	None	Norway	0171	3.96
3	8	2021-01-03 00:00:00	Grétrystraat 63	Brussels	None	Belgium	1000	5.94
*/[0m[32;1m[1;3m
I found out that the correct column name is 'BillingCountry'. I will now rewrite my query and run it again.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT BillingCountry AS country, COUNT(*) AS invoice_count FROM Invoice GROUP BY BillingCountry ORDER BY invoice_count DESC'}}
[0m[36;1m[1;3m[('USA', 91), ('Canada', 56), ('France', 35), ('Brazil', 35), ('Germany', 28), ('United Kingdom', 21), ('Portugal', 14), ('Czech Republic', 14), ('India', 13), ('Sweden', 7), ('Spain', 7), ('Poland', 7), ('Norway', 7), ('Netherlands', 7), ('Italy', 7), ('Ireland', 7), ('Hungary', 7), ('Finland', 7), ('Denmark', 7), ('Chile', 7), ('Belgium', 7), ('Austria', 7), ('Australia', 7), ('Argentina', 7)][0m[32;1m[1;3mRelevant Documents: 1,3,4
Cited Documents: 4
Answer: The countries with the most invoices are the USA (91), Canada (56), and France (35).
Grounded answer: The countries with the most invoices are the <co: 4="">USA (91</co:>), <co: 4="">Canada (56</co:>), and <co: 4="">France (35</co:>).[0m

[1m> Finished chain.[0m
```
```python PYTHON
print(output['output'])
```
```txt title="Output"
The countries with the most invoices are the USA (91), Canada (56), and France (35).
```
The agent initially makes some errors as it jumps to answer the question using the db\_query tool, but it then realizes it needs to figure out what tables it has access to and what they look like. It then fixes the SQL code and is able to generate the right answer.
```python PYTHON
output=agent_executor.invoke({
   "input": 'who is the best customer? The customer who has spent the most money is the best.',
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will run a SQL query to find the customer who has spent the most money.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT customer_name, SUM(total_cost) AS total_spent FROM orders GROUP BY customer_name ORDER BY total_spent DESC LIMIT 1;'}}
[0m[36;1m[1;3mError: (sqlite3.OperationalError) no such table: orders
[SQL: SELECT customer_name, SUM(total_cost) AS total_spent FROM orders GROUP BY customer_name ORDER BY total_spent DESC LIMIT 1;]
(Background on this error at: https://sqlalche.me/e/20/e3q8)[0m[32;1m[1;3m
I received an error message saying that there is no table called 'orders'. I will now use the sql_db_list_tables tool to find out what tables are available.
{'tool_name': 'sql_db_list_tables', 'parameters': {'tool_input': ''}}
[0m[38;5;200m[1;3mAlbum, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track[0m[32;1m[1;3m
I found that there is a table called 'Customer'. I will now use the sql_db_schema tool to find out what columns are in the 'Customer' table.
{'tool_name': 'sql_db_schema', 'parameters': {'table_names': 'Customer'}}
[0m[33;1m[1;3m
CREATE TABLE "Customer" (
    "CustomerId" INTEGER NOT NULL,
    "FirstName" NVARCHAR(40) NOT NULL,
    "LastName" NVARCHAR(20) NOT NULL,
    "Company" NVARCHAR(80),
    "Address" NVARCHAR(70),
    "City" NVARCHAR(40),
    "State" NVARCHAR(40),
    "Country" NVARCHAR(40),
    "PostalCode" NVARCHAR(10),
    "Phone" NVARCHAR(24),
    "Fax" NVARCHAR(24),
    "Email" NVARCHAR(60) NOT NULL,
    "SupportRepId" INTEGER,
    PRIMARY KEY ("CustomerId"),
    FOREIGN KEY("SupportRepId") REFERENCES "Employee" ("EmployeeId")
)

/*
3 rows from Customer table:
CustomerId	FirstName	LastName	Company	Address	City	State	Country	PostalCode	Phone	Fax	Email	SupportRepId
1	Luís	Gonçalves	Embraer - Empresa Brasileira de Aeronáutica S.A.	Av. Brigadeiro Faria Lima, 2170	São José dos Campos	SP	Brazil	12227-000	+55 (12) 3923-5555	+55 (12) 3923-5566	luisg@embraer.com.br	3
2	Leonie	Köhler	None	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	+49 0711 2842222	None	leonekohler@surfeu.de	5
3	François	Tremblay	None	1498 rue Bélanger	Montréal	QC	Canada	H2G 1A7	+1 (514) 721-4711	None	ftremblay@gmail.com	3
*/[0m[32;1m[1;3m
I found that the 'Customer' table does not contain any information about how much money a customer has spent. I will now use the sql_db_schema tool to find out what columns are in the 'Invoice' table.
{'tool_name': 'sql_db_schema', 'parameters': {'table_names': 'Invoice'}}
[0m[33;1m[1;3m
CREATE TABLE "Invoice" (
    "InvoiceId" INTEGER NOT NULL,
    "CustomerId" INTEGER NOT NULL,
    "InvoiceDate" DATETIME NOT NULL,
    "BillingAddress" NVARCHAR(70),
    "BillingCity" NVARCHAR(40),
    "BillingState" NVARCHAR(40),
    "BillingCountry" NVARCHAR(40),
    "BillingPostalCode" NVARCHAR(10),
    "Total" NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY ("InvoiceId"),
    FOREIGN KEY("CustomerId") REFERENCES "Customer" ("CustomerId")
)

/*
3 rows from Invoice table:
InvoiceId	CustomerId	InvoiceDate	BillingAddress	BillingCity	BillingState	BillingCountry	BillingPostalCode	Total
1	2	2021-01-01 00:00:00	Theodor-Heuss-Straße 34	Stuttgart	None	Germany	70174	1.98
2	4	2021-01-02 00:00:00	Ullevålsveien 14	Oslo	None	Norway	0171	3.96
3	8	2021-01-03 00:00:00	Grétrystraat 63	Brussels	None	Belgium	1000	5.94
*/[0m[32;1m[1;3m
I found that the 'Invoice' table contains a 'Total' column, which is likely to be the total amount spent by the customer on that invoice. I will now use the sql_db_query tool to find the customer who has spent the most money.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT c.FirstName, c.LastName, SUM(i.Total) AS total_spent FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId ORDER BY total_spent DESC LIMIT 1;'}}
[0m[36;1m[1;3m[('Helena', 'Holý', 49.62)][0m[32;1m[1;3mRelevant Documents: 1,2,3,4
Cited Documents: 4
Answer: The best customer is Helena Holý, who has spent a total of 49.62.
Grounded answer: The best customer is <co: 4="">Helena Holý</co:>, who has spent a total of <co: 4="">49.62</co:>.[0m

[1m> Finished chain.[0m
```
```python PYTHON
print(output['output'])
```
```txt title="Output"
The best customer is Helena Holý, who has spent a total of 49.62.
```
As you can see, the agent makes an error, but is able to rectify itself. It also manages to generate a SQL query over two tables in the database.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
