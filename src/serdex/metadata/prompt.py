"""Prompts to describe a table content.

https://python.langchain.com/docs/use_cases/qa_structured/sql
"""

from langchain.prompts import PromptTemplate

template_table_describe = """Given a table named {table_name}, that has the following columns:

{column_names}

A sample of the data contained in the table is:

{data_sample}

Provide a description of the table, in a single paragraph.
"""

prompt_table_describe = PromptTemplate(
    input_variables=["table_name", "column_names", "data_sample"],
    template=template_table_describe,
)
