import streamlit as st
import operation as op
import sales as sa

def main():
    st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 50;
            }}
        </style>
    ''',
    unsafe_allow_html=True
    )
    original_title = '<p style="font-family:Courier; color:Black; font-size: 20px;">Welcome to <strong>STREAMLIT</strong> Demo !!!</p>'
    st.sidebar.markdown (original_title, unsafe_allow_html=True)

    option = st.sidebar.selectbox(
    'Please select a Dashboard',
    ('Operations & Monitoring', 'Sales'))

    if option == 'Operations & Monitoring':
        source_path = 'C:\\Users\\maniss7\\Downloads\\Streamlit_poc\\Demo\\data\\operation_data.csv'
        op.operation_dashboard(source_path)
        # content = '<p style="font-family:Courier; color:Black; font-size: 20px;">This dashboard gives you insights for job monitoring in <strong>PRODUCTION</strong> enviroment. Support Engineer can you this dashboard for jobs monitoring, raising defects and fixing bugs.</p>'
        # st.sidebar.markdown (content, unsafe_allow_html=True)
    else:
        source_path = 'C:\\Users\\maniss7\\Downloads\\Streamlit_poc\\sales_data_sample.csv'
        content = '<p style="font-family:Courier; color:Black; font-size: 20px;">This dashboard gives you insights for <strong>Sales</strong>.User can find different insights related to daily sales, visitor traffic, total revenue and lot more ..</p>'
        st.sidebar.markdown (content, unsafe_allow_html=True)
        sa.sales(source_path)

        
if __name__ == '__main__':
    main()