import streamlit as st

st.title("Rishaan first app ")
st.write(
    "This is my first app, I will make a calculator"
    
)

st.write (" 10*100000")
st.write( 10*100000)

number1=st.number_input("Insert number 1")
number2=st.number_input("Insert number 2")
st.write(number1*number2)
