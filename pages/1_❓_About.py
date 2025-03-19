import streamlit as st
import base64

st.set_page_config(page_title="Sales Analysis Tools", page_icon="📊")
st.sidebar.header("📊 Sales Analysis Tools", divider=True)
st.sidebar.markdown(
"""
Sales Analysis Tools is an intuitive web platform designed to help businesses effortlessly upload, process, and visualize their sales, marketing, and product data. With a clean interface and powerful analysis features, this tool enables users to transform raw data into actionable insights, supporting data-driven decision-making and business growth.
"""
)
st.sidebar.subheader("Key Features:", divider=True)
st.sidebar.markdown(
"""
1. File Upload & Auto Processing
2. Data Tabulation
3. Interactive Sales & Marketing Dashboards
4. Multi-Category Analysis
"""
)

st.write("# About 🧐")

_left, mid, _right = st.columns(3)
with mid:
    st.image("https://media.tenor.com/IF2JdxzmyN4AAAAj/coding-girl.gif")

st.markdown(
"""
This website was created by Vira Angelina, a Business Statistics student at Institut Teknologi Sepuluh Nopember (ITS), class of 2022.

The Sales Analysis Tools platform is part of her academic project and personal portfolio, designed to showcase practical applications of data analysis in the business world. Built with a focus on simplicity and functionality, this tool helps users easily upload, process, and analyze sales, marketing, and product data.

Through this project, Vira aims to demonstrate her passion for data analytics, business intelligence, and the development of digital solutions that turn raw data into valuable business insights.    
"""
)

st.subheader("How to reach me?", divider=True)
_col1, _col2, _col3, _col4, _col5, _col6, _col7, _col8, _col9, _col10 = st.columns(10)
_col1.markdown(
    """<a href="https://www.linkedin.com/in/vira-angelina/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(base64.b64encode(open("./icon/linkedin.png", "rb").read()).decode()),
    unsafe_allow_html=True,)
_col2.markdown(
    """<a href="https://www.linkedin.com/in/vira-angelina/">
    <img src="data:image/png;base64,{}" width="25">
    </a>""".format(base64.b64encode(open("./icon/github.png", "rb").read()).decode()),
    unsafe_allow_html=True,)
