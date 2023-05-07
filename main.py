import streamlit as st
import snowflake.connector

account = 'df68881.central-india.azure'
user = 'NANDA'
password = 'Nanda1024'
warehouse = 'COMPUTE_WH'
database = 'MYFIRSTDATABASE'
schema = 'PUBLIC'

conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

cursor = conn.cursor()

cursor.execute('SELECT * FROM MCQ_QUESTIONS')

results = cursor.fetchall()



st.title(":blue[Explore with Streamlit] :black_heart:")
st.write("This app is a test for you to explore! Please enter your name below to get started.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! ")
    "Your test has started...! Mark the Correct Answers :sunglasses:"

    score = 1
    question1 = st.radio("1.What is the spelling of number 3 ?", ('Three', 'one', 'twenty', 'Two'))
    question2 = st.radio("2.What is the special occasion on 26th Jan ?",
                         ('None of the above', 'Republic day', "Gandhi's Birthday", 'Independance day'))
    question3 = st.radio("3.Who is the prime minister of india ?",
                         ('Narendra modi', 'Rakesh jujunwala', 'Nirav modi', 'Satwik nadella'))
    question4 = st.radio("4.What is the capital of Telangana ?", ('Hyderabad ', 'Mumbai', 'Bombay', 'Delhi'))
    if question1 == 'Three':
        score += 1
    if question2 == 'Republic day':
        score += 1
    if question3 == 'Narendra modi':
        score += 1
    if question4 == 'Hyderabad':
        score += 1
    end = st.button("Click here to end the test ")
    if end :
        st.write(name,'your score is ',score)

