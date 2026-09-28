import streamlit as st

from library_db import BookListCreateRetreiveUpdateDelete
st.title("Delete Book Record")
id=st.text_input("Book ID")
btn=st.button("Delete")
if btn:
    b = BookListCreateRetreiveUpdateDelete()
    record= b.delete(id)
    if record:
        st.success("Deleted Successfully")
    else:
        st.error("no record found")