import streamlit as st
import snowflake.connector



conn = snowflake.connector.connect(
    account=st.secrets.connections.snowpark.account,
    user=st.secrets.connections.snowpark.user,
    password=st.secrets.connections.snowpark.password,
    database=st.secrets.connections.snowpark.database,
    schema=st.secrets.connections.snowpark.schema,
    warehouse=st.secrets.connections.snowpark.warehouse
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


