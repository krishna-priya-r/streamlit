import streamlit as st
from blooddb import Blooddonor
from datetime import date
b=Blooddonor()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETREIVE','UPDATE','DELETE'])
with tab1:
    st.title("Add new Record")
    name = st.text_input("enter Name:")
    blood_group = st.text_input("enter Bloodgroup:")
    phone = st.text_input("Enter phone:", )
    city = st.text_input("enter city:")
    last_donation = st.date_input("Enter last_donation:",min_value=date(1990,1,1),max_value=date.today())
    btn = st.button("Add")
    if btn:
        b.post(name,blood_group,phone,city,last_donation)

with tab2:
    st.title("Read All Records")
    records=b.get()
    st.table(records)


with tab3:
    st.title("Read a Record")
    id=st.number_input("Enter ID:",min_value=0)
    btn=st.button("Submit")
    if btn:
        record=b. retrieve(id)
        st.write(record)

with tab4:
    st.title("Update a Record")
    id = st.number_input("Enter ID:",min_value=0,key="update_id" )
    name = st.text_input("enter Name:",key="update_name")
    blood_group = st.text_input("enter Bloodgroup:",key="update_blood_group")
    phone = st.text_input("Enter phone:",key="update_phone" )
    city = st.text_input("enter city:",key="update_city")
    last_donation = st.date_input("Enter last_donation:", min_value=date(1990, 1, 1), max_value=date.today(),key="update_last_donation")
    btn=st.button("Update")
    if btn:
        record=b.put(id,name,blood_group,phone,city,last_donation)
        if record:
          st.success("Updation Successfull")
        else:
            st.error("no record found")


with tab5:
    st.title("Delete a Record")
    id = st.number_input("Enter ID:", min_value=0, key="delete_id")
    btn=st.button("submit")
    if btn:
     record=b.delete(id)
     if record:
        st.success("Deletion Successfull")
     else:
        st.error("no record found")



