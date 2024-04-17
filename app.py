from dotenv import load_dotenv
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

load_dotenv()

key=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-pro')

def get_gemini_response(question, prompt):
    response=model.generate_content([prompt[0],question])
    
    return response.text

def read_sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()

    return rows

prompt=[
    """
    You are an expert in converting English to sql query! You have to create SQL query for SQLLITE database running in python.
    The SQL database has a table named STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS etc.
    For Example,
    Example 1 - How many entries of records are present?, the SQL command will be something like this
        SELECT COUNT(*) FROM STUDENT;
    Example 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this
        SELECT * FROM STUDENT WHERE CLASS="Data Science";
    also the response must not contains any unnecessary character at the beginning or end of SQL query. 
    Please make sure to return values NAME, CLASS, SECTION, MARKS where ever possible.
    """
]

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

if submit:
    sql=get_gemini_response(question,prompt)
    print(sql)
    response=read_sql_query(sql,"student.db")
    st.header("The Response is")
    print(response)
    for row in response:
        st.subheader(''.join(str(row)).replace("(", "").replace(")", "").replace("'", "").replace(",",""))