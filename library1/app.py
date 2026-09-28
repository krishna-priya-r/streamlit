
import streamlit as st
from library_db import BookListCreateRetreiveUpdateDelete

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETREIVE','DELETE','UPDATE'])
b = BookListCreateRetreiveUpdateDelete()

with tab1:
    st.title("ADD")

with tab2:
    st.title('READ')
with tab3:
    st.title('RETRIEVE')
with tab4:
    st.title('DELETE')
with tab5:
    st.title('UPDATE')