import streamlit as st
from library_db import BookListCreateRetreiveUpdateDelete
st.title("Read a Book Record")
id=st.text_input("Book ID")
btn=st.button("Retrieve")
if btn:
    b = BookListCreateRetreiveUpdateDelete()
    record= b.retrieve(id)
    if record:
          st.write("Title:",record[1])
          st.write("Author:", record[2])
          st.write("price:", record[3])
          st.write("pages:", record[4])
          st.write("Language:", record[5])
    else:
        st.error("no record found")