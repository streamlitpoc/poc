import streamlit as st
import pandas as pd
import pandasql as ps
import matplotlib.pyplot as plt
import  numpy as np
from PIL import Image

def operation_dashboard(source_data):
    st.markdown(
    """
    <style>
    .reportview-container {
        background: blue
    }
   .sidebar .sidebar-content {
        background: blue
    }
    </style>
    """,
    unsafe_allow_html=True
        )
    df = pd.read_csv(source_data,encoding="utf-8")
    df = ps.sqldf("select * from df where substring(start_date_time,0,8) in ('2022-11','2022-12')")
    option = st.sidebar.selectbox('END DATE TIME',('YEAR', 'MONTH', 'DAY'))
    if option == 'YEAR':
        year_df = ps.sqldf("select distinct substring(start_date_time,0,5) as year from df")
        year_list = year_df['year'].values. tolist()
        year = st.sidebar.selectbox('YEAR',year_list)
    elif option == 'MONTH':
        year_df = ps.sqldf("select distinct substring(start_date_time,0,5) as year from df")
        year_list = year_df['year'].values. tolist()
        year = st.sidebar.selectbox('YEAR',year_list)

        month_df = ps.sqldf("select distinct substring(start_date_time,6,2) as month from df")
        month_list = month_df['month'].values. tolist()
        month = st.sidebar.selectbox('MONTH',month_list)
    else :
        year_df = ps.sqldf("select distinct substring(start_date_time,0,5) as year from df")
        year_list = year_df['year'].values. tolist()
        year = st.sidebar.selectbox('YEAR',year_list)

        month_df = ps.sqldf("select distinct substring(start_date_time,6,2) as month from df")
        month_list = month_df['month'].values. tolist()
        month = st.sidebar.selectbox('MONTH',month_list)

        day_df = ps.sqldf("select distinct substring(start_date_time,9,2) as day from df")
        year_list = day_df['day'].values. tolist()[::-1]
        day = st.sidebar.selectbox('DAY',year_list)
    
#     submit = st.sidebar.button("Submit")
#     if submit == True:    
    image = Image.open('./Logo.jpg')

    st.image(image)
    tab1, tab2= st.tabs(["Job Status", "Ratio of Succeeded/Failed Job"])
    with tab1:
                if option == 'YEAR':
                        job_status_count = ps.sqldf("select job_runner_status, count(*) as cnt from df where substring(start_date_time,0,5) = '"+year+"' group by job_runner_status")
                elif option == 'MONTH':
                        job_status_count = ps.sqldf("select job_runner_status, count(*) as cnt from df where substring(start_date_time,0,5) = '"+year+"' and substring(start_date_time,6,2) = '"+month+"' group by job_runner_status")
                else:
                        job_status_count = ps.sqldf("select job_runner_status, count(*) as cnt from df where substring(start_date_time,0,5) = '"+year+"' and substring(start_date_time,6,2) = '"+month+"' and substring(start_date_time,9,2) = '"+day+"' group by job_runner_status")
                
                job_status_count = ps.sqldf("select case when job_runner_status = 'success' then 'SUCCEEDED' else 'FAILED' end as job_runner_status, cnt from job_status_count ")
                job_status_count['job_status'] = job_status_count['job_runner_status'].str.cat(job_status_count['cnt'].values.astype(str), sep=' : ')
                status = job_status_count['job_status'].values. tolist()
                labels = job_status_count['job_runner_status'].values. tolist()
                count = job_status_count['cnt'].values. tolist() 
                colors = ['#FF0000','#228B22']
                plt_1 = plt.figure(figsize=(2, 4))
                plt.pie(count, colors=colors, labels=status, pctdistance=0.85)
                centre_circle = plt.Circle((0, 0), 0.70, fc='white')
                #plt.title("Job Status")
                plt.legend(labels, bbox_to_anchor=(0,0.3), loc = "upper right") 
                fig1 = plt.gcf()
                fig1.gca().add_artist(centre_circle)
                st.pyplot(fig1)
                st.info("TOTAL JOB RUNS : " + str(sum(count)))
                
    with tab2: 
                if option == 'YEAR':
                        df1 = ps.sqldf("select target_schema_nm, sum(failure) as total_failure, sum(success) as total_success from (select target_schema_nm,start_date_time, case when job_runner_status = 'failure' then 1 else 0 end as failure, case when job_runner_status = 'success' then 1 else 0 end as success from df) x where substring(start_date_time,0,5) = '"+year+"' group by target_schema_nm ")
                elif option == 'MONTH':
                        df1 = ps.sqldf("select target_schema_nm, sum(failure) as total_failure, sum(success) as total_success from (select target_schema_nm,start_date_time, case when job_runner_status = 'failure' then 1 else 0 end as failure, case when job_runner_status = 'success' then 1 else 0 end as success from df) x where substring(start_date_time,0,5) = '"+year+"' and substring(start_date_time,6,2) = '"+month+"' group by target_schema_nm ")
                else:         
                        df1 = ps.sqldf("select target_schema_nm, sum(failure) as total_failure, sum(success) as total_success from (select target_schema_nm,start_date_time, case when job_runner_status = 'failure' then 1 else 0 end as failure, case when job_runner_status = 'success' then 1 else 0 end as success from df) x where substring(start_date_time,0,5) = '"+year+"' and substring(start_date_time,6,2) = '"+month+"' and substring(start_date_time,9,2) = '"+day+"'group by target_schema_nm ")
                df1['totals'] = df1.sum(axis=1)
                df1['failure_percent'] = (df1['total_failure']/df1['totals']).mul(100).round(2)
                df1['success_percent'] = (df1['total_success']/df1['totals']).mul(100).round(2)
                percent_df = df1[['target_schema_nm','failure_percent','success_percent']]
                percent_df.set_index('target_schema_nm',inplace=True)
                ax = percent_df.plot(kind='barh', stacked=True, figsize=(9, 5), color=['red', 'green'], xticks=[])
                ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, frameon=False)
                ax.tick_params(left=False, bottom=False)
                ax.spines[['top', 'bottom', 'left', 'right']].set_visible(False)
                # for c in ax.containers:  
                #     # custom label calculates percent and add an empty string so 0 value bars don't have a number
                #     labels = [f'{w:0.2f}%' if (w := v.get_width()) > 0 else '' for v in c]               
                #     # add annotations
                #     ax.bar_label(c, labels=labels, label_type='center', padding=0.3, color='b')

                fig2 = plt.gcf()
                st.pyplot(fig2)

