**Navigation:** [← Previous](./18-employing-a-smaller-context-window-also-has-the-ad.md) | [Index](./index.md) | [Next →](./20-deploy-your-finetuned-model-on-aws-marketplace.md)

---

# instantiate the ReAct agent
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

# SQL Agent with context \[#sec\_step2]

Generally, passing in additional context to the system instruction (preamble) can help reduce the initial failures. This context is provided by the SQLDBToolkit and contains the first 3 rows of the tables in the Database.

```python PYTHON
print('**Context to pass to LLM on tables**')
print('Table Names')
print(context['table_names'])
print('Table Schemas')
print(context['table_info'])
```

```sql title="Output"
**Context to pass to LLM on tables**
Table Names
Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
Table Schemas

CREATE TABLE "Album" (
    "AlbumId" INTEGER NOT NULL,
    "Title" NVARCHAR(160) NOT NULL,
    "ArtistId" INTEGER NOT NULL,
    PRIMARY KEY ("AlbumId"),
    FOREIGN KEY("ArtistId") REFERENCES "Artist" ("ArtistId")
)

/*
3 rows from Album table:
AlbumId	Title	ArtistId
1	For Those About To Rock We Salute You	1
2	Balls to the Wall	2
3	Restless and Wild	2
*/


CREATE TABLE "Artist" (
    "ArtistId" INTEGER NOT NULL,
    "Name" NVARCHAR(120),
    PRIMARY KEY ("ArtistId")
)

/*
3 rows from Artist table:
ArtistId	Name
1	AC/DC
2	Accept
3	Aerosmith
*/


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
*/


CREATE TABLE "Employee" (
    "EmployeeId" INTEGER NOT NULL,
    "LastName" NVARCHAR(20) NOT NULL,
    "FirstName" NVARCHAR(20) NOT NULL,
    "Title" NVARCHAR(30),
    "ReportsTo" INTEGER,
    "BirthDate" DATETIME,
    "HireDate" DATETIME,
    "Address" NVARCHAR(70),
    "City" NVARCHAR(40),
    "State" NVARCHAR(40),
    "Country" NVARCHAR(40),
    "PostalCode" NVARCHAR(10),
    "Phone" NVARCHAR(24),
    "Fax" NVARCHAR(24),
    "Email" NVARCHAR(60),
    PRIMARY KEY ("EmployeeId"),
    FOREIGN KEY("ReportsTo") REFERENCES "Employee" ("EmployeeId")
)

/*
3 rows from Employee table:
EmployeeId	LastName	FirstName	Title	ReportsTo	BirthDate	HireDate	Address	City	State	Country	PostalCode	Phone	Fax	Email
1	Adams	Andrew	General Manager	None	1962-02-18 00:00:00	2002-08-14 00:00:00	11120 Jasper Ave NW	Edmonton	AB	Canada	T5K 2N1	+1 (780) 428-9482	+1 (780) 428-3457	andrew@chinookcorp.com
2	Edwards	Nancy	Sales Manager	1	1958-12-08 00:00:00	2002-05-01 00:00:00	825 8 Ave SW	Calgary	AB	Canada	T2P 2T3	+1 (403) 262-3443	+1 (403) 262-3322	nancy@chinookcorp.com
3	Peacock	Jane	Sales Support Agent	2	1973-08-29 00:00:00	2002-04-01 00:00:00	1111 6 Ave SW	Calgary	AB	Canada	T2P 5M5	+1 (403) 262-3443	+1 (403) 262-6712	jane@chinookcorp.com
*/


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
*/


CREATE TABLE "InvoiceLine" (
    "InvoiceLineId" INTEGER NOT NULL,
    "InvoiceId" INTEGER NOT NULL,
    "TrackId" INTEGER NOT NULL,
    "UnitPrice" NUMERIC(10, 2) NOT NULL,
    "Quantity" INTEGER NOT NULL,
    PRIMARY KEY ("InvoiceLineId"),
    FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"),
    FOREIGN KEY("InvoiceId") REFERENCES "Invoice" ("InvoiceId")
)

/*
3 rows from InvoiceLine table:
InvoiceLineId	InvoiceId	TrackId	UnitPrice	Quantity
1	1	2	0.99	1
2	1	4	0.99	1
3	2	6	0.99	1
*/


CREATE TABLE "MediaType" (
    "MediaTypeId" INTEGER NOT NULL,
    "Name" NVARCHAR(120),
    PRIMARY KEY ("MediaTypeId")
)

/*
3 rows from MediaType table:
MediaTypeId	Name
1	MPEG audio file
2	Protected AAC audio file
3	Protected MPEG-4 video file
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
*/


CREATE TABLE "PlaylistTrack" (
    "PlaylistId" INTEGER NOT NULL,
    "TrackId" INTEGER NOT NULL,
    PRIMARY KEY ("PlaylistId", "TrackId"),
    FOREIGN KEY("TrackId") REFERENCES "Track" ("TrackId"),
    FOREIGN KEY("PlaylistId") REFERENCES "Playlist" ("PlaylistId")
)

/*
3 rows from PlaylistTrack table:
PlaylistId	TrackId
1	3402
1	3389
1	3390
*/


CREATE TABLE "Track" (
    "TrackId" INTEGER NOT NULL,
    "Name" NVARCHAR(200) NOT NULL,
    "AlbumId" INTEGER,
    "MediaTypeId" INTEGER NOT NULL,
    "GenreId" INTEGER,
    "Composer" NVARCHAR(220),
    "Milliseconds" INTEGER NOT NULL,
    "Bytes" INTEGER,
    "UnitPrice" NUMERIC(10, 2) NOT NULL,
    PRIMARY KEY ("TrackId"),
    FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"),
    FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"),
    FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId")
)

/*
3 rows from Track table:
TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
2	Balls to the Wall	2	2	1	U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann	342562	5510424	0.99
3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Hoffman	230619	3990994	0.99
*/
```

We can pass this context into the system instruction (preamble) and re-run a query to see how it performs.

```python PYTHON
preamble="""## Task And Context
You use your advanced complex reasoning capabilities to help people by answering their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You may need to use multiple tools in parallel or sequentially to complete your task. You should focus on serving the user's needs as best you can, which will be wide-ranging.

## Style Guide
Unless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.

## Additional Information
You are an expert who answers the user's question by creating SQL queries and executing them.
You are equipped with a number of relevant SQL tools.

Here is information about the database:
{schema_info}
""".format(schema_info=context)
```

```python PYTHON
output=agent_executor.invoke({
   "input": 'provide the name of the best customer? The customer who has spent the most money is the best.',
   "preamble": preamble
})
```

```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write a SQL query to find the customer who has spent the most money.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId ORDER BY TotalSpent DESC LIMIT 1;'}}
[0m[36;1m[1;3m[('Helena', 'Holý', 49.62)][0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The customer who has spent the most money is Helena Holý.
Grounded answer: The customer who has spent the most money is <co: 0="">Helena Holý</co:>.[0m

[1m> Finished chain.[0m
```

```python PYTHON
print(output['output'])
```

```txt title="Output"
The customer who has spent the most money is Helena Holý.
```

We can see that passing that additional context actually avoids the error seen in the previous section and gets to the answer in one tool call. This works as long as you have a few tables and a few columns per table. We will follow up with more techniques to improve stability and scalability in future work.


# Evaluating Text Summarization Models

> This page discusses how to evaluate a model's text summarization.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Summarization_Evals.ipynb" />

In this cookbook, we will be demonstrating an approach we use for evaluating summarization tasks using LLM evaluation.

# Get Started \[#start]

