import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open("C:/Users/nivedj/Downloads/exapmle.jpg")
image2 = Image.open("C:/Users/nivedj/Downloads/example2.jpg")

st.title('Demo  Dashboard')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)


col1, col2= st.columns(2)
with col1:
   st.header("KOCH")
   st.image(image, caption='Koch logo')

with col2:
   st.header("MOLEX")
   st.image(image2, caption='Molex logo')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Revenue')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)