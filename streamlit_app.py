import streamlit as st
import numpy as np

if st.button("Refresh"):
  st.rerun()

st.title("This is a maths Sats test")
n1=np.random.randint(low=0,high=9)
n2=np.random.randint(low=0,high=9)
s=n1*n2
st.write("First number is " , n1)
st.write("Second numberis " , n2)
st.write("The first sum is" , s)       


st.divider()



st.title("Rishaan first app ")
st.write("This is my first app, I will make a calculator")
st.write (" 10*100000")
st.write( 10*100000)

number1=st.number_input("Insert number 1",step=1)
number2=st.number_input("Insert number 2",step=1)
st.write("the sum is ")
st.write(number1+number2)
st.write("the product is ")
st.write(number1*number2)
st.write("the difference")
st.write(number1-number2)
st.write(number1-number2)









































