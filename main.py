import streamlit as st
import snowflake.connector

account = 'df68881.central-india.azure'
user = 'NANDA'
password = 'Nanda1024'
warehouse = 'COMPUTE_WH'
database = 'MYFIRSTDATABASE'
schema = 'APP'

conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM FIRSTTABLE')

results = cursor.fetchall()

st.title(":blue[Explore with Streamlit] :black_heart:")
st.write("This app is a test for you to explore! Please enter your name below to get started.")

name = st.text_input("Enter your name:")

if name:
    key = {}
    submitted = {}
    for each in results:
        q,a,b,c,d,answer = each
        sub = st.radio(q,(a,b,c,d))
        key[q] = answer
        submitted[q] = sub

    end = st.button("Click here to end the test ")
    if end:
        score = 0
        for q, a in key.items():
            if key[q] == submitted[q]:
                score += 1
        st.write(name,'your score is ',score)


