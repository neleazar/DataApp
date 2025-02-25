# Create an Interactive Data Analytics Portal with Streamlit in 7 Steps

import pandas as pd 
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title='Data Analytics Dashboard by Eleazar',
    page_icon='📊'
)


st.title('Data Analytics PortalDashboard')
st.subheader(':gray[Explore the data.]',divider='rainbow')

file = st.file_uploader('Drop csv or excel file', type=['csv', 'xlsx'])
if file:
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)
    st.dataframe(data)
    st.info('File is successfully Uploaded', icon='🚨')

st.subheader(':rainbow[Basic information of the dataset]',divider='rainbow')
tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

with tab1:
    st.write(f'There are {data.shape[0]} rows in dataset and  {data.shape[1]} columns in the dataset')
    st.subheader(':gray[Statistical summary of the dataset]')
    st.dataframe(data.describe())
with tab2:
    st.subheader(':gray[Top Rows]')
    toprows = st.slider('Number of rows you want', 1, data.shape[0], key='topslider')
    st.dataframe(data.head(toprows))
    st.subheader(':gray[Bottom Rows]')
    bottomrows = st.slider('Number of rows you want', 1, data.shape[0], key='bottomslider')
    st.dataframe(data.tail(bottomrows))
with tab3:
    st.subheader(':grey[Data types of column]')
    st.dataframe(data.dtypes)
with tab4:
    st.subheader('Column Names in Dataset')
    st.write(list(data.columns))