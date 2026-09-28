import streamlit as st

st.title("Substraction")

num1=st.number_input("Enter number1:",min_value=0)

num2=st.number_input("Enter number2:",min_value=0)

btn=st.button("Add")

if btn:   #when button clicks it will execute if block
    result=num1- num2
    #print result
    st.write("Difference is",result)  #shows it in interface