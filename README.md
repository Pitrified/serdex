# Self refining data explorer

Create SQL queries to explore your data based on natural language input.

1. Create metadata for the data you want to explore
1. Build a RAG to extract the relevant tables for the question
1. Write a query to answer the question
1. Iterate on the query to fix the errors
1. Ask for relevant KPI related to the question
1. Build those queries and compute the KPIs
1. Present the results with business insights

## Setup

### MySQL

[Install](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
mysql server.

Create the
[`sakila`](https://dev.mysql.com/doc/sakila/en/sakila-installation.html)
database.

Export the password in the environment variable `MYSQL_PASSWORD`.

```bash
export MYSQL_PASSWORD=your_password
```
