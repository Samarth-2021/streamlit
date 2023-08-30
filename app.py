import streamlit as st
st.header("Find the Maximum Number")
def app_logic():
    num_one=st.number_input("First number")
    num_two=st.number_input("Second number")
    num_three=st.number_input("Third number")
    maximum=num_one
    if maximum < num_two:
        maximum=num_two
    if maximum < num_three:
        maximum=num_three
    
    return maximum

largest=None
largest=app_logic()
if largest!=None:
    st.subheader(f"The maximum value is : {largest}")
