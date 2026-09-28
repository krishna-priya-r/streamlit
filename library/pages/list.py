import streamlit as st
from library_db import BookListCreateRetreiveUpdateDelete
st.title("Read all Book Record")

b = BookListCreateRetreiveUpdateDelete()
records=b.list()
st.table(records)

