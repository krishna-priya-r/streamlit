import streamlit as st

st.title("BMI")
weight=st.number_input("weight in kg",min_value=0)
height=st.number_input("height in cm",min_value=0)
bt=st.button("calculate")

if bt:
    bmi=weight/(height/100)**2
    st.write("bmi is:", bmi)
    if bmi<18.5:
        st.info("underweight")
    elif 18.5<=bmi<25:
        st.success("normal")
    elif 25<=bmi<30:
        st.warning("overweight")
    elif bmi>30:
        st.error("obesity")