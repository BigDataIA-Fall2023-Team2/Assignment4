import streamlit as st
import pandas as pd
import numpy as np
# from langchain.prompts import PromptTemplate
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_sql_query_chain


from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_sql_query_chain

import requests, pathlib, os
from dotenv import load_dotenv


env_path = pathlib.Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# OPENAI_API_KEY = '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'
# 'snowflake://<user_login_name>:<password>@<account_identifier>/<database_name>/<schema_name>?warehouse=<warehouse_name>&role=<role_name>'

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
user_login_name = os.getenv('user_login_name')
password = os.getenv('password')
account_identifier = os.getenv('account_identifier')
database_name = os.getenv('database_name')
schema_name = os.getenv('schema_name')
warehouse_name = os.getenv('warehouse_name')
role_name = os.getenv('role_name')



db = SQLDatabase.from_uri(f"snowflake://{user_login_name}:{password}@{account_identifier}/{database_name}/{schema_name}?warehouse={warehouse_name}&role={role_name}")


def build_query_chain(dialect, table_info, few_shot_examples, user_question):

    few_shot_examples_str = "\n".join(
        [f"Question: \"{example['question']}\"\nSQLQuery: \"{example['query']}\"\n" for example in few_shot_examples]
    )

    prompt = create_prompt(user_question, few_shot_examples_str, table_info, dialect)

    # Create a SQL query chain
    chain = create_sql_query_chain(ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY), db)
    response = chain.invoke({"question": prompt})
    return response

def create_prompt(input_text, examples_text, table_info, dialect):
    template = """
    Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    Use the following format:

    Question: "{input_text}"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQL Query"
    Answer: "Final answer here"

    Only use the following tables:

    {table_info}.

    Some examples of SQL queries that correspond to questions are:

    {few_shot_examples}
        """
    return template.format(input_text=input_text, few_shot_examples=examples_text, table_info=table_info, dialect=dialect)


dialect = "SQL"
table_info = db.get_table_info()
few_shot_examples = [
    {"question": "Display all rows in app information table", "query": "SELECT * FROM APP_VISIT;"},
    {"question": "Retrieve Apps with Longest Average Usage Duration", "query": "SELECT app_name, AVG(duration_sec) AS avg_duration FROM your_table_name GROUP BY app_name ORDER BY avg_duration DESC;"},
    {"question": "Tell me count of Records for Each App Category", "query": "SELECT app_category, COUNT(*) AS record_count FROM your_table_name GROUP BY app_category;"},
]


st.title("Langchain Query Writer")
user_query = st.text_input("Enter the question you want to ask", key="query_input")
# user_question = "what is the count of records for each app?"

# Build and execute the SQL query chain
response = build_query_chain(dialect, table_info, few_shot_examples, user_query)
print(response)

modified_question = st.text_area("Modify the question", key="modified_question", value=response)

if st.button("Ask"):
    if user_query:
        st.write("Original Question:", user_query)

    if modified_question:
        st.write("Modified Question:", modified_question)

    st.write(db.run(modified_question))
