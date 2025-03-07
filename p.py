import streamlit as st

st.title("Welcome Mahnoor website ")
st.header("Fill the your details")
with st.form("user_form"):
    name = st.text_input("Enter you name: ")
    email = st.text_input("Enter your email address: ")
    phone = st.text_input("Enter your phone number: ")
    password = st.text_input("Enter your password: ", type="password")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if name and email and phone and password:
            st.success(f"Thank you, {name}! Your details have been submitted successfully. 🎉")
        else:
            st.error("Please fill in all the details.")