You'll need a Cohere API key to run this notebook. If you don't have a key, head to [https://cohere.com/](https://cohere.com/) to generate your key.

```python PYTHON
!pip install cohere datasets --quiet
```

```python PYTHON
import json
import random
import re
from typing import List, Optional

import cohere
from getpass import getpass
from datasets import load_dataset
import pandas as pd

co_api_key = getpass("Enter your Cohere API key: ")
co_model = "command-r"
co = cohere.Client(api_key=co_api_key)
```

As test data, we'll use transcripts from the [QMSum dataset](https://github.com/Yale-LILY/QMSum). Note that in addition to the transcripts, this dataset also contains reference summaries -- we will use only the transcripts as our approach is reference-free.

```python PYTHON
qmsum = load_dataset("MocktaiLEngineer/qmsum-processed", split="validation")
transcripts = [x for x in qmsum["meeting_transcript"] if x is not None]
```

```txt title="Output"
Generating train split:   0%|          | 0/1095 [00:00<?, ? examples/s]



Generating validation split:   0%|          | 0/237 [00:00<?, ? examples/s]



Generating test split:   0%|          | 0/244 [00:00<?, ? examples/s]
```

# Construct the evaluation dataset \[#dataset]

We are interested in evaluating summarization in real-world, enterprise use cases, which typically have two distinguishing features as compared to academic summarization benchmarks:

* Enterprise use cases often focus on specific summarization objectives, e.g. "summarize action items".
* Enterprise use cases often feature specific instruction constraints, e.g. "summarize in bullets with each bullet under 20 words".

Therefore, we must first create a dataset that contains diverse summarization prompts. We will do this programmatically by building prompts from their components, as defined below:

* Prompt = text (e.g. transcript to be summarized) + instruction
* Instruction = instruction objective (e.g. "summarize action items") + modifiers
* Modifiers = format/length modifiers (e.g. "use bullets") + style/tone modifiers (e.g. "do not mention names") + ...

First, we define the prompt that combines the text and instructions. Here, we use a very basic prompt:

```python PYTHON
prompt_template = """## meeting transcript
{transcript}

## instructions
{instructions}"""
```

Next, we build the instructions. Because each instruction may have a different objective and modifiers, we track them using metadata. This will later be required for evaluation (i.e. to know what the prompt is asking).

```python PYTHON

instruction_objectives = {
    "general_summarization": "Summarize the meeting based on the transcript.",
    "action_items": "What are the follow-up items based on the meeting transcript?",
}

format_length_modifiers = {
    "paragraphs_short": {
        "text": "In paragraph form, output your response. Use at least 10 words and at most 50 words in total.",
        "objectives": ["general_summarization"],
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 10,
            "max_length": 50,
        },
    },
    "paragraphs_medium": {
        "text": "Return the answer in the form of paragraphs. Make sure your answer is between 50 and 200 words long.",
        "objectives": ["general_summarization"],
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 50,
            "max_length": 200,
        },
    },
    "bullets_short_3": {
        "text": "Format your answer in the form of bullets. Use exactly 3 bullets. Each bullet should be at least 10 words and at most 20 words.",
        "objectives": ["general_summarization", "action_items"],
        "eval_metadata": {
            "format": "bullets",
            "number": 3,
            "min_length": 10,
            "max_length": 20,
        },
    },
    "bullets_medium_2": {
        "text": "In bullets, output your response. Make sure to use exactly 2 bullets. Make sure each bullet is between 20 and 80 words long.",
        "objectives": ["general_summarization", "action_items"],
        "eval_metadata": {
            "format": "bullets",
            "number": 2,
            "min_length": 20,
            "max_length": 80,
        },
    },
}
```

Let's combine the objectives and format/length modifiers to finish building the instructions.

```python PYTHON
instructions = []
for obj_name, obj_text in instruction_objectives.items():
    for mod_data in format_length_modifiers.values():
        for mod_obj in mod_data["objectives"]:
            if mod_obj == obj_name:
                instruction = {
                        "instruction": f"{obj_text} {mod_data['text']}",
                        "eval_metadata": mod_data["eval_metadata"],
                        "objective": obj_name,
                    }
                instructions.append(instruction)

print(json.dumps(instructions[:2], indent=4))
```

```python title="Output"
[
    {
        "instruction": "Summarize the meeting based on the transcript. In paragraph form, output your response. Use at least 10 words and at most 50 words in total.",
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 10,
            "max_length": 50
        },
        "objective": "general_summarization"
    },
    {
        "instruction": "Summarize the meeting based on the transcript. Return the answer in the form of paragraphs. Make sure your answer is between 50 and 200 words long.",
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 50,
            "max_length": 200
        },
        "objective": "general_summarization"
    }
]
```

Finally, let's build the final prompts by semi-randomly pairing the instructions with transcripts from the QMSum dataset.

```python PYTHON
data = pd.DataFrame(instructions)

transcripts = sorted(transcripts, key=lambda x: len(x), reverse=True)[:int(len(transcripts) * 0.25)]
random.seed(42)
random.shuffle(transcripts)
data["transcript"] = transcripts[:len(data)]

data["prompt"] = data.apply(lambda x: prompt_template.format(transcript=x["transcript"], instructions=x["instruction"]), axis=1)
```

```python PYTHON
data["transcript_token_len"] = [len(x) for x in co.batch_tokenize(data["transcript"].tolist(), model=co_model)]
```

```python PYTHON
print(data["prompt"][0])
```

```txt title="Output"
## meeting transcript
PhD F: As opposed to the rest of us
PhD D: Well comment OK I I remind that me my first objective eh in the project is to to study difference parameters to to find a a good solution to detect eh the overlapping zone in eh speech recorded But eh tsk comment ehhh comment In that way comment I I I begin to to study and to analyze the ehn the recorded speech eh the different session to to find and to locate and to mark eh the the different overlapping zone And eh so eh I was eh I am transcribing the the first session and I I have found eh eh one thousand acoustic events eh besides the overlapping zones eh I I I mean the eh breaths eh aspiration eh eh talk eh eh clap eh comment I do not know what is the different names eh you use to to name the the pause n speech
Grad G: Oh I do not think we ve been doing it at that level of detail So
PhD D: Eh I I I do I do not need to to to mmm to m to label the the different acoustic but I prefer because eh I would like to to study if eh I I will find eh eh a good eh parameters eh to detect overlapping I would like to to to test these parameters eh with the another eh eh acoustic events to nnn to eh to find what is the ehm the false eh the false eh hypothesis eh nnn which eh are produced when we use the the ehm this eh parameter eh I mean pitch eh eh difference eh feature
PhD A: You know I think some of these that are the nonspeech overlapping events may be difficult even for humans to tell that there s two there I mean if it s a tapping sound you would not necessarily or you know something like that it would be it might be hard to know that it was two separate events
Grad G: Well You were not talking about just overlaps were you ? You were just talking about acoustic events
PhD D: I I I I t I t I talk eh about eh acoustic events in general but eh my my objective eh will be eh to study eh overlapping zone Eh ? comment n Eh in twelve minutes I found eh eh one thousand acoustic events
Professor E: How many overlaps were there in it ? No no how many of them were the overlaps of speech though ?
PhD D: How many ? Eh almost eh three hundred eh in one session in five eh in forty five minutes Alm Three hundred overlapping zone With the overlapping zone overlapping speech speech what eh different duration
Postdoc B: Does this ? So if you had an overlap involving three people how many times was that counted ?
PhD D: three people two people Eh I would like to consider eh one people with difference noise eh in the background be
Professor E: No no but I think what she s asking is pause if at some particular for some particular stretch you had three people talking instead of two did you call that one event ?
PhD D: Oh Oh I consider one event eh for th for that eh for all the zone This th I I I con I consider I consider eh an acoustic event the overlapping zone the period where three speaker or eh are talking together
Grad G: So let s say me and Jane are talking at the same time and then Liz starts talking also over all of us How many events would that be ?
PhD D: So I do not understand
Grad G: So two people are talking comment and then a third person starts talking Is there an event right here ?
PhD D: Eh no No no For me is the overlapping zone because because you you have s you have more one eh more one voice eh eh produced in a in in a moment
Grad G: So i if two or more people are talking
Professor E: OK So I think We just wanted to understand how you are defining it So then in the region between since there there is some continuous region in between regions where there is only one person speaking And one contiguous region like that you are calling an event Is it Are you calling the beginning or the end of it the event or are you calling the entire length of it the event ?
PhD D: I consider the the nnn the nnn nnn eh the entirety eh eh all all the time there were the voice has overlapped This is the idea But eh I I do not distinguish between the the numbers of eh speaker I m not considering eh the the ehm eh the fact of eh eh for example what did you say ? Eh at first eh eh two talkers are eh speaking and eh eh a third person eh join to to that For me it s eh it s eh all overlap zone with eh several numbers of speakers is eh eh the same acoustic event Wi but without any mark between the zone of the overlapping zone with two speakers eh speaking together and the zone with the three speakers
Postdoc B: That would j just be one
PhD D: Eh with eh a beginning mark and the ending mark Because eh for me is the is the zone with eh some kind of eh distortion the spectral I do not mind By the moment by the moment
Grad G: Well but But you could imagine that three people talking has a different spectral characteristic than two
PhD D: I I do not but eh but eh I have to study comment What will happen in a general way
Grad G: So You had to start somewhere
PhD C: So there s a lot of overlap
PhD D: I I do not know what eh will will happen with the
Grad G: That s a lot of overlap
Professor E: So again that s that s three three hundred in forty five minutes that are that are speakers just speakers
Postdoc B: But a a a th
Professor E: So that s about eight per minute
Postdoc B: But a thousand events in twelve minutes that s
PhD C: But that can include taps
Postdoc B: Well but a thousand taps in eight minutes is a l in twelve minutes is a lot
PhD D: I I con I consider I consider acoustic events eh the silent too
Grad G: Silence starting or silence ending
PhD D: silent ground to bec to detect eh because I consider acoustic event all the things are not eh speech In ge in in in a general point of view
Professor E: OK so how many of those thousand were silence ?
PhD F: Not speech not speech or too much speech
Professor E: Right So how many of those thousand were silence silent sections ?
PhD D: silent I I I I do not I I have not the eh I I would like to to do a stylistic study

## instructions
Summarize the meeting based on the transcript. In paragraph form, output your response. Use at least 10 words and at most 50 words in total.
```

# Build the evaluation framework \[#eval-framework]

We now setup the tools we will use for evaluation.

We use three criteria that are graded using LLMs:

* Completeness: checks if the summary includes all the important information from the original text that it should include
* Correctness: checks if there are any hallucinations or factual inaccuracies in the summary
* Conciseness: checks if the summary includes any unnecessary information or wordiness

In this cookbook, we will use Command-R to grade the completions. However, note that in practice, we typically use an ensemble of multiple LLM evaluators to reduce any bias.

```python PYTHON

grading_prompt_template = """You are an AI grader that given a prompt, a completion, and a criterion, grades the completion based on the prompt and criterion. Below is a prompt, a completion, and a criterion with which to grade the completion. You need to respond according to the criterion instructions.

PROMPT:
{prompt}

COMPLETION:
{completion}

CRITERION:
{criteria}

Do not provide an explanation or respond with additional text. Only respond with the final score in the format SCORE: <final_score>

SCORE:"""


criteria_completeness = """Please judge the above completion on whether or not all the completion fully addresses the task posed in the prompt. The completion should contain all the information that is asked for by the prompt while also upholding the constraints mentioned in the prompt. Please return a grade between 1 and 5, where 1 means the completion does not address the prompt at all, 2 means the completion mostly does not address the prompt, 3 is neutral, 4 means the completion mostly addresses the prompt, and 5 means the completion fully addresses the prompt."""

criteria_correctness = """Please judge the above completion on whether or not all information was derived from the prompt and that no information is false. Return a grade between 1 and 5, where 1 means the answers are entirely untruthful relative to the prompt, 2 means the answers are somewhat untruthful relative to the prompt, 3 means neutral, 4 means the answers are somewhat truthful relative to the prompt, and 5 means the answers are entirely truthful relative to the prompt. Evaluate only the truthfulness of the answers, not whether or not they capture all the relevant information in the prompt."""

criteria_conciseness = """Please judge the above completion on whether or not the completion contains any unnecessary information or wordiness that does not help answer the specific instruction given in the prompt. Return a grade between 1 and 5, where 1 means the completion contains many unnecessary details and wordiness that do not answer the specific instruction given in the prompt, 2 means the completion contains some unnecessary details or wordiness, 3 means neutral, 4 means the completion contains few unnecessary details or wordiness, and 5 means the completion contains only necessary details that answer the specific instruction given in the prompt."""


def score_llm(prompt: str, completion: str, criteria: str) -> int:
    """
    Score a completion based on a prompt and a criterion using LLM Because we
    grade all completions on a scale of 1-5, we will normalize the scores by 5 so that the final score
    is between 0 and 1.
    """
    grading_prompt = grading_prompt_template.format(
        prompt=prompt, completion=completion, criteria=criteria
    )
    # Use Cohere to grade the completion
    completion = co.chat(message=grading_prompt, model=co_model, temperature=0.2).text

    ### Alternatively, use OpenAI to grade the completion (requires key)
    # import openai
    # completion = openai.OpenAI(api_key="INSERT OPENAI KEY HERE").chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": grading_prompt}],
    #     temperature=0.2,
    # ).choices[0].message.content

    # Extract the score from the completion
    score = float(re.search(r"[12345]", completion).group()) / 5
    return score
```

In addition, we have two criteria that are graded programmatically:

* Format: checks if the summary follows the format (e.g. bullets) that was requested in the prompt
* Length: checks if the summary follows the length that was requested in the prompt.

```python PYTHON

def score_format(completion: str, format_type: str) -> int:
    """
    Returns 1 if the completion is in the correct format, 0 otherwise.
    """
    if format_type == "paragraphs":
        return int(_is_only_paragraphs(completion))
    elif format_type == "bullets":
        return int(_is_only_bullets(completion))
    return 0

def score_length(
    completion: str,
    format_type: str,
    min_val: int,
    max_val: int,
    number: Optional[int] = None
) -> int:
    """
    Returns 1 if the completion has the correct length for the given format, 0 otherwise. This
    includes both word count and number of items (optional).
    """
    # Split into items (each bullet for bullets or each paragraph for paragraphs)
    if format_type == "bullets":
        items = _extract_markdown_bullets(completion, include_bullet=False)
    elif format_type == "paragraphs":
        items = completion.split("\n")

    # Strip whitespace and remove empty items
    items = [item for item in items if item.strip() != ""]

    # Check number of items if provided
    if number is not None and len(items) != number:
        return 0

    # Check length of each item
    for item in items:
        num_words = item.strip().split()
        if min_val is None and len(num_words) > max_val:
            return 0
        elif max_val is None and len(num_words) < min_val:
            return 0
        elif not min_val <= len(num_words) <= max_val:
            return 0
    return 1


def _is_only_bullets(text: str) -> bool:
    """
    Returns True if text is only markdown bullets.
    """
    bullets = _extract_markdown_bullets(text, include_bullet=True)

    for bullet in bullets:
        text = text.replace(bullet, "")

    return text.strip() == ""


def _is_only_paragraphs(text: str) -> bool:
    """
    Returns True if text is only paragraphs (no bullets).
    """
    bullets = _extract_markdown_bullets(text, include_bullet=True)

    return len(bullets) == 0


def _extract_markdown_bullets(text: str, include_bullet: bool = False) -> List[str]:
    """
    Extracts markdown bullets from text as a list. If include_bullet is True, the bullet will be
    included in the output. The list of accepted bullets is: -, *, +, •, and any number followed by
    a period.
    """
    if include_bullet:
        return re.findall(r"^[ \t]*(?:[-*+•]|[\d]+\.).*\w+.*$", text, flags=re.MULTILINE)
    return re.findall(r"^[ \t]*(?:[-*+•]|[\d]+\.)(.*\w+.*)$", text, flags=re.MULTILINE)

```

# Run evaluations \[#run-evals]

Now that we have our evaluation dataset and defined our evaluation functions, let's run evaluations!

First, we generate completions to be graded. We will use Cohere's [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01) model, boasting a context length of 128K.

```python PYTHON
completions = []
for prompt in data["prompt"]:
    completion = co.chat(message=prompt, model="command-r", temperature=0.2).text
    completions.append(completion)

data["completion"] = completions
```

```python PYTHON
print(data["completion"][0])
```

PhD D is transcribing recorded sessions to locate overlapping speech zones and categorizing them as acoustic events. The team discusses the parameters PhD D should use and how to define these events, considering the number of speakers and silence.

Let's grade the completions using our LLM and non-LLM checks.

```python PYTHON
data["format_score"] = data.apply(
    lambda x: score_format(x["completion"], x["eval_metadata"]["format"]), axis=1
)

data["length_score"] = data.apply(
    lambda x: score_length(
        x["completion"],
        x["eval_metadata"]["format"],
        x["eval_metadata"].get("min_length"),
        x["eval_metadata"].get("max_length"),
    ),
    axis=1,
)

data["completeness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_completeness), axis=1
)

data["correctness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_correctness), axis=1
)

data["conciseness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_conciseness), axis=1
)
```

```python PYTHON
data
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          instruction
        </th>

        <th>
          eval_metadata
        </th>

        <th>
          objective
        </th>

        <th>
          transcript
        </th>

        <th>
          prompt
        </th>

        <th>
          transcript_token_len
        </th>

        <th>
          completion
        </th>

        <th>
          format_score
        </th>

        <th>
          length_score
        </th>

        <th>
          completeness_score
        </th>

        <th>
          correctness_score
        </th>

        <th>
          conciseness_score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'paragraphs', 'min_length': 10, 'ma...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          PhD F: As opposed to the rest of us \nPhD D: W...
        </td>

        <td>
          \## meeting transcript\nPhD F: As opposed to th...
        </td>

        <td>
          1378
        </td>

        <td>
          PhD D is transcribing recorded sessions to loc...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'paragraphs', 'min_length': 50, 'ma...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Lynne Neagle AM: Thank you very much And the n...
        </td>

        <td>
          \## meeting transcript\nLynne Neagle AM: Thank ...
        </td>

        <td>
          1649
        </td>

        <td>
          The discussion focused on the impact of COVID1...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'bullets', 'number': 3, 'min_length...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Industrial Designer: Yep So we are to mainly d...
        </td>

        <td>
          \## meeting transcript\nIndustrial Designer: Ye...
        </td>

        <td>
          1100
        </td>

        <td>
          \- The team is designing a remote control with ...
        </td>

        <td>
          1
        </td>

        <td>
          0
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'bullets', 'number': 2, 'min_length...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Industrial Designer: Mm I think one of the ver...
        </td>

        <td>
          \## meeting transcript\nIndustrial Designer: Mm...
        </td>

        <td>
          2618
        </td>

        <td>
          \- The team discusses the target demographic fo...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          What are the follow-up items based on the meet...
        </td>

        <td>
          \{'format': 'bullets', 'number': 3, 'min_length...
        </td>

        <td>
          action_items
        </td>

        <td>
          Marketing: so a lot of people have to be able ...
        </td>

        <td>
          \## meeting transcript\nMarketing: so a lot of ...
        </td>

        <td>
          2286
        </td>

        <td>
          \- Investigate how the remote will interact wit...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          5
        </th>

        <td>
          What are the follow-up items based on the meet...
        </td>

        <td>
          \{'format': 'bullets', 'number': 2, 'min_length...
        </td>

        <td>
          action_items
        </td>

        <td>
          Project Manager: Alright So finance And we wil...
        </td>

        <td>
          \## meeting transcript\nProject Manager: Alrigh...
        </td>

        <td>
          1965
        </td>

        <td>
          \- The project manager will send the updated de...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>
    </tbody>
  </table>
</div>

Finally, let's print the average scores per critiera.

```python PYTHON
avg_scores = data[["format_score", "length_score", "completeness_score", "correctness_score", "conciseness_score"]].mean()
print(avg_scores)
```

```txt title="Output"
format_score          1.000000
length_score          0.833333
completeness_score    0.800000
correctness_score     1.000000
conciseness_score     0.800000
dtype: float64
```


# Text Classification Using Embeddings

> This page discusses the creation of a text classification model using word vector embeddings.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Text_Classification_Using_Embeddings.ipynb" />

This notebook shows how to build a classifier using Cohere's embeddings.

<img alt="first we embed the text in the dataset, then we use that to train a classifier" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/simple-classifier-embeddings.png" />

The example classification task here will be sentiment analysis of film reviews. We'll train a simple classifier to detect whether a film review is negative (class 0) or positive (class 1).

We'll go through the following steps:

1. Get the dataset
2. Get the embeddings of the reviews (for both the training set and the test set).
3. Train a classifier using the training set
4. Evaluate the performance of the classifier on the testing set

If you're running an older version of the SDK you'll want to upgrade it, like this:

```python PYTHON
#!pip install --upgrade cohere
```

## 1. Get the dataset

```python PYTHON
import cohere
from sklearn.model_selection import train_test_split

import pandas as pd
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv', delimiter='\t', header=None)
```

```python PYTHON
df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          0
        </th>

        <th>
          1
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          a stirring , funny and finally transporting re imagining of beauty and
          the beast and 1930s horror films
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          apparently reassembled from the cutting room floor of any given
          daytime soap
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          they presume their audience wo n't sit still for a sociology lesson ,
          however entertainingly presented , so they trot out the conventional
          science fiction elements of bug eyed monsters and futuristic women in
          skimpy clothes
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          this is a visually stunning rumination on love , memory , history and
          the war between art and commerce
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          jonathan parker 's bartleby should have been the be all end all of the
          modern office anomie films
        </td>

        <td>
          1
        </td>
      </tr>
    </tbody>
  </table>
</div>

We'll only use a subset of the training and testing datasets in this example. We'll only use 500 examples since this is a toy example. You'll want to increase the number to get better performance and evaluation.

The `train_test_split` method splits arrays or matrices into random train and test subsets.

```python PYTHON
num_examples = 500
df_sample = df.sample(num_examples)

sentences_train, sentences_test, labels_train, labels_test = train_test_split(
            list(df_sample[0]), list(df_sample[1]), test_size=0.25, random_state=0)


sentences_train = sentences_train[:95]
sentences_test = sentences_test[:95]

labels_train = labels_train[:95]
labels_test = labels_test[:95]
```

## 2. Set up the Cohere client and get the embeddings of the reviews

We're now ready to retrieve the embeddings from the API. You'll need your API key for this next cell. [Sign up to Cohere](https://dashboard.cohere.com/) and get one if you haven't yet.

```python PYTHON
model_name = "embed-v4.0"
api_key = ""

input_type = "classification"

co = cohere.Client(api_key)
```

```python PYTHON
embeddings_train = co.embed(texts=sentences_train,
                            model=model_name,
                            input_type=input_type
                            ).embeddings

embeddings_test = co.embed(texts=sentences_test,
                           model=model_name,
                           input_type=input_type
                            ).embeddings

```

Note that the ordering of the arguments is important. If you put `input_type` in before `model_name`, you'll get an error.

We now have two sets of embeddings, `embeddings_train` contains the embeddings of the training sentences while `embeddings_test` contains the embeddings of the testing sentences.

Curious what an embedding looks like? We can print it:

```python PYTHON
print(f"Review text: {sentences_train[0]}")
print(f"Embedding vector: {embeddings_train[0][:10]}")
```

```
Review text: the script was reportedly rewritten a dozen times either 11 times too many or else too few
Embedding vector: [1.1531117, -0.8543223, -1.2496399, -0.28317127, -0.75870246, 0.5373464, 0.63233083, 0.5766576, 1.8336298, 0.44203663]
```

## 3. Train a classifier using the training set

Now that we have the embedding, we can train our classifier. We'll use an SVM from sklearn.

```python PYTHON
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced'))

svm_classifier.fit(embeddings_train, labels_train)

```

```
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('svc', SVC(class_weight='balanced'))])
```

## 4. Evaluate the performance of the classifier on the testing set

```python PYTHON
score = svm_classifier.score(embeddings_test, labels_test)
print(f"Validation accuracy on is {100*score}%!")
```

```
Validation accuracy on Large is 91.2%!
```

You may get a slightly different number when you run this code.

This was a small scale example, meant as a proof of concept and designed to illustrate how you can build a custom classifier quickly using a small amount of labelled data and Cohere's embeddings. Increase the number of training examples to achieve better performance on this task.


# Topic Modeling System for AI Papers

> This page discusses how to create a topic-modeling system for papers focused on AI papers.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Topic_Modeling_AI_Papers.ipynb" />

Natural Language Processing (NLP) is a key area of machine learning focused on analyzing and understanding text data. One popular NLP application is topic modeling, which uses unsupervised learning and clustering algorithms to group similar texts and extract underlying topics from document collections. This approach enables automatic document organization, efficient information retrieval, and content filtering.

Here, you'll learn how to use Cohere’s NLP tools to perform semantic search and clustering of AI Papers, which could help you discover trends in AI. You'll:

* Scrape the most recent page of the ArXiv page for AI, with the output being a list of recently published AI papers.
* Use Cohere’s Embed Endpoint to generate word embeddings using your list of AI papers.
* Visualize the embeddings and proceed to perform topic modeling.
* Use a tool to find the papers most relevant to a query you provide.

To follow along with this tutorial, you need to be familiar with Python and have python version 3.6+ installed, and you'll need to have a Cohere account. Everything that follows can be tested with a Google Colab notebook.

First, you need to install the python dependencies required to run the project. Use pip to install them using the command below.

```python PYTHON
pip install requests beautifulsoup4 cohere altair clean-text numpy pandas scikit-learn > /dev/null
```

And we'll also initialize the Cohere client.

```python PYTHON
import cohere

api_key = '<api_key>'
co = cohere.ClientV2(api_key="YOUR API KEY")
```

With that done, we'll import the required libraries to make web requests, process the web content, and perform our topic-modeling functions.

```python PYTHON
## Getting the web content
import requests
from bs4 import BeautifulSoup

## Processing the content 
import pandas as pd
import numpy as np

## Handling the underlying NLP
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
```

Next, make an HTTP request to the source website that has an archive of the AI papers.

```python PYTHON
URL = "https://arxiv.org/list/cs.AI/new"
page = requests.get(URL)
```

## Setting up the Functions We Need

In this section, we'll walk through some of the Python code we'll need for our topic modeling project.

### Getting and Processing ArXiv Papers.

This `make_raw_df` function scrapes paper data from a given URL, pulling out titles and abstracts. It uses `BeautifulSoup` to parse the HTML content, extracting titles from elements with class `"list-title mathjax"` and abstracts from paragraph elements with class `"mathjax"`. Finally, it organizes this data into a pandas dataframe with two columns - "titles" and "texts" - where each row represents the information from a single paper.

```python PYTHON
def make_raw_df(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, "html.parser")

    titles=list()
    texts=list()

    # Extract titles from <div class="list-title mathjax">
    title_tags = soup.find_all(class_="list-title mathjax")
    for title_tag in title_tags:
        titles.append(title_tag.text.strip())  # Remove leading/trailing whitespace

    # Extract abstracts from <p class="mathjax">
    abstract_tags = soup.find_all('p', class_="mathjax")#, tag="p")
    for abstract_tag in abstract_tags:
        texts.append(abstract_tag.text.strip())

    df = pd.DataFrame({"titles": titles, "texts": texts})
    return df
```

### Generating embeddings

[Word embedding](https://docs.cohere.com/docs/embeddings) is a technique for learning a numerical representation of words. You can use these embeddings to:

• Cluster large amounts of text\
• Match a query with other similar sentences\
• Perform classification tasks like sentiment classification

All of which we will do today.

Cohere’s platform provides an [Embed endpoint](https://docs.cohere.com/reference/embed) that returns text embeddings. An embedding is a list of floating-point numbers, and it captures the semantic meaning of the represented text. Models used to create these embeddings are available in several; small models are faster while large models offer better performance.

In the `get_embeddings`, `make_clusters`, and `create_cluster_names` functions defined below, we'll generate embeddings from the papers, use principal component analysis to create axes for later plotting efforts, use KMeans clustering to group the embedded papers into broad topics, and create a 'short name' that captures the essence of each cluster. This short name will make our Altair plot easier to read.

```python PYTHON
def get_embeddings(text,model='embed-v4.0'):
  output = co.embed(
                model=model,
                texts=[text],
                input_type="classification",
                embedding_types=["float"],)
  return output.embeddings.float_[0]

# Reduce embeddings to 2 principal components to aid visualization
# Function to return the principal components
def get_pc(arr,n):
  pca = PCA(n_components=n)
  embeds_transform = pca.fit_transform(arr)
  return embeds_transform

def make_clusters(df,n_clusters):

    # Get the embeddings for the text column
    df_clust = df.copy()
    df_clust['text_embeds'] = df_clust['texts'].apply(get_embeddings) # We've defined this function above.

    # Convert the embeddings list to a numpy array
    embeddings_array = np.array(df_clust['text_embeds'].tolist())
    # Cluster the embeddings

    kmeans_model = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
    classes = kmeans_model.fit_predict(embeddings_array).tolist()
    df_clust['cluster'] = (list(map(str,classes)))

    df_clust.columns.astype(str)
    return df_clust

def create_cluster_names(essences_dict):
    cluster_names = {}
    for cluster_num, description in essences_dict.items():
        # Take the first sentence and limit to first N characters
        short_name = description.split('.')[0][:30].strip() + '...'
        cluster_names[cluster_num] = short_name
    return cluster_names
```

### Get Topic Essences

Then, the `get_essence` function calls out to a Cohere [Command endpoint](https://docs.cohere.com/reference/chat) to create an 'essentialized' description of the papers in a given cluster. Like the 'short names' from above this will improve the readibility of our plot, because otherwise it would be of limited use.

```python PYTHON
def get_essence(df):

    clusters = sorted(df['cluster'].unique())
    cluster_descriptions = {}

    for cluster_num in clusters:
        
        cluster_df = df[df['cluster'] == cluster_num]
        # Combine titles and texts
        titles = ' '.join(cluster_df['titles'].fillna(''))
        texts = ' '.join(cluster_df['texts'].fillna(''))
        combined_text = f"Titles: {titles}\n\nTexts: {texts}"

        system_message = """
        ## Task & Context
        You are a world-class language model that's especially good at capturing the essence of complex text.

        ## Style Guide
        Unless the user asks for a different style of answer, you should answer in concise text with proper grammar and spelling.
        """

        message=f"""Based on the following titles and texts from academic papers, provide 3-4 words that describe what this category of papers is about. Think of this like a word cloud.
        Focus on the main theme or topic that unifies these papers.
        Please do not use the words 'AI', 'Artificial Intelligence,' 'Machine Learning,' or 'ML' in your response.
        
        {combined_text}
        
        Description:"""

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": message},
        ]

        essence = co.chat(
            model="command-a-03-2025,
            messages=messages
        )

        description = essence.message.content[0].text.strip() + "."
        cluster_descriptions[cluster_num] = description     

    return cluster_descriptions
```

### Generating a Topic Plot

Finally, this `generate_chart` ties together the processing we've defined so far to create a beautiful Altair chart displaying the papers in our topics.

```python PYTHON
import altair as alt
# Function to generate the 2D plot
def generate_chart(df,xcol,ycol,lbl='off',color='basic',title='', cluster_names=None):

  ## IMPORTANT
  ## We're using this function to create the 'x' and 'y' columns for the chart.
  ## We don't actually use the principal components anywhere else in the code.
  embeds = np.array(df['text_embeds'].tolist())
  embeds_pc2 = get_pc(embeds,2)
  # Add the principal components to dataframe
  df = pd.concat([df, pd.DataFrame(embeds_pc2)], axis=1)
  ## END IMPORTANT

  # Add cluster names to the dataframe if provided
  if cluster_names:
      df['cluster_label'] = df['cluster'].map(cluster_names)
  else:
      df['cluster_label'] = df['cluster']
  
  # Plot the 2D embeddings on a chart
  df.columns = df.columns.astype(str)

  if color == 'basic':
      color_encode = alt.value('#333293')
  else:
      color_encode = alt.Color('cluster_label:N',
          scale=alt.Scale(scheme='category20'),
          legend=alt.Legend(
              title="Topics",
              symbolLimit=len(cluster_names) if cluster_names else None,
              orient='right',
              labelLimit=500,  # Increase label width limit (default is 200)
              columns=1  # Force single column layout
          ))


  chart = alt.Chart(df).mark_circle(size=500).encode(
        x=alt.X(xcol,
            scale=alt.Scale(zero=False),
            axis=alt.Axis(labels=False, ticks=False, domain=False)
        ),
        y=alt.Y(ycol,
            scale=alt.Scale(zero=False),
            axis=alt.Axis(labels=False, ticks=False, domain=False)
        ),
        color=color_encode,
        tooltip=['titles', 'cluster_label']  # Updated to show cluster label in tooltip
    )

  if lbl == 'on':
    text = chart.mark_text(align='left', baseline='middle',dx=15, size=13,color='black').encode(text='title', color= alt.value('black'))
  else:
    text = chart.mark_text(align='left', baseline='middle',dx=10).encode()

  result = (chart + text).configure(background="#FDF7F0"
      ).properties(
          width=800,
          height=500,
          title=title
      ).configure_legend(
          orient='right',
          titleFontSize=18,
          labelFontSize=10,
          padding=5,  # Add some padding around the legend
          offset=5,   # Move legend away from chart
          labelLimit=500  # Also need to set it here
      )
      
  return result
```

### Calling the Functions

Since we've defined our logic in the functions above, we now need only to call them in order.

```python PYTHON
### Creating the baseline dataframe.
df = make_raw_df("https://arxiv.org/list/cs.AI/new")

### Defining our cluster number and making a 'cluster' dataframe.
n_clusters = 12
df_clust = make_clusters(df,n_clusters)

### Get the topic essences and cluster names
overview = get_essence(df_clust)
cluster_names = create_cluster_names(overview)

### Generate the chart
generate_chart(df_clust,'0','1',lbl='off',color='cluster',title=f'Clustering with {n_clusters} Clusters', cluster_names=cluster_names)
```

Your chart will look different, but it should be similar to this one:
![Topic modeling chart](file:9bca598c-dd83-41bd-8e81-7a6287274f0c)

Congratulations! You have created the word embeddings and visualized them using a scatter plot, showing the overall structure of these papers.

## Similarity Search Across Papers

Next, we'll expand on the functionality we've built so far to make it possible to find papers related to a user-provided query.

As before, we'll begin by defining our `get_similarity` function. It takes a `target` query and compares it to `candidates` to return the most relevant papers.

```python PYTHON
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(target,candidates):
  # Turn list into array
  candidates = np.array(candidates)
  target = np.expand_dims(np.array(target),axis=0)

  # Calculate cosine similarity
  sim = cosine_similarity(target,candidates)
  sim = np.squeeze(sim).tolist()
  sort_index = np.argsort(sim)[::-1]
  sort_score = [sim[i] for i in sort_index]
  similarity_scores = zip(sort_index,sort_score)

  # Return similarity scores
  return similarity_scores
```

All we need now is to feed it a query and print out the top papers:

```python PYTHON 
# Add new query
new_query = "Anything on AI personalities?"

# Get embeddings of the new query
new_query_embeds = get_embeddings(new_query)

embeds = np.array(df_clust['text_embeds'].tolist()) # We defined these embeddings earlier and are pulling them out now for the function.

# Get the similarity between the search query and existing queries
similarity = get_similarity(new_query_embeds, embeds)
#print(list(similarity))
# View the top 5 articles
print('Query:')
print(new_query,'\n')

print('Similar queries:')
for idx,sim in similarity:
  print(f'Similarity: {sim:.2f};')
  print(df.iloc[idx]['titles'])
  print(df.iloc[idx]['texts'])
  print()
```

You should see something like this:

![Similar papers](file:14553fdf-9924-48d2-9d21-65cb774bebb5)

## Conclusion

Let's recap the NLP tasks implemented in this tutorial. You’ve created word embeddings, clustered those, and visualized them, then performed a semantic search to find similar papers. Cohere’s platform provides NLP tools that are easy and intuitive to integrate. You can create digital experiences that support powerful NLP capabilities like text clustering. It’s easy to [register a Cohere account](https://dashboard.cohere.com/) and get to an API key.


# Wikipedia Semantic Search with Cohere + Weaviate

> This page contains a description of building a Wikipedia-focused search engine with Cohere's LLM platform and the Weaviate vector database.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Wikipedia_search_demo_cohere_weaviate.ipynb" />

This is starter code that you can use to search 10 million vectors from Wikipedia embedded with Cohere's multilingual model and hosted as a Weaviate public dataset. This dataset contains 1M vectors in each of the Wikipedia sites in these languages: English, German, French, Spanish, Italian, Japanese, Arabic, Chinese (Simplified), Korean, Hindi \[respective language codes: `en, de, fr, es, it, ja, ar, zh, ko, hi`]

```python PYTHON
import weaviate

cohere_api_key = ''

auth_config = weaviate.auth.AuthApiKey(api_key="76320a90-53d8-42bc-b41d-678647c6672e")
client = weaviate.Client(
    url="https://cohere-demo.weaviate.network/",
    auth_client_secret=auth_config,
    additional_headers={
        "X-Cohere-Api-Key": cohere_api_key,
    }
)

client.is_ready() #check if True
```

```txt title="Output"
True
```

Let's now define the search function that queries our vector database. Optionally, we want the ability to filter by language.

```python PYTHON

def semantic_serch(query, results_lang=''):
    """
    Query the vectors database and return the top results.


    Parameters
    ----------
        query: str
            The search query

        results_lang: str (optional)
            Retrieve results only in the specified language.
            The demo dataset has those languages:
            en, de, fr, es, it, ja, ar, zh, ko, hi

    """

    nearText = {"concepts": [query]}
    properties = ["text", "title", "url", "views", "lang", "_additional {distance}"]

    # To filter by language
    if results_lang != '':
        where_filter = {
        "path": ["lang"],
        "operator": "Equal",
        "valueString": results_lang
        }
        response = (
            client.query
            .get("Articles", properties)
            .with_where(where_filter)
            .with_near_text(nearText)
            .with_limit(5)
            .do()
        )

    # Search all languages
    else:
        response = (
            client.query
            .get("Articles", properties)
            .with_near_text(nearText)
            .with_limit(5)
            .do()
        )


    result = response['data']['Get']['Articles']

    return result


def print_result(result):
    """ Print results with colorful formatting """
    for item in result:
        print(f"\033[95m{item['title']} ({item['views']}) {item['_additional']['distance']}\033[0m")
        print(f"\033[4m{item['url']}\033[0m")
        print(item['text'])
        print()
```

We can now query the database with any query we want. In the background, Weaviate uses your Cohere API key to embed the query, then retrun the most relevant passages to the query.

```python PYTHON
query_result = semantic_serch("time travel plot twist")

print_result(query_result)
```

```txt title="Output"
[95mThe Adam Project (3000) -147.31755[0m
[4mhttps://en.wikipedia.org/wiki?curid=65867428[0m
Due to a safety feature preventing him from flying because of his injuries, Adam must bring along the younger Adam and use his DNA to enter his jet. They both are soon attacked by Maya Sorian, the leader of the dystopian world, and her assistant Christos, but are saved by Laura, who had faked her death and stayed off-grid in an unknown location. After surviving the attack and comparing notes, Laura and the Adams realize that after the invention of time travel by Louis Reed and his subsequent death, Sorian had monopolized the discovery. During her visit to 2018, Laura learned Sorian frequently came and advised her past self in order to secure her future wealth and power. To protect her secret, Sorian ordered Laura's death. Although Laura survived the assassination attempt, destruction of her time jet left her stranded in the past. The sudden arrival of Sorian's goons interrupts the reunion, and Laura fights off the attack long enough for the two Adams to escape to 2018.

[95mKang the Conqueror (2000) -146.57275[0m
[4mhttps://en.wikipedia.org/wiki?curid=393437[0m
Nathaniel Richards, a 31st-century scholar and descendant of Reed Richards' time traveling father Nathaniel, becomes fascinated with history and discovers the time travel technology created by Victor von Doom, another possible ancestor of his. He then travels back in time to ancient Egypt aboard a Sphinx-shaped timeship and becomes the Pharaoh Rama-Tut, with plans to claim En Sabah Nur—the mutant destined to become Apocalypse—as his heir. Rama-Tut's rule is cut short when he is defeated by the time-displaced Fantastic Four. An embittered Nathaniel Richards travels forward to the 20th century where he meets Doctor Doom, whom he believes might be his ancestor. He later designs an armor based on Doom's and, calling himself the Scarlet Centurion, pits the Avengers team against alternate-reality counterparts. He plans to dispose of all of them, but the Avengers manage to force him from the timeline.

[95mBack to the Future (3000) -146.4269[0m
[4mhttps://en.wikipedia.org/wiki?curid=42993[0m
That night, Marty meets his eccentric scientist friend, Emmett "Doc" Brown, in the Twin Pines mall parking lot. Doc unveils a time machine built from a modified DeLorean, powered by plutonium he swindled from Libyan terrorists. After Doc inputs a destination time of November5, 1955—the day he first conceived his time travel invention—the terrorists arrive unexpectedly and gun Doc down. Marty flees in the DeLorean, inadvertently activating time travel when he reaches .

[95mTime (2000) -146.41129[0m
[4mhttps://en.wikipedia.org/wiki?curid=30012[0m
Time travel is the concept of moving backwards or forwards to different points in time, in a manner analogous to moving through space, and different from the normal "flow" of time to an earthbound observer. In this view, all points in time (including future times) "persist" in some way. Time travel has been a plot device in fiction since the 19th century. Travelling backwards or forwards in time has never been verified as a process, and doing so presents many theoretical problems and contradictive logic which to date have not been overcome. Any technological device, whether fictional or hypothetical, that is used to achieve time travel is known as a time machine.

[95mIn Time (2000) -145.93015[0m
[4mhttps://en.wikipedia.org/wiki?curid=29446866[0m
Will and Sylvia rob Weis' time banks, giving the time capsules to the needy. They soon realize they can't significantly change anything, as prices are raised faster to compensate for the extra time. Fortis' gang ambushes them intending to collect the reward for their capture, but Will kills Fortis and his gang. Will and Sylvia then decide to rob Weis' vault of a one-million year capsule. Leon chases them back to Dayton but fails to stop them from distributing the stolen time; Leon times out, having neglected to collect his day's salary. Will and Sylvia nearly time out themselves but survive by taking Leon's salary.
```

## Filtering by language

If we're interested in results in only one language, we can specify it.

```python PYTHON
query_result = semantic_serch("time travel plot twist", results_lang='ja')

print_result(query_result)
```

```txt title="Output"
[95m時空の旅人 (500) -144.16002[0m
[4mhttps://ja.wikipedia.org/wiki?curid=523464[0m
バスは1868年の攘夷戦争で娘と夫を亡くした老婆の営む茶店に降り立つ。一時は老婆は一行を盗人と間違えて襲い掛かるも、ホクベンを亡き夫だと思い込んだことで一転して歓迎する。しかしそこへジロを追うタイムマシンがあらわれ、やむなく一行はバスに乗って走り去る。追い縋る老婆を見捨てられずバスを飛び降りたホクベンだが、直後にタイムマシンに攫われてしまった。

[95m親殺しのパラドックス (700) -144.11864[0m
[4mhttps://ja.wikipedia.org/wiki?curid=71910[0m
パラドックスを防ぐアイデアとして、時間旅行者は元々の歴史とは異なる並行宇宙に行くのだと解釈するもので、上の科学的理論で述べたのと同じ考え方であり、SFにもよく見られる。歴史改変SFにあるタイムトラベル参照。

[95mタイムトラベル (1000) -143.70331[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムパラドックスの矛盾を説明するため、タイムトラベル者による歴史の改変で時間軸が分岐し元の世界と並行した別の世界が生まれるとするパラレルワールドの概念がある。この概念を発展させ、タイムトラベル者の介在がなくとも歴史上の重要なポイントで世界が枝分かれしていると解釈する立場もある。この概念を大幅に作品に取り入れた最初期の小説に、可能性として存在する二つの歴史「ジョンバール」と「ギロンチ」の抗争を描いた、ジャック・ウィリアムスンの『航時軍団』（The Legion of Time、1938年）がある。

[95mタイムトラベル (1000) -143.69884[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムトラベラーが主人公であるマーク・トウェインの「アーサー王宮廷のコネチカット・ヤンキー」や、天使が未来の書物を携えて現れるサミュエル・マッデンの「20世紀回想」など、SFというカテゴリが明確なものとして育つ以前から、タイムトラベルをテーマにした物語は創られている。

[95mタイムトラベル (1000) -143.61562[0m
[4mhttps://ja.wikipedia.org/wiki?curid=1971274[0m
タイムパラドックス（Time Paradox / 時間の逆説）は、タイムトラベルに伴う矛盾や変化のことであり、物語のテーマとしてしばしば扱われる。具体的には、タイムトラベルした過去で現代（相対的未来）に存在する事象を改変した場合、その事象における過去と現代の存在や状況、因果関係の不一致という逆説が生じることに着目したものである。
```


# Wikipedia Semantic Search with Cohere Embedding Archives

> This page contains a description of building a Wikipedia-focused semantic search engine with Cohere's LLM platform and the Weaviate vector database.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Wikipedia_Semantic_Search_With_Cohere_Embeddings_Archives.ipynb" />

This notebook contains the starter code to do simple [semantic search](https://cohere.com/llmu/what-is-semantic-search/) on the [Wikipedia embeddings archives](https://cohere.com/blog/embedding-archives-wikipedia/) published by Cohere. These archives embed Wikipedia sites in multiple languages. In this example, we'll use [Wikipedia Simple English](https://huggingface.co/datasets/Cohere/wikipedia-22-12-simple-embeddings).

Let's now download 1,000 records from the English Wikipedia embeddings archive so we can search it afterwards.

```python PYTHON
from datasets import load_dataset
import torch
import cohere
s
co = cohere.Client("")

#Load at max 1000 documents + embeddings
max_docs = 1000
docs_stream = load_dataset(f"Cohere/wikipedia-22-12-simple-embeddings", split="train", streaming=True)

docs = []
doc_embeddings = []

for doc in docs_stream:
    docs.append(doc)
    doc_embeddings.append(doc['emb'])
    if len(docs) >= max_docs:
        break

doc_embeddings = torch.tensor(doc_embeddings)
```

```txt title="Output"
Downloading:   0%|          | 0.00/1.29k [00:00<?, ?B/s]


Using custom data configuration Cohere--wikipedia-22-12-simple-embeddings-94deea3d55a22093
```

Now, `doc_embeddings` holds the embeddings of the first 1,000 documents in the dataset. Each document is represented as an [embeddings vector](https://cohere.com/llmu/sentence-word-embeddings/) of 768 values.

```python PYTHON
doc_embeddings.shape
```

```txt title="Output"
torch.Size([1000, 768])
```

We can now search these vectors for any query we want. For this toy example, we'll ask a question about Wikipedia since we know the Wikipedia page is included in the first 1000 documents we used here.

To search, we embed the query, then get the nearest neighbors to its embedding (using dot product).

```python PYTHON

query = 'Who founded Wikipedia'
response = co.embed(texts=[query], model='embed-v4.0')
query_embedding = response.embeddings
query_embedding = torch.tensor(query_embedding)

dot_scores = torch.mm(query_embedding, doc_embeddings.transpose(0, 1))
top_k = torch.topk(dot_scores, k=3)

print("Query:", query)
for doc_id in top_k.indices[0].tolist():
    print(docs[doc_id]['title'])
    print(docs[doc_id]['text'], "\n")

```

```txt title="Output"
Query: Who founded Wikipedia
Wikipedia
Larry Sanger and Jimmy Wales are the ones who started Wikipedia. Wales is credited with defining the goals of the project. Sanger created the strategy of using a wiki to reach Wales' goal. On January 10, 2001, Larry Sanger proposed on the Nupedia mailing list to create a wiki as a "feeder" project for Nupedia. Wikipedia was launched on January 15, 2001. It was launched as an English-language edition at www.wikipedia.com, and announced by Sanger on the Nupedia mailing list. Wikipedia's policy of "neutral point-of-view" was enforced in its initial months, and was similar to Nupedia's earlier "nonbiased" policy. Otherwise, there weren't very many rules initially, and Wikipedia operated independently of Nupedia.

Wikipedia
Wikipedia began as a related project for Nupedia. Nupedia was a free English-language online encyclopedia project. Nupedia's articles were written and owned by Bomis, Inc which was a web portal company. The important people of the company were Jimmy Wales, the person in charge of Bomis, and Larry Sanger, the editor-in-chief of Nupedia. Nupedia was first licensed under the Nupedia Open Content License which was changed to the GNU Free Documentation License before Wikipedia was founded and made their first article when Richard Stallman requested them.

Wikipedia
Wikipedia was started on January 10, 2001, by Jimmy Wales and Larry Sanger as part of an earlier online encyclopedia named Nupedia. On January 15, 2001, Wikipedia became a separate website of its own. It is a wiki that uses the software MediaWiki (like all other Wikimedia Foundation projects).
```

This shows the top three passages that are relevant to the query. We can retrieve more results by changing the `k` value. The question in this simple demo is about Wikipedia because we know that the Wikipedia page is part of the documents in this subset of the archive.


# Build Chatbots with MongoDB and Cohere

> This page describes how to build a chatbot that provides actionable insights on technology company market reports.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/rag_chatbot_with_cohere_and_mongodb.ipynb" />

**What you will learn:**

* How to empower leverage semantic search on customer or operational data in MongoDB Atlas.
* Pass retrieved data to Cohere’s Command R+ generative model for retrieval-augmented generation (RAG).
* Develop and deploy a RAG-optimized user interface for your app.
* Create a conversation data store for your RAG chatbot using MongoDB

**Use Case**: Develop an advanced chatbot assistant that provides asset managers with information and actionable insights on technology company market reports.

## Introduction

* What is Cohere?
* What is MongoDB?
* How Cohere and MongoDB work together?

### What is Cohere?

![](file:e0cf8abc-25b2-4357-8839-1ee549afd119)

### What is MongoDB?

![](file:ce90f111-619d-44c3-bdd9-1e578a99b9f9)

### What exactly are we showing today?

![](file:a540f3e6-edec-4c6b-9810-a635391b237d)

## Step 1: Install libaries and Set Environment Variables

Critical Security Reminder: Safeguard your production environment by never committing sensitive information, such as environment variable values, to public repositories. This practice is essential for maintaining the security and integrity of your systems.

Libraries:

* `cohere`: A Python library for accessing Cohere's large language models, enabling natural language processing tasks like text generation, classification, and embedding.
* `pymongo`: The recommended Python driver for MongoDB, allowing Python applications to interact with MongoDB databases for data storage and retrieval.
* `datasets`: A library by Hugging Face that provides easy access to a wide range of datasets for machine learning and natural language processing tasks.
  \*`tqdm`: A fast, extensible progress bar library for Python, useful for displaying progress in long-running operations or loops.

```sh
pip install --quiet datasets tqdm cohere pymongo
```

```python
import os
import cohere

os.environ["COHERE_API_KEY"] = ""
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

os.environ["HF_TOKEN"] = ""
```

## Step 2: Data Loading and Preparation

**Dataset Information**

This dataset contains detailed information about multiple technology companies in the Information Technology sector. For each company, the dataset includes:

1. Company name and stock ticker symbol
2. Market analysis reports for recent years (typically 2023 and 2024), which include:

* Title and author of the report
* Date of publication
* Detailed content covering financial performance, product innovations, market position, challenges, and future outlook
* Stock recommendations and price targets

3. Key financial metrics such as:

* Current stock price
* 52-week price range
* Market capitalization
* Price-to-earnings (P/E) ratio
* Dividend yield

4. Recent news items, typically including:

* Date of the news
* Headline
* Brief summary

The market analysis reports provide in-depth information about each company's performance, innovations, challenges, and future prospects. They offer insights into the companies' strategies, market positions, and potential for growth.

```python
import pandas as pd
from datasets import load_dataset

# Make sure you have an Hugging Face token(HF_TOKEN) in your development environemnt before running the code below
# How to get a token: https://huggingface.co/docs/hub/en/security-tokens
# https://huggingface.co/datasets/MongoDB/fake_tech_companies_market_reports
dataset = load_dataset(
    "MongoDB/fake_tech_companies_market_reports",
    split="train",
    streaming=True,
)
dataset_df = dataset.take(100)

# Convert the dataset to a pandas dataframe
dataset_df = pd.DataFrame(dataset_df)
dataset_df.head(5)
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          recent_news
        </th>

        <th>
          reports
        </th>

        <th>
          company
        </th>

        <th>
          ticker
        </th>

        <th>
          key_metrics
        </th>

        <th>
          sector
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          \[{'date': '2024-06-09', 'headline': 'CyberDefe...
        </td>

        <td>
          \[{'author': 'Taylor Smith, Technology Sector L...
        </td>

        <td>
          CyberDefense Dynamics
        </td>

        <td>
          CDDY
        </td>

        <td>
          \{'52_week_range': {'high': 387.3, 'low': 41.63...
        </td>

        <td>
          Information Technology
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          \[{'date': '2024-07-04', 'headline': 'CloudComp...
        </td>

        <td>
          \[{'author': 'Casey Jones, Chief Market Strateg...
        </td>

        <td>
          CloudCompute Pro
        </td>

        <td>
          CCPR
        </td>

        <td>
          \{'52_week_range': {'high': 524.23, 'low': 171....
        </td>

        <td>
          Information Technology
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          \[{'date': '2024-06-27', 'headline': 'VirtualRe...
        </td>

        <td>
          \[{'author': 'Sam Brown, Head of Equity Researc...
        </td>

        <td>
          VirtualReality Systems
        </td>

        <td>
          VRSY
        </td>

        <td>
          \{'52_week_range': {'high': 530.59, 'low': 56.4...
        </td>

        <td>
          Information Technology
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'date': '2024-07-06', 'headline': 'BioTech I...
        </td>

        <td>
          \[{'author': 'Riley Smith, Senior Tech Analyst...
        </td>

        <td>
          BioTech Innovations
        </td>

        <td>
          BTCI
        </td>

        <td>
          \{'52_week_range': {'high': 366.55, 'low': 124...
        </td>

        <td>
          Information Technology
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          \[{'date': '2024-06-26', 'headline': 'QuantumCo...
        </td>

        <td>
          \[{'author': 'Riley Garcia, Senior Tech Analyst...
        </td>

        <td>
          QuantumComputing Inc
        </td>

        <td>
          QCMP
        </td>

        <td>
          \{'52_week_range': {'high': 231.91, 'low': 159...
        </td>

        <td>
          Information Technology
        </td>
      </tr>
    </tbody>
  </table>
</div>

```python
# Data Preparation
def combine_attributes(row):
    combined = f"{row['company']} {row['sector']} "

    # Add reports information
    for report in row["reports"]:
        combined += f"{report['year']} {report['title']} {report['author']} {report['content']} "

    # Add recent news information
    for news in row["recent_news"]:
        combined += f"{news['headline']} {news['summary']} "

    return combined.strip()
```

```python
# Add the new column 'combined_attributes'
dataset_df["combined_attributes"] = dataset_df.apply(
    combine_attributes, axis=1
)
```

```python
# Display the first few rows of the updated dataframe
dataset_df[["company", "ticker", "combined_attributes"]].head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          company
        </th>

        <th>
          ticker
        </th>

        <th>
          combined_attributes
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          CyberDefense Dynamics
        </td>

        <td>
          CDDY
        </td>

        <td>
          CyberDefense Dynamics Information Technology 2...
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          CloudCompute Pro
        </td>

        <td>
          CCPR
        </td>

        <td>
          CloudCompute Pro Information Technology 2023 C...
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          VirtualReality Systems
        </td>

        <td>
          VRSY
        </td>

        <td>
          VirtualReality Systems Information Technology ...
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          BioTech Innovations
        </td>

        <td>
          BTCI
        </td>

        <td>
          BioTech Innovations Information Technology 202...
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          QuantumComputing Inc
        </td>

        <td>
          QCMP
        </td>

        <td>
          QuantumComputing Inc Information Technology 20...
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Step 3: Embedding Generation with Cohere

```python
from tqdm import tqdm


def get_embedding(
    text: str, input_type: str = "search_document"
) -> list[float]:
    if not text.strip():
        print("Attempted to get embedding for empty text.")
        return []

    model = "embed-v4.0"
    response = co.embed(
        texts=[text],
        model=model,
        input_type=input_type,  # Used for embeddings of search queries run against a vector DB to find relevant documents
        embedding_types=["float"],
    )

    return response.embeddings.float[0]


# Apply the embedding function with a progress bar
tqdm.pandas(desc="Generating embeddings")
dataset_df["embedding"] = dataset_df[
    "combined_attributes"
].progress_apply(get_embedding)

print(f"We just computed {len(dataset_df['embedding'])} embeddings.")
```

We just computed 63 embeddings.

```python
dataset_df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          recent_news
        </th>

        <th>
          reports
        </th>

        <th>
          company
        </th>

        <th>
          ticker
        </th>

        <th>
          key_metrics
        </th>

        <th>
          sector
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          embedding
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          \[{'date': '2024-06-09', 'headline': 'CyberDefe...
        </td>

        <td>
          \[{'author': 'Taylor Smith, Technology Sector L...
        </td>

        <td>
          CyberDefense Dynamics
        </td>

        <td>
          CDDY
        </td>

        <td>
          \{'52_week_range': {'high': 387.3, 'low': 41.63...
        </td>

        <td>
          Information Technology
        </td>

        <td>
          CyberDefense Dynamics Information Technology 2...
        </td>

        <td>
          \[0.01210022, -0.03466797, -0.017562866, -0.025...
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          \[{'date': '2024-07-04', 'headline': 'CloudComp...
        </td>

        <td>
          \[{'author': 'Casey Jones, Chief Market Strateg...
        </td>

        <td>
          CloudCompute Pro
        </td>

        <td>
          CCPR
        </td>

        <td>
          \{'52_week_range': {'high': 524.23, 'low': 171....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          CloudCompute Pro Information Technology 2023 C...
        </td>

        <td>
          \[-0.058563232, -0.06323242, -0.037139893, -0.0...
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          \[{'date': '2024-06-27', 'headline': 'VirtualRe...
        </td>

        <td>
          \[{'author': 'Sam Brown, Head of Equity Researc...
        </td>

        <td>
          VirtualReality Systems
        </td>

        <td>
          VRSY
        </td>

        <td>
          \{'52_week_range': {'high': 530.59, 'low': 56.4...
        </td>

        <td>
          Information Technology
        </td>

        <td>
          VirtualReality Systems Information Technology ...
        </td>

        <td>
          \[0.024154663, -0.022872925, -0.01751709, -0.05...
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'date': '2024-07-06', 'headline': 'BioTech I...
        </td>

        <td>
          \[{'author': 'Riley Smith, Senior Tech Analyst'...
        </td>

        <td>
          BioTech Innovations
        </td>

        <td>
          BTCI
        </td>

        <td>
          \{'52_week_range': {'high': 366.55, 'low': 124....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          BioTech Innovations Information Technology 202...
        </td>

        <td>
          \[0.020736694, -0.041046143, -0.0029773712, -0....
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          \[{'date': '2024-06-26', 'headline': 'QuantumCo...
        </td>

        <td>
          \[{'author': 'Riley Garcia, Senior Tech Analyst...
        </td>

        <td>
          QuantumComputing Inc
        </td>

        <td>
          QCMP
        </td>

        <td>
          \{'52_week_range': {'high': 231.91, 'low': 159....
        </td>

        <td>
          Information Technology
        </td>

        <td>
          QuantumComputing Inc Information Technology 20...
        </td>

        <td>
          \[-0.009757996, -0.04815674, 0.039611816, 0.023...
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Step 4: MongoDB Vector Database and Connection Setup

MongoDB acts as both an operational and a vector database for the RAG system.
MongoDB Atlas specifically provides a database solution that efficiently stores, queries and retrieves vector embeddings.

Creating a database and collection within MongoDB is made simple with MongoDB Atlas.

1. First, register for a [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas/register). For existing users, sign into MongoDB Atlas.
2. [Follow the instructions](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/). Select Atlas UI as the procedure to deploy your first cluster.
3. Create the database: `asset_management_use_case`.
4. Within the database ` asset_management_use_case`, create the collection `market_reports`.
5. Create a [vector search index](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/#procedure/) named vector\_index for the ‘listings\_reviews’ collection. This index enables the RAG application to retrieve records as additional context to supplement user queries via vector search. Below is the JSON definition of the data collection vector search index.

Your vector search index created on MongoDB Atlas should look like below:

```
{
  "fields": [
    {
      "numDimensions": 1024,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}

```

Follow MongoDB’s [steps to get the connection](https://www.mongodb.com/docs/manual/reference/connection-string/) string from the Atlas UI. After setting up the database and obtaining the Atlas cluster connection URI, securely store the URI within your development environment.

```python
import os

os.environ["MONGO_URI"] = ""
```

```python
import pymongo


def get_mongo_client(mongo_uri):
    """Establish and validate connection to the MongoDB."""

    client = pymongo.MongoClient(
        mongo_uri, appname="devrel.showcase.rag.cohere_mongodb.python"
    )

    # Validate the connection
    ping_result = client.admin.command("ping")
    if ping_result.get("ok") == 1.0:
        # Connection successful
        print("Connection to MongoDB successful")
        return client
    else:
        print("Connection to MongoDB failed")
    return None


MONGO_URI = os.environ["MONGO_URI"]

if not MONGO_URI:
    print("MONGO_URI not set in environment variables")

mongo_client = get_mongo_client(MONGO_URI)

DB_NAME = "asset_management_use_case"
COLLECTION_NAME = "market_reports"

db = mongo_client.get_database(DB_NAME)
collection = db.get_collection(COLLECTION_NAME)
```

Connection to MongoDB successful

```python
# Delete any existing records in the collection
collection.delete_many({})
```

```

DeleteResult({'n': 63, 'electionId': ObjectId('7fffffff000000000000002b'), 'opTime': {'ts': Timestamp(1721913981, 63), 't': 43}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1721913981, 63), 'signature': {'hash': b'cU;+\xe3\xbdRc\t\x80\xad\x03\x16\x11\x18\xe6s\xebF\x01', 'keyId': 7353740577831124994}}, 'operationTime': Timestamp(1721913981, 63)}, acknowledged=True)

```

## Step 5: Data Ingestion

MongoDB's Document model and its compatibility with Python dictionaries offer several benefits for data ingestion.

* Document-oriented structure:
  * MongoDB stores data in JSON-like documents: BSON(Binary JSON).
  * This aligns naturally with Python dictionaries, allowing for seamless data representation using key value pair data structures.
* Schema flexibility:
  * MongoDB is schema-less, meaning each document in a collection can have a different structure.
  * This flexibility matches Python's dynamic nature, allowing you to ingest varied data structures without predefined schemas.
* Efficient ingestion:
  * The similarity between Python dictionaries and MongoDB documents allows for direct ingestion without complex transformations.
  * This leads to faster data insertion and reduced processing overhead.

![](file:e6782400-2bf8-4283-b6b5-d37ee857d715)

```python
documents = dataset_df.to_dict("records")
collection.insert_many(documents)

print("Data ingestion into MongoDB completed")
```

Data ingestion into MongoDB completed

## Step 6: MongoDB Query language and Vector Search

**Query flexibility**

MongoDB's query language is designed to work well with document structures, making it easy to query and manipulate ingested data using familiar Python-like syntax.

**Aggregation Pipeline**

MongoDB's aggregation pipelines is a powerful feature of the MongoDB Database that allows for complex data processing and analysis within the database.
Aggregation pipeline can be thought of similarly to pipelines in data engineering or machine learning, where processes operate sequentially, each stage taking an input, performing operations, and providing an output for the next stage.

**Stages**

Stages are the building blocks of an aggregation pipeline.
Each stage represents a specific data transformation or analysis operation.
Common stages include:

* `$match`: Filters documents (similar to WHERE in SQL)
* `$group`: Groups documents by specified fields
* `$sort`: Sorts the documents
* `$project`: Reshapes documents (select, rename, compute fields)
* `$limit`: Limits the number of documents
* `$unwind`: Deconstructs array fields
* `$lookup`: Performs left outer joins with other collections

![](file:8ca192ab-21bb-45d7-ada8-53a8abc322aa)

```python
def vector_search(user_query, collection):
    """
    Perform a vector search in the MongoDB collection based on the user query.

    Args:
    user_query (str): The user's query string.
    collection (MongoCollection): The MongoDB collection to search.

    Returns:
    list: A list of matching documents.
    """

    # Generate embedding for the user query
    query_embedding = get_embedding(
        user_query, input_type="search_query"
    )

    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    # Define the vector search pipeline
    vector_search_stage = {
        "$vectorSearch": {
            "index": "vector_index",
            "queryVector": query_embedding,
            "path": "embedding",
            "numCandidates": 150,  # Number of candidate matches to consider
            "limit": 5,  # Return top 4 matches
        }
    }

    unset_stage = {
        "$unset": "embedding"  # Exclude the 'embedding' field from the results
    }

    project_stage = {
        "$project": {
            "_id": 0,  # Exclude the _id field
            "company": 1,  # Include the plot field
            "reports": 1,  # Include the title field
            "combined_attributes": 1,  # Include the genres field
            "score": {
                "$meta": "vectorSearchScore"  # Include the search score
            },
        }
    }

    pipeline = [vector_search_stage, unset_stage, project_stage]

    # Execute the search
    results = collection.aggregate(pipeline)
    return list(results)
```

## Step 7:  Add the Cohere Reranker

Cohere rerank functions as a second stage search that can improve the precision of your first stage search results

![](file:470cf874-d7a4-45c4-9b12-aaf0776e2930)

```python
def rerank_documents(query: str, documents, top_n: int = 3):
    # Perform reranking with Cohere ReRank Model
    try:
        response = co.rerank(
            model="rerank-english-v3.0",
            query=query,
            documents=documents,
            top_n=top_n,
            rank_fields=["company", "reports", "combined_attributes"],
        )

        # Extract the top reranked documents
        top_documents_after_rerank = []
        for result in response.results:
            original_doc = documents[result.index]
            top_documents_after_rerank.append(
                {
                    "company": original_doc["company"],
                    "combined_attributes": original_doc[
                        "combined_attributes"
                    ],
                    "reports": original_doc["reports"],
                    "vector_search_score": original_doc["score"],
                    "relevance_score": result.relevance_score,
                }
            )

        return top_documents_after_rerank

    except Exception as e:
        print(f"An error occurred during reranking: {e}")
        # Return top N documents without reranking
        return documents[:top_n]
```

```python
import pprint

query = "What companies have negative market reports or negative sentiment that might deter from investment in the long term"

get_knowledge = vector_search(query, collection)
pd.DataFrame(get_knowledge).head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          reports
        </th>

        <th>
          company
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          \[{'author': 'Jordan Garcia, Senior Tech Analys...
        </td>

        <td>
          GreenEnergy Corp
        </td>

        <td>
          GreenEnergy Corp Information Technology 2023 G...
        </td>

        <td>
          0.659524
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          \[{'author': 'Morgan Smith, Technology Sector L...
        </td>

        <td>
          BioTech Therapeutics
        </td>

        <td>
          BioTech Therapeutics Information Technology 20...
        </td>

        <td>
          0.646300
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          \[{'author': 'Casey Davis, Technology Sector Le...
        </td>

        <td>
          RenewableEnergy Innovations
        </td>

        <td>
          RenewableEnergy Innovations Information Techno...
        </td>

        <td>
          0.645224
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          \[{'author': 'Morgan Johnson, Technology Sector...
        </td>

        <td>
          QuantumSensor Corp
        </td>

        <td>
          QuantumSensor Corp Information Technology 2023...
        </td>

        <td>
          0.644383
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          \[{'author': 'Morgan Williams, Senior Tech Anal...`
        </td>

        <td>
          BioEngineering Corp
        </td>

        <td>
          BioEngineering Corp Information Technology 202...
        </td>

        <td>
          0.643690
        </td>
      </tr>
    </tbody>
  </table>
</div>

```python
reranked_documents = rerank_documents(query, get_knowledge)
pd.DataFrame(reranked_documents).head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          company
        </th>

        <th>
          combined_attributes
        </th>

        <th>
          reports
        </th>

        <th>
          vector_search_score
        </th>

        <th>
          relevance_score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          GreenEnergy Corp
        </td>

        <td>
          GreenEnergy Corp Information Technology 2023 G...
        </td>

        <td>
          \[{'author': 'Jordan Garcia, Senior Tech Analys...
        </td>

        <td>
          0.659524
        </td>

        <td>
          0.000147
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          BioEngineering Corp
        </td>

        <td>
          BioEngineering Corp Information Technology 202...
        </td>

        <td>
          \[{'author': 'Morgan Williams, Senior Tech Anal...
        </td>

        <td>
          0.643690
        </td>

        <td>
          0.000065
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          QuantumSensor Corp
        </td>

        <td>
          QuantumSensor Corp Information Technology 2023...
        </td>

        <td>
          \[{'author': 'Morgan Johnson, Technology Sector...
        </td>

        <td>
          0.644383
        </td>

        <td>
          0.000054
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Step 8: Handling User Queries

```python
def format_documents_for_chat(documents):
    return [
        {
            "company": doc["company"],
            # "reports": doc['reports'],
            "combined_attributes": doc["combined_attributes"],
        }
        for doc in documents
    ]


# Generating response with Cohere Command R
response = co.chat(
    message=query,
    documents=format_documents_for_chat(reranked_documents),
    model="command-a-03-2025",
    temperature=0.3,
)

print("Final answer:")
print(response.text)
```

Final answer:
Here is an overview of the companies with negative market reports or sentiment that might deter long-term investment:

## GreenEnergy Corp (GRNE):

* **Challenges**: Despite solid financial performance and a positive market position, GRNE faces challenges due to the volatile political environment and rising trade tensions, resulting in increased tariffs and supply chain disruptions.
* **Regulatory Scrutiny**: The company is under scrutiny for its data handling practices, raising concerns about potential privacy breaches and ethical dilemmas.

## BioEngineering Corp (BENC):

* **Regulatory Hurdles**: BENC faces delays in obtaining approvals for certain products due to stringent healthcare regulations, impacting their time-to-market.
* **Reimbursement and Pricing Pressures**: As healthcare costs rise, the company must carefully navigate pricing strategies to balance accessibility and profitability.
* **Research and Development Expenses**: BENC has experienced a significant increase in R\&D expenses, which may impact its ability to maintain a competitive pricing strategy.

## QuantumSensor Corp (QSCP):

* **Supply Chain Disruptions**: QSCP has faced supply chain issues due to global logistics problems and geopolitical tensions, impacting production and delivery.
* **Regulatory Scrutiny**: The company is under scrutiny for its data collection and handling practices, with potential privacy and ethical concerns.
* **Technical Workforce Challenges**: Attracting and retaining skilled talent in a competitive market has been challenging for QSCP.

```python
for cite in response.citations:
    print(cite)
```

```
start=122 end=145 text='GreenEnergy Corp (GRNE)' document_ids=['doc_0']
start=151 end=161 text='Challenges' document_ids=['doc_0']
start=173 end=231 text='solid financial performance and a positive market position' document_ids=['doc_0']
start=266 end=322 text='volatile political environment and rising trade tensions' document_ids=['doc_0']
start=337 end=384 text='increased tariffs and supply chain disruptions.' document_ids=['doc_0']
start=390 end=409 text='Regulatory Scrutiny' document_ids=['doc_0']
start=428 end=474 text='under scrutiny for its data handling practices' document_ids=['doc_0']
start=484 end=547 text='concerns about potential privacy breaches and ethical dilemmas.' document_ids=['doc_0']
start=552 end=578 text='BioEngineering Corp (BENC)' document_ids=['doc_1']
start=584 end=602 text='Regulatory Hurdles' document_ids=['doc_1']
start=617 end=667 text='delays in obtaining approvals for certain products' document_ids=['doc_1']
start=675 end=707 text='stringent healthcare regulations' document_ids=['doc_1']
start=725 end=740 text='time-to-market.' document_ids=['doc_1']
start=745 end=780 text='Reimbursement and Pricing Pressures' document_ids=['doc_1']
start=787 end=808 text='healthcare costs rise' document_ids=['doc_1']
start=827 end=864 text='carefully navigate pricing strategies' document_ids=['doc_1']
start=868 end=908 text='balance accessibility and profitability.' document_ids=['doc_1']
start=913 end=946 text='Research and Development Expenses' document_ids=['doc_1']
start=973 end=1009 text='significant increase in R&D expenses' document_ids=['doc_1']
start=1043 end=1083 text='maintain a competitive pricing strategy.' document_ids=['doc_1']
start=1088 end=1113 text='QuantumSensor Corp (QSCP)' document_ids=['doc_2']
start=1119 end=1143 text='Supply Chain Disruptions' document_ids=['doc_2']
start=1162 end=1181 text='supply chain issues' document_ids=['doc_2']
start=1189 end=1240 text='global logistics problems and geopolitical tensions' document_ids=['doc_2']
start=1252 end=1276 text='production and delivery.' document_ids=['doc_2']
start=1281 end=1300 text='Regulatory Scrutiny' document_ids=['doc_2']
start=1319 end=1380 text='under scrutiny for its data collection and handling practices' document_ids=['doc_2']
start=1387 end=1426 text='potential privacy and ethical concerns.' document_ids=['doc_2']
start=1431 end=1461 text='Technical Workforce Challenges' document_ids=['doc_2']
start=1465 end=1528 text='Attracting and retaining skilled talent in a competitive market' document_ids=['doc_2']
```

## Step 9: Using MongoDB as a Data Store for Conversation History

```python
from typing import Dict, Optional, List


class CohereChat:

    def __init__(
        self,
        cohere_client,
        system: str = "",
        database: str = "cohere_chat",
        main_collection: str = "main_collection",
        history_params: Optional[Dict[str, str]] = None,
    ):
        self.co = cohere_client
        self.system = system
        self.history_params = history_params or {}

        # Use the connection string from history_params
        self.client = pymongo.MongoClient(
            self.history_params.get(
                "connection_string", "mongodb://localhost:27017/"
            )
        )

        # Use the database parameter
        self.db = self.client[database]

        # Use the main_collection parameter
        self.main_collection = self.db[main_collection]

        # Use the history_collection from history_params, or default to "chat_history"
        self.history_collection = self.db[
            self.history_params.get(
                "history_collection", "chat_history"
            )
        ]

        # Use the session_id from history_params, or default to "default_session"
        self.session_id = self.history_params.get(
            "session_id", "default_session"
        )

    def add_to_history(self, message: str, prefix: str = ""):
        self.history_collection.insert_one(
            {
                "session_id": self.session_id,
                "message": message,
                "prefix": prefix,
            }
        )

    def get_chat_history(self) -> List[Dict[str, str]]:
        history = self.history_collection.find(
            {"session_id": self.session_id}
        ).sort("_id", 1)
        return [
            {
                "role": (
                    "user" if item["prefix"] == "USER" else "chatbot"
                ),
                "message": item["message"],
            }
            for item in history
        ]

    def rerank_documents(
        self, query: str, documents: List[Dict], top_n: int = 3
    ) -> List[Dict]:
        rerank_docs = [
            {
                "company": doc["company"],
                "combined_attributes": doc["combined_attributes"],
            }
            for doc in documents
            if doc["combined_attributes"].strip()
        ]

        if not rerank_docs:
            print("No valid documents to rerank.")
            return []

        try:
            response = self.co.rerank(
                query=query,
                documents=rerank_docs,
                top_n=top_n,
                model="rerank-english-v3.0",
                rank_fields=["company", "combined_attributes"],
            )

            top_documents_after_rerank = [
                {
                    "company": rerank_docs[result.index]["company"],
                    "combined_attributes": rerank_docs[result.index][
                        "combined_attributes"
                    ],
                    "relevance_score": result.relevance_score,
                }
                for result in response.results
            ]

            print(
                f"\nHere are the top {top_n} documents after rerank:"
            )
            for doc in top_documents_after_rerank:
                print(
                    f"== {doc['company']} (Relevance: {doc['relevance_score']:.4f})"
                )

            return top_documents_after_rerank

        except Exception as e:
            print(f"An error occurred during reranking: {e}")
            return documents[:top_n]

    def format_documents_for_chat(
        self, documents: List[Dict]
    ) -> List[Dict]:
        return [
            {
                "company": doc["company"],
                "combined_attributes": doc["combined_attributes"],
            }
            for doc in documents
        ]

    def send_message(self, message: str, vector_search_func) -> str:
        self.add_to_history(message, "USER")

        # Perform vector search
        search_results = vector_search_func(
            message, self.main_collection
        )

        # Rerank the search results
        reranked_documents = self.rerank_documents(
            message, search_results
        )

        # Format documents for chat
        formatted_documents = self.format_documents_for_chat(
            reranked_documents
        )

        # Generate response using Cohere chat
        response = self.co.chat(
            chat_history=self.get_chat_history(),
            message=message,
            documents=formatted_documents,
            model="command-a-03-2025",
            temperature=0.3,
        )

        result = response.text
        self.add_to_history(result, "CHATBOT")

        print("Final answer:")
        print(result)

        print("\nCitations:")
        for cite in response.citations:
            print(cite)

        return result

    def show_history(self):
        history = self.history_collection.find(
            {"session_id": self.session_id}
        ).sort("_id", 1)
        for item in history:
            print(f"{item['prefix']}: {item['message']}")
            print("-------------------------")
```

```python
# Initialize CohereChat
chat = CohereChat(
    co,
    system="You are a helpful assistant taking on the role of an Asset Manager focused on tech companies.",
    database=DB_NAME,
    main_collection=COLLECTION_NAME,
    history_params={
        "connection_string": MONGO_URI,
        "history_collection": "chat_history",
        "session_id": 2,
    },
)

# Send a message
response = chat.send_message(
    "What is the best investment to make why?", vector_search
)
```

```
Here are the top 3 documents after rerank:
== EcoTech Innovations (Relevance: 0.0001)
== GreenEnergy Systems (Relevance: 0.0001)
== QuantumComputing Inc (Relevance: 0.0000)
Final answer:
I am an AI assistant and cannot comment on what the single "best" investment is. However, I have found some companies that have been recommended as "Buy" investments in the documents provided. 

## EcoTech Innovations (ETIN)
EcoTech Innovations is a leading provider of sustainable technology solutions, specializing in renewable energy and environmentally friendly products. In 2023 and 2024, ETIN demonstrated solid financial performance, innovative capabilities, and a growing market presence, making it an attractive investment opportunity for those interested in the sustainable technology sector. 

## GreenEnergy Systems (GESY)
GreenEnergy Systems is a leading provider of renewable energy solutions, offering solar and wind power technologies, energy storage systems, and smart grid solutions. In 2023 and 2024, GESY reported strong financial performance, innovative product developments, and a solid market position, positioning it well for future growth in the renewable energy sector. 

## QuantumComputing Inc. (QCMP)
QuantumComputing Inc. is a leading developer of quantum computing software and solutions, aiming to revolutionize computing tasks across industries. In 2023 and 2024, QCMP demonstrated strong financial performance, innovative product offerings, and a growing market presence, making it an attractive investment opportunity in the rapidly growing quantum computing industry. 

Please note that these recommendations are based on specific reports and may not consider all factors. It is always advisable to conduct thorough research and consult professional advice before making any investment decisions.

Citations:
start=148 end=153 text='"Buy"' document_ids=['doc_0', 'doc_1', 'doc_2']
start=198 end=224 text='EcoTech Innovations (ETIN)' document_ids=['doc_0']
start=250 end=302 text='leading provider of sustainable technology solutions' document_ids=['doc_0']
start=320 end=375 text='renewable energy and environmentally friendly products.' document_ids=['doc_0']
start=379 end=383 text='2023' document_ids=['doc_0']
start=388 end=392 text='2024' document_ids=['doc_0']
start=412 end=439 text='solid financial performance' document_ids=['doc_0', 'doc_1']
start=441 end=464 text='innovative capabilities' document_ids=['doc_0']
start=472 end=495 text='growing market presence' document_ids=['doc_0', 'doc_1']
start=572 end=602 text='sustainable technology sector.' document_ids=['doc_0']
start=608 end=634 text='GreenEnergy Systems (GESY)' document_ids=['doc_1']
start=660 end=706 text='leading provider of renewable energy solutions' document_ids=['doc_1']
start=717 end=801 text='solar and wind power technologies, energy storage systems, and smart grid solutions.' document_ids=['doc_1']
start=805 end=809 text='2023' document_ids=['doc_1']
start=814 end=818 text='2024' document_ids=['doc_1']
start=834 end=862 text='strong financial performance' document_ids=['doc_1']
start=864 end=895 text='innovative product developments' document_ids=['doc_1']
start=903 end=924 text='solid market position' document_ids=['doc_1']
start=971 end=995 text='renewable energy sector.' document_ids=['doc_1']
start=1001 end=1029 text='QuantumComputing Inc. (QCMP)' document_ids=['doc_2']
start=1057 end=1118 text='leading developer of quantum computing software and solutions' document_ids=['doc_2']
start=1130 end=1178 text='revolutionize computing tasks across industries.' document_ids=['doc_2']
start=1182 end=1186 text='2023' document_ids=['doc_2']
start=1191 end=1195 text='2024' document_ids=['doc_2']
start=1215 end=1243 text='strong financial performance' document_ids=['doc_2']
start=1245 end=1273 text='innovative product offerings' document_ids=['doc_2']
start=1281 end=1304 text='growing market presence' document_ids=['doc_2']
start=1360 end=1403 text='rapidly growing quantum computing industry.' document_ids=['doc_2']
```

```python
# Show chat history
chat.show_history()
```

```
USER: What is the best investment to make why?
-------------------------
CHATBOT: I am an AI assistant and therefore cannot comment on what the single "best" investment is. However, I can tell you about some companies that have been recommended as "Buy" investments in the documents provided. 

## CloudInfra Systems (CISY)
CloudInfra Systems is a leading provider of cloud computing solutions, offering infrastructure-as-a-service (IaaS) and platform-as-a-service (PaaS) to businesses worldwide. In 2023, CISY demonstrated strong financial performance and product innovation, making it an attractive investment opportunity. 

## VirtualReality Systems (VRSY)
VirtualReality Systems is a leading provider of virtual reality hardware and software solutions. In 2023, VRSY reported strong financial performance, innovative product developments, and strategic partnerships, positioning it well in a rapidly growing and competitive market. 

## BioTech Innovations (BTCI)
BioTech Innovations is a leading biotechnology company specializing in healthcare solutions and innovative medicines. In 2023, BTCI demonstrated solid financial growth, product innovations, and a strengthened market position, making it an attractive investment option for long-term growth prospects. 

Please note that these recommendations are based on specific reports and may not consider all factors. It is always advisable to conduct thorough research and consult professional advice before making any investment decisions.
-------------------------
USER: What is the best investment to make why?
-------------------------
CHATBOT: I am an AI assistant and therefore cannot comment on what the single "best" investment is. However, I can provide you with some companies that have been recommended as "Buy" investments in the documents provided. 

## CloudInfra Systems (CISY)
CloudInfra Systems is a leading provider of cloud computing solutions, offering infrastructure-as-a-service (IaaS) and platform-as-a-service (PaaS) to businesses worldwide. In 2023, CISY demonstrated strong financial performance and product innovation, making it an attractive investment opportunity. 

## VirtualReality Systems (VRSY)
VirtualReality Systems is a leading provider of virtual reality hardware and software solutions. In 2023, VRSY reported strong financial performance, innovative product developments, and strategic partnerships, positioning it well in a rapidly growing and competitive market. 

## BioTech Innovations (BTCI)
BioTech Innovations is a leading biotechnology company specializing in healthcare solutions and innovative medicines. In 2023, BTCI demonstrated solid financial growth, product innovations, and a strengthened market position, making it an attractive investment option for long-term growth prospects. 

Please note that these recommendations are based on specific reports and may not consider all factors. It is always advisable to conduct thorough research and consult professional advice before making any investment decisions.
-------------------------
USER: What is the best investment to make why?
-------------------------
CHATBOT: I am an AI assistant and cannot comment on what the single "best" investment is. However, I can provide information on companies that have been recommended as "Buy" investments in the documents provided. 

## CloudInfra Systems (CISY)
CloudInfra Systems is a leading provider of cloud computing solutions, offering infrastructure-as-a-service (IaaS) and platform-as-a-service (PaaS) to a diverse range of businesses. In 2023, CISY demonstrated strong financial performance and product innovation, positioning it well in the competitive cloud market. 

## VirtualReality Systems (VRSY)
VirtualReality Systems is a leading provider of virtual reality hardware and software solutions. In 2023, VRSY reported robust financial results, innovative product developments, and strategic partnerships, making it a solid investment choice for those with a long-term investment horizon. 

## BioTech Innovations (BTCI)
BioTech Innovations is a leading biotechnology company specializing in healthcare solutions and innovative medicines. In 2023 and 2024, BTCI demonstrated solid financial growth, product innovations, and an improved market position, making it an attractive investment opportunity for long-term growth. 

Please note that these recommendations are based on specific reports and may not consider all factors. It is always advisable to conduct thorough research and consult professional advice before making any investment decisions.
-------------------------
USER: What is the best investment to make why?
-------------------------
CHATBOT: I am an AI assistant and cannot comment on what the single "best" investment is. However, I have found some companies that have been recommended as "Buy" investments in the documents provided. 

## EcoTech Innovations (ETIN)
EcoTech Innovations is a leading provider of sustainable technology solutions, specializing in renewable energy and environmentally friendly products. In 2023 and 2024, ETIN demonstrated solid financial performance, innovative capabilities, and a growing market presence, making it an attractive investment opportunity for those interested in the sustainable technology sector. 

## GreenEnergy Systems (GESY)
GreenEnergy Systems is a leading provider of renewable energy solutions, offering solar and wind power technologies, energy storage systems, and smart grid solutions. In 2023 and 2024, GESY reported strong financial performance, innovative product developments, and a solid market position, positioning it well for future growth in the renewable energy sector. 

## QuantumComputing Inc. (QCMP)
QuantumComputing Inc. is a leading developer of quantum computing software and solutions, aiming to revolutionize computing tasks across industries. In 2023 and 2024, QCMP demonstrated strong financial performance, innovative product offerings, and a growing market presence, making it an attractive investment opportunity in the rapidly growing quantum computing industry. 

Please note that these recommendations are based on specific reports and may not consider all factors. It is always advisable to conduct thorough research and consult professional advice before making any investment decisions.
-------------------------
```


# Finetuning on Cohere's Platform

> An example of finetuning using Cohere's platform and a financial dataset.

<AuthorsContainer
  authors={[
    {
      name: "Komal Teru",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/7026fcc-komal-headshot.jpg"
    }
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/finetuning/convfinqa_finetuning_wandb.ipynb" />

## Overview

Cohere chat models (Comand R and Command R+) are fantastic generally capable models out of the box. To further adopt our models for specific tasks, there are several strategies like prompt engineering, RAG, tool use, finetuning. In this cookbook, we will focus on finetuning. While the other strategies involve careful and intelligent orchestration of our models out of the box, finetuning involves modifying the weights to specialize the model for a task at hand. This requires careful investment of time and resources from data collection to model training. This is typically employed when all other strategies fall short.

Our finetuning service allows customization of our latest Command R model (command-r-08-2024) with LoRA based finetuning which gives users the the ability to control model flexibility depending on their task. Additionally, we extended the training context length to 16384 tokens giving users the ability to user longer training data points which is typical for RAG, agents, and tool use. In this cookbook, we will showcase model customization via our [Finetuning API](https://cohere-preview-6021ac31-6091-4dd4-a195-dc3456f6883c.docs.buildwithfern.com/reference/createfinetunedmodel) and also show you how to monitor loss functions for your finetuning jobs using the [Weights & Biases integration](#sec_wandb). Please note that you can do the same via the UI. You can find a detailed guide for that [here](https://cohere-preview-6021ac31-6091-4dd4-a195-dc3456f6883c.docs.buildwithfern.com/docs/fine-tuning-with-the-cohere-dashboard).

We will finetine our Command R model on the task of conversational financial question answering. Specifically, we finetune our model on [ConvFinQA](https://github.com/czyssrs/ConvFinQA) dataset. In this task, the output expected from the model is a domain specific language (DSL) that we will potentially feed into a downstream application. LLMs are known to be bad at arithmetics. Hence, instead of computing the answer, the task here is to extract the right numbers from the context and applying the right sequence of predicates and to strictly follow the DSL to ensure minimal error rates in the downstream application that may consume the DSL output from our model. Prompt engineering proves to be rather brittle for such tasks as it is hard to make sure the model follows the exact syntax of the DSL. Finetuning the model gives that guarantee.

## Setup

### Dependencies

If you dont already have [Cohere Python SDK](https://github.com/cohere-ai/cohere-python), you can install it as follows.

```python
# ! pip install cohere
```

```python
import os
import cohere
from cohere.finetuning import (
    Hyperparameters,
    Settings,
    WandbConfig,
    FinetunedModel,
    BaseModel,
)

# fill in your Cohere API key here
os.environ["COHERE_API_KEY"] = "<COHERE_API_KEY>"

# instantiate the Cohere client
co = cohere.ClientV2(os.environ["COHERE_API_KEY"])
```

## Dataset

[ConvFinQA](https://github.com/czyssrs/ConvFinQA) dataset is a conversational dataset comprising of multi-turn numerical question and answers based on a given financial report which includes text and tables. We process the original dataset to do a few things:

* We preprocess the financial reports to combine various fields in the original dataset to create a single text blurb from which the questions are to be answered. This involves concatenating various pieces of text, converting the tables to simple text with heuristic regex mappings, among other cosmetic things.
* For finetuning Command R models, the dataset needs to be a `jsonl` file, where each `json` object is a conversation. Each conversation has a list of messages, and each message has two properties: role and content. The role identifies the sender (Chatbot, System, or User), while the content contains the text content. You can find more detailed guide on preparing the dataset including the data validations we have, train/eval splits we recommend, etc. [here](https://docs.cohere.com/docs/chat-preparing-the-data). We format the conversations in the original dataset to conform to these requirements.

### ConvFinQA data example

Following is an example datapoint from the finetuning data.

```python
{
    "messages": [
        {
            "role": "System",
            "content": "stock-based awards under the plan stock options 2013 marathon grants stock options under the 2007 plan and previously granted options under the 2003 plan .\nmarathon 2019s stock options represent the right to purchase shares of common stock at the fair market value of the common stock on the date of grant .\nthrough 2004 , certain stock options were granted under the 2003 plan with a tandem stock appreciation right , which allows the recipient to instead elect to receive cash and/or common stock equal to the excess of the fair market value of shares of common stock , as determined in accordance with the 2003 plan , over the option price of the shares .\nin general , stock options granted under the 2007 plan and the 2003 plan vest ratably over a three-year period and have a maximum term of ten years from the date they are granted .\nstock appreciation rights 2013 prior to 2005 , marathon granted sars under the 2003 plan .\nno stock appreciation rights have been granted under the 2007 plan .\nsimilar to stock options , stock appreciation rights represent the right to receive a payment equal to the excess of the fair market value of shares of common stock on the date the right is exercised over the grant price .\nunder the 2003 plan , certain sars were granted as stock-settled sars and others were granted in tandem with stock options .\nin general , sars granted under the 2003 plan vest ratably over a three-year period and have a maximum term of ten years from the date they are granted .\nstock-based performance awards 2013 prior to 2005 , marathon granted stock-based performance awards under the 2003 plan .\nno stock-based performance awards have been granted under the 2007 plan .\nbeginning in 2005 , marathon discontinued granting stock-based performance awards and instead now grants cash-settled performance units to officers .\nall stock-based performance awards granted under the 2003 plan have either vested or been forfeited .\nas a result , there are no outstanding stock-based performance awards .\nrestricted stock 2013 marathon grants restricted stock and restricted stock units under the 2007 plan and previously granted such awards under the 2003 plan .\nin 2005 , the compensation committee began granting time-based restricted stock to certain u.s.-based officers of marathon and its consolidated subsidiaries as part of their annual long-term incentive package .\nthe restricted stock awards to officers vest three years from the date of grant , contingent on the recipient 2019s continued employment .\nmarathon also grants restricted stock to certain non-officer employees and restricted stock units to certain international employees ( 201crestricted stock awards 201d ) , based on their performance within certain guidelines and for retention purposes .\nthe restricted stock awards to non-officers generally vest in one-third increments over a three-year period , contingent on the recipient 2019s continued employment .\nprior to vesting , all restricted stock recipients have the right to vote such stock and receive dividends thereon .\nthe non-vested shares are not transferable and are held by marathon 2019s transfer agent .\ncommon stock units 2013 marathon maintains an equity compensation program for its non-employee directors under the 2007 plan and previously maintained such a program under the 2003 plan .\nall non-employee directors other than the chairman receive annual grants of common stock units , and they are required to hold those units until they leave the board of directors .\nwhen dividends are paid on marathon common stock , directors receive dividend equivalents in the form of additional common stock units .\nstock-based compensation expense 2013 total employee stock-based compensation expense was $ 80 million , $ 83 million and $ 111 million in 2007 , 2006 and 2005 .\nthe total related income tax benefits were $ 29 million , $ 31 million and $ 39 million .\nin 2007 and 2006 , cash received upon exercise of stock option awards was $ 27 million and $ 50 million .\ntax benefits realized for deductions during 2007 and 2006 that were in excess of the stock-based compensation expense recorded for options exercised and other stock-based awards vested during the period totaled $ 30 million and $ 36 million .\ncash settlements of stock option awards totaled $ 1 million and $ 3 million in 2007 and 2006 .\nstock option awards granted 2013 during 2007 , 2006 and 2005 , marathon granted stock option awards to both officer and non-officer employees .\nthe weighted average grant date fair value of these awards was based on the following black-scholes assumptions: .\nThe weighted average exercise price per share of 2007, 2006, 2005 are $ 60.94, $ 37.84, $ 25.14. The expected annual dividends per share of 2007, 2006, 2005 are $ 0.96, $ 0.80, $ 0.66. The expected life in years of 2007, 2006, 2005 are 5.0, 5.1, 5.5. The expected volatility of 2007, 2006, 2005 are 27% ( 27 % ), 28% ( 28 % ), 28% ( 28 % ). The risk-free interest rate of 2007, 2006, 2005 are 4.1% ( 4.1 % ), 5.0% ( 5.0 % ), 3.8% ( 3.8 % ). The weighted average grant date fair value of stock option awards granted of 2007, 2006, 2005 are $ 17.24, $ 10.19, $ 6.15.\n.",
        },
        {
            "role": "User",
            "content": "what was the weighted average exercise price per share in 2007?",
        },
        {"role": "Chatbot", "content": "60.94"},
        {"role": "User", "content": "and what was it in 2005?"},
        {"role": "Chatbot", "content": "25.14"},
        {
            "role": "User",
            "content": "what was, then, the change over the years?",
        },
        {"role": "Chatbot", "content": "subtract(60.94, 25.14)"},
        {
            "role": "User",
            "content": "what was the weighted average exercise price per share in 2005?",
        },
        {"role": "Chatbot", "content": "25.14"},
        {
            "role": "User",
            "content": "and how much does that change represent in relation to this 2005 weighted average exercise price?",
        },
        {
            "role": "Chatbot",
            "content": "subtract(60.94, 25.14), divide(#0, 25.14)",
        },
    ]
}
```

As you can see, the financial report based on which we answer the questions is put in as System role. This acts as the 'system prompt', which is part of the prompt used as context/instructions for the entire conversation. Since the information in the report is required and relevant to every user question in the conversation, we would want to put it as the overall context of the conversation.

Few things to note in the above example:

* Each datapoint has multiple turns alternating between `User` and `Chatbot`; during finetuning, we consume messages from all roles but only the `Chatbot` messages contribute to the model updates.
* We want the model to learn to strictly follow the domain specific language as represented by the desired Chatbot responses in this example.

### Upload the dataset

We use the [Datasets API](https://docs.cohere.com/reference/create-dataset) to upload the dataset required for finetuning. Note that we upload both training and evaluation files. The data in evaluation file is used for validation and early stopping as we will elaborate later.

```python
chat_dataset = co.datasets.create(
    name="cfqa-ft-dataset",
    data=open("data/convfinqa-train-chat.jsonl", "rb"),
    eval_data=open("data/convfinqa-eval-chat.jsonl", "rb"),
    type="chat-finetune-input",
)
print(
    chat_dataset.id
)  # we will use this id to refer to the dataset when creating a finetuning job
```

Whenever a dataset is created, the data is validated asynchronously. This validation is kicked off automatically on the backend, and must be completed before we can use this dataset for finetuning. You can find more info on interpreting the errors, if you get any, [here](https://docs.cohere.com/docs/datasets#dataset-validation).

```python
co.wait(
    chat_dataset
)  # wait for the dataset to be processed and validated
```

## Start finetuning

Once the dataset is validated, we can start a finetuning job with the [Finetuning API](https://docs.cohere.com/reference/createfinetunedmodel).

### Hyperparameters

There are several hyperparameters that you can modify to get the most out of your finetuning, including LoRA-specific params. You can find detailed explanation [here](https://docs.cohere.com/reference/createfinetunedmodel#request.body.settings.hyperparameters).

```python
hp_config = Hyperparameters(
    train_batch_size=16,
    train_epochs=1,
    learning_rate=0.0001,
)
```

<a id="sec_wandb" />

### WandB integration

For chat finetuning, we support WandB integration which allows you to monitor the loss curves of finetuning jobs in real-time without having to wait for the job to finish. You can find more info [here](https://docs.cohere.com/reference/createfinetunedmodel#request.body.settings.wandb).

```python
wnb_config = WandbConfig(
    project="test-project",
    api_key="<wandb_api_key>",
    entity="test-entity",  # must be a valid enitity associated with the provided API key
)
```

### Create the finetuning job

With the dataset, hyperparameters, and the wandb configurations ready, we can create a fientuning job as follows. You can find the details of all params in the [Finetuning API](https://docs.cohere.com/reference/createfinetunedmodel#request) documentation.

```python
cfqa_finetune = co.finetuning.create_finetuned_model(
    request=FinetunedModel(
        name="cfqa-command-r-ft",
        settings=Settings(
            base_model=BaseModel(
                base_type="BASE_TYPE_CHAT",  # specifies this is a chat finetuning
            ),
            dataset_id=chat_dataset.id,  # the id of the dataset we created above
            hyperparameters=hp_config,
            wandb=wnb_config,
        ),
    ),
)
print(
    cfqa_finetune.finetuned_model.id
)  # we will use this id to refer to the finetuned model when making predictions/getting status/etc.
```

## Check finetuning status

Once the finetuning job finishes and the finetuned model is ready to use, you will get notified via email. Or you can check of the status of your finetuning job as follows.

```python
response = co.finetuning.get_finetuned_model(
    cfqa_finetune.finetuned_model.id
)
print(
    response.finetuned_model.status
)  # when the job finished this will be STATUS_READY
```

You may view the fine-tuning job loss curves via the Weights and Biases dashboard. It will be available via the following URL once the training starts: `https://wandb.ai/<your-entity>/<your-project>/runs/<finetuned-model-id>`. We log the following to WandB:

* training loss at every training step
* validation loss and accuracy (as described [here](https://docs.cohere.com/docs/chat-understanding-the-results)) at every validation step

For this particular fientuning job, the traning loss, validation loss and validation accuracy should look as follows.

Once the training job finished you can also check the validation metrics as follows.

```python
train_step_metrics = co.finetuning.list_training_step_metrics(
    finetuned_model_id=cfqa_finetune.finetuned_model.id
)

for metric in train_step_metrics.step_metrics:
    print(metric.metrics)
```

## Run inference with the finetuned model

Once your model completes training, you can call it via co.chat() and pass your custom model id. Please note, the model id is the id returned by the fine-tuned model object + `-ft` suffix.

```python
response = co.chat(
    model=cfqa_finetune.finetuned_model.id + "-ft",
    messages=[
        {
            "role": "system",
            "content": "in the ordinary course of business , based on our evaluations of certain geologic trends and prospective economics , we have allowed certain lease acreage to expire and may allow additional acreage to expire in the future .\nif production is not established or we take no other action to extend the terms of the leases , licenses or concessions , undeveloped acreage listed in the table below will expire over the next three years .\nwe plan to continue the terms of certain of these licenses and concession areas or retain leases through operational or administrative actions ; however , the majority of the undeveloped acres associated with other africa as listed in the table below pertains to our licenses in ethiopia and kenya , for which we executed agreements in 2015 to sell .\nthe kenya transaction closed in february 2016 and the ethiopia transaction is expected to close in the first quarter of 2016 .\nsee item 8 .\nfinancial statements and supplementary data - note 5 to the consolidated financial statements for additional information about this disposition .\nnet undeveloped acres expiring year ended december 31 .\nThe u.s . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 68, 89, 128. The e.g . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 92, 36. The other africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4352, 854. The total africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4444, 890. The other international of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 2014, 2014. The total of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 257, 4533, 1018.\n.",
        },
        {
            "role": "user",
            "content": "what percentage of undeveloped acres were in the us in 2018?",
        },
        {
            "role": "assistant",
            "content": "divide(128, 1018)",
        },
        {
            "role": "user",
            "content": "what was the total african and us net undeveloped acres expiring in 2016?",
        },
    ],
)
print("#### Model response ####")
print(response.text)
print("########################")
```

```
#### Model response ####
add(189, 68)
########################
```

The response object is described in detail [here](https://docs.cohere.com/reference/chat#response). As you can see, the finetuned model responds in the DSL as expected and matches the ground truth. This DSL response can now be consumed by any downstream application or engine that can compute the final answer. For a comparison we show the base model response to the same inputs.

```python
response = co.chat(
    model="command-r-08-24",
    messages=[
        {
            "role": "system",
            "content": "in the ordinary course of business , based on our evaluations of certain geologic trends and prospective economics , we have allowed certain lease acreage to expire and may allow additional acreage to expire in the future .\nif production is not established or we take no other action to extend the terms of the leases , licenses or concessions , undeveloped acreage listed in the table below will expire over the next three years .\nwe plan to continue the terms of certain of these licenses and concession areas or retain leases through operational or administrative actions ; however , the majority of the undeveloped acres associated with other africa as listed in the table below pertains to our licenses in ethiopia and kenya , for which we executed agreements in 2015 to sell .\nthe kenya transaction closed in february 2016 and the ethiopia transaction is expected to close in the first quarter of 2016 .\nsee item 8 .\nfinancial statements and supplementary data - note 5 to the consolidated financial statements for additional information about this disposition .\nnet undeveloped acres expiring year ended december 31 .\nThe u.s . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 68, 89, 128. The e.g . of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 92, 36. The other africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4352, 854. The total africa of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 189, 4444, 890. The other international of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 2014, 2014, 2014. The total of net undeveloped acres expiring year ended december 31 , 2016, net undeveloped acres expiring year ended december 31 , 2017, net undeveloped acres expiring year ended december 31 , 2018 are 257, 4533, 1018.\n.",
        },
        {
            "role": "user",
            "content": "what percentage of undeveloped acres were in the us in 2018?",
        },
        {
            "role": "assistant",
            "content": "divide(128, 1018)",
        },
        {
            "role": "user",
            "content": "what was the total african and us net undeveloped acres expiring in 2016?",
        },
    ],
)

print("#### Model response ####")
print(base_response.text)
print("########################")
```

```
#### Model response ####
The total African undeveloped acres expiring in 2016 is 189 acres, while the US undeveloped acres expiring in the same year is 68 acres. 

Adding these together gives a total of 257 acres.
########################
```

As you can see, the base model is pretty good in itself. The final answer is correct, in this particular instance (189 + 68 = 257). However, this model response needs further processing to extract the final answer. This post processing can be a noisy process. Also, please note that the LLM's ability for complex numerical reasoning is not very reliable. For these reasons, finetuning it to output DSL is a much more reliable and interpretable way to arrive at the final answer.



---

**Navigation:** [← Previous](./18-employing-a-smaller-context-window-also-has-the-ad.md) | [Index](./index.md) | [Next →](./20-deploy-your-finetuned-model-on-aws-marketplace.md)
