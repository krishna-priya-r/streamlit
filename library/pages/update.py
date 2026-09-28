import streamlit as st
from library_db import BookListCreateRetreiveUpdateDelete
st.title("Update Book Record")
id=st.text_input("Book ID")
title = st.text_input("enter Title:")
author = st.text_input("enter author name:")
price = st.number_input("Enter price:",min_value=0)
pages = st.number_input("enter pages:",min_value=0)
language = st.text_input("Enter language:")
btn=st.button("Add")
if btn:
    b=BookListCreateRetreiveUpdateDelete()
    record= b.update(id,title,author,price,pages,language)
    if record:
        st.succes("succesfully updated")
    else:
        st.error("No record found")