import datetime
import streamlit as st
import numpy as np
import pandas as pd

st.snow()
st.header("KOCH")
with st.form("Employee Details"):
   st.write("Enter Employee Details:")

   employee_type = st.radio(
    "Employee Type",
    ('Full Time','Consultant','Intern'))

   employee_id = st.text_input("Employee ID")

   name= st.text_input("Name")

   slider_val = st.slider("Rate your work experience")

   options = st.multiselect(
    'What are your favorite shift timings',
    ['12pm-9pm', '1pm-10pm', '8am-4pm', '9am-5pm'],
    ['12pm-9pm', '8am-4pm'])

   option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Office Landline', 'Mobile phone'))

   title = st.text_input("Contact Detail", 'Enter your contact detail')

   d = st.date_input(
    "Enter your Date Of Birth",datetime.date(1990, 1, 1))

   uploaded_files = st.file_uploader("Upload Your documents", accept_multiple_files=True)
   for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read() 
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
   
   color = st.color_picker('Pick A color for your ID card background', '#00f900')
  
   checkbox_val = st.checkbox("High Priority")

   picture = st.camera_input("Take a picture to upload")
   if picture:
    st.image(picture)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Thank You",name,",we are processing your request with employee id-",employee_id,".")
       st.write("We will get back to you shortly!")
       st.success('Success!')
