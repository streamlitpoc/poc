import streamlit as st
import pandas as pd
import pandasql as ps
import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\maniss7\\Downloads\\Streamlit_poc\\sales_data_sample.csv',encoding="ansi")

col1, col2, col3 = st.columns(3)

with col1:
    expander = st.expander("Today's sales")
    #expander.write("_Sales Summary_")

    df1 = ps.sqldf("select sum(sales) as totalsales , orderdate from df group by orderdate order by orderdate desc limit 1")

    expander.write(" Total Sales : $" + str(int(df1['totalsales'][0])))


with col2:
    expander = st.expander("Today's Orders")
    #expander.write("_Sales Summary_")

    df1 = ps.sqldf("select count(sales) as totalorders from df")

    expander.write(" Total Orders : " + str(int(df1['totalorders'][0])))

    

with col3:
    expander = st.expander("Products Sold")
    #expander.write("_Sales Summary_")

    df1 = ps.sqldf("select count(PRODUCTCODE) as totalproducts  from df group by orderdate order by orderdate desc limit 1")

    expander.write(" Products Sold : " + str(int(df1['totalproducts'][0])))

tab1, tab2, tab3, tab4 = st.tabs(["Sales Mapping by State", "Visitor's Insight", "Top Products", "Total Revenue"])

with tab1:
    df2 = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
    st.map(df2)

with tab2:
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

with tab3:
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.area_chart(chart_data)

with tab4:
    df1 = ps.sqldf("select substring(orderdate,0,9) as orderdate, sum(sales) as totalsales  from df group by orderdate order by orderdate desc limit 3")
    df1.set_index("orderdate", inplace = True)
    #expander.dataframe(df1)

    st.bar_chart(data = df1)




