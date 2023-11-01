def write_sql(table_sample: str, query: str) -> str:
    prompt = f"""You are an expert en SQL. 
Your task is to write SQL commands given a textual description of the request
and a sample of the table (including headers).
These is how the table(s) look like, delimited by triple backticks:
```
{table_sample}
```
Write a query that performs the following: {query}.
"""
    return prompt

_title = "Write SQL queries"
_description = "Provide a description of the request you need and the relevant table_headers. GPT will write the query"