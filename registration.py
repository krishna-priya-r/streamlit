import streamlit as st
from datetime import date

st.title("Student Registration Form")
Name=st.text_input("Name")
age=st.number_input("Age",min_value=0)
DOB=st.date_input("DOB",min_value=date(1990,1,1),max_value=date.today(),value=date(2000,1,1))
email=st.text_input("Email")
gender=st.radio("Select Gender",['Male','Female'])
courses=st.selectbox("Select courses",['python','java','dotnet','testiny'])
btn=st.button("Register")

if btn:
    st.title("Info")
    st.write("Name:",Name)
    st.write("Age:",age)
    st.write("DOB:", DOB)
    st.write("email:", email)
    st.write("gender:", gender)
    st.write("course:",courses)