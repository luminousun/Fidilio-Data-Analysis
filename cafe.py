
# --- Import Libraries ---
import pandas as pd
import numpy as np
import plotly.express as px 
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Iran Coffee Shops Report', page_icon=':coffee:' ,layout='wide')

# --- Minimalize Default Features ---
# MainMenu {visibility: hidden; }
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Assets ---
df = pd.read_csv('./cafe.csv', dtype={'phone_number': str}, index_col=0)
df.style.apply(lambda x: ["text-align:right"]*len(x))
lottie__coding1 = load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_CGBC5zgP4g.json')

# --- Header Section ---
with st.container():
    st.sidebar.markdown('### Select Bar')
    st.write(':bar_chart: Quera Data Analysis Bootcamp Project')
    st.title('Iran Coffee Shops Report')

# --- lottie file ---
with st.container():
    left_column, right_colum = st.columns(2)
    with right_colum:
        st_lottie(lottie__coding1, height=200, key='coding')

# --- Analysis and Charts ---
with st.container():
    st.write('---')
    st.subheader('Explore Coffee Shops by City')
    st.sidebar.subheader('[Explore Coffee Shops by City](#explore-coffee-shops-by-city)')
    city1 = list(pd.unique(df['city']))
    city1.insert(0, 'select')
    city_filter = st.sidebar.selectbox('Select the City', city1) # HERE
    df = df[df["city"] == city_filter]
    if city_filter != 'select' :
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric(
        label="Food Quality 🍝",
        value= round(df[df["city"] == city_filter]['food_quality'].mean(),1)
    )
        kpi2.metric(
        label="Service 🍴",
        value= round(df[df["city"] == city_filter]['service'].mean(),1)
    )
        kpi3.metric(
        label="Cost Value 💵",
        value= round(df[df["city"] == city_filter]['cost_value'].mean(),1)
    )
        kpi4.metric(
        label="Environment 🪴",
        value= round(df[df["city"] == city_filter]['environment'].mean(),1)
    )

# --- Scatterplot on maps ---
with st.container():
    s3,s4 = st.columns(2)
    with s3:
        if st.sidebar.checkbox('Show on the Map'):
            st.map(df)
    with s4:
            if st.sidebar.checkbox('Rating by Quality and Cost Heatmap'):
# rating by quality and cost bar chart
                fig = px.density_heatmap(
                data_frame=df, y="food_quality", x="cost"
            )
                st.write(fig)
    s1, s2 = st.columns(2)
# --- Bar Charts --- by Parastoo
    with s1:
        if st.sidebar.checkbox('Cost Bar Chart'):
            # cost bar chart
            st.bar_chart(df, x='cafe_name', y='cost', width=0, height=0, use_container_width=False)
    with s2:
        if st.sidebar.checkbox('Rating by Quality Bar Chart'):
            # rating by quality bar chart
            st.bar_chart(df, x='cafe_name', y='food_quality', width=0, height=0, use_container_width=False)

# --- Time ---
with st.container():
    st.sidebar.subheader('[City Work Time Line Charts](#city-work-time-line-charts)')
    st.write('---')
    st.subheader('City Work Time Line Charts')
    col1, col2 = st.columns(2)
    with col1 :
        if st.sidebar.checkbox('Work Start Line Chart'):
            RWS = df.groupby('work_start').cost_value.mean().reset_index()
            st.line_chart(RWS,
                        x='work_start',
                        y='cost_value',
                        width=0, height=0,
                        use_container_width=False)
    with col2:
        if st.sidebar.checkbox('Work  Line Chart'):
            RWE = df.groupby('work_end').cost_value.mean().reset_index()
            st.line_chart(RWE,
                        x='work_end',
                        y='cost_value',
                        width=0, height=0,
                        use_container_width=False)

# --- Options ---
with st.container():
    st.sidebar.subheader('[Explore City Coffee Shops by Options](#explore-city-coffee-shops-by-options)')
    st.write('---')
    st.subheader('Explore City Coffee Shops by Options')
    options_list =  ['hookah', 'internet', 'delivery', 'smoking', 'open_space', 'live_music', 'parking', 'pos']
    options = st.sidebar.multiselect('Select the Options', options_list)
    if len(options) != 0:
        df[(df[options] == True).all(axis=1)][['cafe_name', 'city', 'province', 'phone_number', 'cost',
        'work_start', 'work_end', 'cafe_address']]
            

# --- Detailed Data View ---
with st.container():
    st.sidebar.subheader('[Detailed Data View](#detailed-data-view)')
    st.write('---')
    st.subheader('Detailed Data View')
    if st.sidebar.checkbox('Show Detailed Data'):
        st.dataframe(df)

# --- Providers ---
with st.container():
    st.sidebar.subheader('Provided by:')
    st.sidebar.subheader('### [Morteza Ahmadi >](https://www.linkedin.com/in/morteza-ahmadi-ab3917220)')
    st.sidebar.subheader('### [Mehra Nouri >](https://www.linkedin.com/in/mehranouri)')
    st.sidebar.subheader('### [Parastoo Tavakoli Basti >](https://www.linkedin.com/in/partbasti)')

# --- INTERFACE DEVELOPMENT ---
for i in range(5):
        st.sidebar.write('\n')
