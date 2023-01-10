import streamlit as st
import pandas as pd
import pandasql as ps
import pandas as pd
import numpy as np
# data visualization
import pandas as pd
import pandasql as ps
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fast')


def form_callback(df,country_selected,year_selected):

    st.header("Dashboard")

    sales_query = "select sum(sales) as totalsales from df where country = '"+country_selected+"' and year_id ='"+str(year_selected)+"'"

    count_sales_query = "select count(sales) as totalorders from df where country = '"+country_selected+"' and year_id ='"+str(year_selected)+"'"

    product_query = "select count(distinct PRODUCTCODE) as totalproducts  from df where country = '"+country_selected+"' and year_id ='"+str(year_selected)+"'"

    col1, col2, col3 = st.columns(3)
    
    with col1:
            expander = st.expander("Total Sales :",expanded=True)
            df1 = ps.sqldf(sales_query)
            expander.write("$" + str(int(df1['totalsales'][0])))


    with col2:
            expander = st.expander("Total Orders",expanded=True)
            df1 = ps.sqldf(count_sales_query)
            expander.write("" + str(int(df1['totalorders'][0])))

            

    with col3:
            expander = st.expander("Products Category Sold",expanded=True)
            df1 = ps.sqldf(product_query)
            expander.write("" + str(int(df1['totalproducts'][0])))

    tab1,tab2= st.tabs(["Sales by State",'Distribution by Deal size'])

    with tab1:
        if country_selected in ('France','Spain'):
            st.info("State Level Information Not available")
        else:
        
            state_df = ps.sqldf("select case when state is null then 'NA' else state end as STATE, sum(sales) as total_sales from df where country = '"+country_selected+"'and year_id ='"+str(year_selected)+"' group by state")
            fig3, ax = plt.subplots()  
            state = state_df.STATE.to_list()
            sales = state_df.total_sales.to_list()
            plt.rcParams['figure.figsize'] = (10, 5)
            ax = sns.barplot(x = state, y = sales)
            ax.set_xlabel(xlabel = 'state', fontsize = 10)
            ax.set_ylabel(ylabel = 'total sales', fontsize = 10)
            plt.xticks(rotation = 90)
            fig3 = plt.gcf()
            st.pyplot(fig3)
    with tab2 :
        deal_df = ps.sqldf("select dealsize, count(*) as count from df where country = '"+country_selected+"'and year_id ='"+str(year_selected)+"' group by dealsize")
        fig4, ax = plt.subplots()  
        deal = deal_df.DEALSIZE.to_list()
        count = deal_df['count'].to_list()
        plt.pie(count, labels = deal,autopct='%1.1f%%')
        fig4 = plt.gcf()
        st.pyplot(fig4)
    


def sales(source_data):
    df = pd.read_csv(source_data,encoding="unicode_escape")
    df1 = ps.sqldf("select country, count(*) as order_count from df group by country order by count(*) desc limit 5")
    country = tuple(df1.COUNTRY.to_list())
    country_selected = st.sidebar.radio('Select a country',country, key = "my_radiobox")
    df1 = ps.sqldf("select distinct year_id from df")
    year = tuple(df1.YEAR_ID.to_list())
    year_selected = st.sidebar.selectbox('Select a year',year, key = "my_selectbox")
    form_callback(df,country_selected,year_selected)
    #generate = st.sidebar.button('',on_click=form_callback(df,country_selected,year_selected))
