import streamlit as st
import pandas as pd
import numpy as np
import pandasql as ps
from PIL import Image

# st.set_page_config(layout="wide")
col1,col2,col3,col4=st.columns(4)
with col1:
    
    st.header("Dashboard")

with col2: 
    st.text_input(label="",placeholder="Search here")

with col3:
    country = st.selectbox(
    'Country',
    ('US', 'India', 'Malaysia'))

with col4:
    options = st.selectbox('User',('Admin','Nivedha'))

for i in range(3):
    st.write(" ")

with st.expander('Check the weather condition'):
    col5,col6,col7=st.columns(3)
    if country=="US":
        st.subheader(country)
        with col5:
            st.metric("Temperature", "70 °F", "1.2 °F")
        with col6:
            st.metric("Wind", "9 mph", "-8%")
        with col7:
            st.metric("Humidity", "86%", "4%")
    elif country=="India":
        st.subheader(country)
        with col5:
            st.metric("Temperature", "10 °F", "12 °F")
        with col6:
            st.metric("Wind", "16 mph", "5%")
        with col7:
            st.metric("Humidity", "8%", "40%")
    else:
        st.subheader(country)
        with col5:
            st.metric("Temperature", "9 °F", "15 °F")
        with col6:
            st.metric("Wind", "100 mph", "-30%")
        with col7:
            st.metric("Humidity", "41%", "3%")

for i in range(3):
    st.write(" ")

st.subheader("Today's Sales")
st.caption("Sales Summary and Product Distribution")
# tab1, tab2 , tab3 ,tab4= st.tabs(["Total Sales", "Total Order", "Product Sold","New Customers"])

# with tab1:
#    st.bar_chart(np.random.randn(50, 3))
col8,col9=st.columns(2)
with col8:
    st.bar_chart(np.random.randn(50, 3))

    data=pd.read_csv("C:/Users/nivedj/Downloads/sales_data_sample.csv")

    st.line_chart(data,x="ORDERDATE",y=["SALES","YEAR_ID"],width=350,height=350) 


with col9:
    import altair as alt
    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)

    
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.map(df)


    




