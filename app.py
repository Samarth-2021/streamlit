import streamlit as st
st.header("Streamlit application")
def sapp_logic(num_one, num_two, num_three):
    maximum=num_one
    if maximum < num_two:
        maximum=num_two
    if maximum < num_three:
        maximum=num_three
    
    return maximum

num_one=st.number_input("First number")
num_two=st.number_input("Second number")
num_three=st.number_input("Third number")
largest=app_logic(num_one, num_two, num_three)
st.write(largest)
