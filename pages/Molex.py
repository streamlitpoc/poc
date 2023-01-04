import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


st.header("Welcome to Molex-")

txt = st.text_area('About us', '''
    Connections matter. They empower today’s innovation leaders to collaborate across 
    industries to solve design and manufacturing challenges. 
    They push boundaries in electronics and connectivity to enable solutions
    that address real customer problems. All to improve lives, every day, 
    around the world.
    From design and development to testing and delivery, we work with our customers 
    to build the technology that’s inside the technology in products that are improving 
    lives all over the world. Customer-first relationships, exceptional engineering 
    expertise and quality that’s second-to-none –that’s how we are Creating Connections 
    for Life.
    ''')

st.balloons()

for i in range(7):
    st.text(" ")


st.caption('The current weather condition in Lisle where the Molex Headquarters is situated-')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

for i in range(7):
    st.text(" ")


st.text("Data Scientists can even display complex mathematical formulae")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


for i in range(7):
    st.text(" ")

st.write("You can display code snippets easily-")
code = '''my_dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
my_dict2 = {'d' : 4, 'e' : 5, 'f' : 6}

# Method 1
result = { **my_dict1, **my_dict2}
print(result)

# Method 2
result = my_dict1.copy()
result.update(my_dict2)
print(result)

# Method 3
result = {key: value for d in (my_dict1, my_dict2) for key, value in d.items()}
print(result)
'''
st.code(code, language='python')

for i in range(7):
    st.text(" ")

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
if st.checkbox('Show dataframe'):
    st.dataframe(df)
st.table(df)

for i in range(7):
    st.text(" ")


st.write("Can display json:")
st.json({
    'Koch': 'Pine',
    'Molex': 'Crystal',
    'floors': [
        'floor 1',
        'floor 2',
        'floor 3',
        'floor 4',
    ],
})


for i in range(7):
    st.text(" ")

st.write("Some type of charts:")

left_column,right_column=st.columns(2)
data=pd.read_csv("C:/Users/nivedj/Downloads/sales_data_sample.csv")

with left_column:
    st.bar_chart(np.random.randn(50, 3))

    st.line_chart(data,x="ORDERDATE",y=["SALES","YEAR_ID"],width=350,height=350) 
    st.bar_chart(data,x="ORDERDATE",y=["SALES","YEAR_ID"],width=350,height=350)  


    import altair as alt

    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)


with right_column:
    st.area_chart(data,x="ORDERDATE",y=["SALES","YEAR_ID"],width=350,height=350)  

    from bokeh.plotting import figure

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')
    p.line(x, y, legend_label='Trend', line_width=2)
    st.bokeh_chart(p, use_container_width=True)


for i in range(7):
    st.text(" ")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'



st.header("THANK YOU !!")