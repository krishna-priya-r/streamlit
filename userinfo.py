import streamlit as st

name=st.text_input("Enter name")
st.write(name)
place=st.radio("select location",['ernakulam','thrissur','trivandrum'])
place=st.selectbox("select location",['ernakulam','thrissur','trivandrum'])
st.write(place)