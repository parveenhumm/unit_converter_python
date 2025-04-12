import streamlit as st
from convert_unit import convert_unit

st.title("UNIT CONVERTER")

st.markdown("### Converts Length, Weight and Time instantly")

st.write("Welcome! Select category and Enter value and get converted results")
 
category = st.selectbox("choose a category", ["Length", "Weight", "Time"])

if category  == "Length":
    unit = st.selectbox("Select Conversion", ["kilometers to miles", "miles to kilometers"])

elif category  == "Weight":
    unit = st.selectbox("Select Conversion", ["kilograms to pounds", "pounds to kilograms"])

elif category  == "Time":
    unit = st.selectbox("Select Conversion", ["hours to minutes", "minutes to hours", "hours to days", "days to hours"])

value = st.number_input("Enter the value to convert", min_value = 1.0, step = 1.0)

if st.button("convert"):
    result = convert_unit(category, value, unit)
    st.success(f"The result is {result:2f}")
else:
    st.warning("please select valid conversion")