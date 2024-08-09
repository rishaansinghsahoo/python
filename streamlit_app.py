import streamlit as st
import numpy as np

if st.button("Refresh"):
  st.cache_resource.clear()
  st.rerun()

st.title("This is a maths Sats test")
st.write("sum of these numbers")
n1=np.random.randint(low=550,high=10000)
n2=np.random.randint(low=450,high=1000)
s=n1+n2

if 'answer' not in st.session_state:
  # st.write("inside session creation:")
  st.session_state.answer = s
  # st.write("session answer:",s)


st.write("First number is " , n1)
st.write("Second number is " , n2)
# st.write("The first sum is" , s)       
a=st.number_input(" Enter your answer",step=1)


if st.button("check your answer"):
  ans = st.session_state.answer
  st.write("Actual Answer: ", ans)
  st.write("Your Answer: ", a)
  if a==ans:
    st.write( " YAY YOU ARE CORRRRRRRREEEEEECCCCCCTTTTTTTTTTTTTTTTTT")
  else:
    st.write(" YOU GET A RED CAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")
  st.session_state.answer = s
                 

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









































