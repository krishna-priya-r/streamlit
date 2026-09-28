import streamlit as st

name=st.text_input("Enter name")
age=st.text_input("Enter age")
place=st.text_input("Enter place")
gender=st.radio("select Gender",['male','female'])
qualif=st.selectbox("Select qualification",['bca','bba','btech'])

bt=st.button("submit")

if bt:
    st.title("User Info")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Place:",place)
    st.write("Gender:",gender)
    st.write("Qualification:",qualif)
