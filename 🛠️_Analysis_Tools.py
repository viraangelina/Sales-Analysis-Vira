import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')  
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
sns.set_style("darkgrid")

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

st.write("# Sales Analysis Tools 📊")
st.markdown(
"""
Welcome to Sales Analysis Tools!

Easily manage, analyze, and visualize your sales, marketing, and product data.
Upload your files, and let us help you tabulate data, uncover key insights, and drive smarter business decisions.

📈 Upload — Analyze — Grow with data!    
"""
)

# File Uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    global df
    global dfReady
    df = pd.read_csv(uploaded_file)
    # st.write(dataframe)
    df['Date'] = pd.to_datetime(df.Date)
    df['Bulan'] = pd.to_datetime(df['Date']).dt.month
    df['Tahun'] = pd.to_datetime(df['Date']).dt.year
    df['Time'] = pd.to_datetime(df['Time'])
    df['Jam'] = df['Time'].dt.hour
    df['Menit'] = df['Time'].dt.minute
    dfReady = True
else:
    st.write("Please Upload File First")
    dfReady = False

# Template Download
with open('./supermarketSales_example.csv') as f:
   st.download_button('Download Template CSV', f, file_name='template_example.csv')

# Multiple Tab Setup
tab1, tab2, tab3, tab4 = st.tabs(["📅 Data", "🤑 Sales", "📣 Marketting", "📦 Product"])

# Data Tab
with tab1:
    tab1.subheader("Data Tabulation")
    if dfReady == True:    
        st.dataframe(df)
    else:
        st.warning("Please Upload File First")

# Sales Tab
with tab2:
    tab2.subheader("Sales Data Visualization")
    if dfReady == True:
        df['Bulan'].value_counts()
        hasil = df.groupby('Bulan').sum(numeric_only=True)
        bulan = [Bulan for Bulan, df in df.groupby('Bulan')]
        fig = plt.figure(figsize=(10,5))
        plt.bar(bulan, hasil['Total'])
        plt.xticks(bulan)
        plt.ylabel('Total dalam USD ($)')
        plt.xlabel('Bulan')
        plt.grid()
        st.pyplot(fig)

        fig = plt.figure(figsize= (15,5))
        sns.countplot(y='Product line', data=df, hue='Payment').set(title='Plot Hitung untuk menunjukan jenis pembayaran pada tiap jenis produk')
        plt.xlabel("Count")
        st.pyplot(fig)

        fig = plt.figure(figsize= (10,5))
        sns.countplot(y='Payment', data=df, hue='City').set(title='Menunjukan metode pembayaran terbanyak diberbagai cabang')
        plt.xlabel("Count")
        st.pyplot(fig)

        Waktu = df.groupby('Jam').sum(numeric_only=True)
        waktu = [Jam for Jam, df in df.groupby('Jam')]
        fig = plt.figure(figsize=(10,5))
        plt.bar(waktu, Waktu['Total'])
        plt.title('Perbandingan Jumlah Transaksi Belanja di Setiap Jam', fontsize=15)
        plt.xticks(waktu)
        plt.ylabel('Total dalam USD ($)', fontsize=12)
        plt.xlabel('Jam', fontsize=12)
        plt.grid()
        st.pyplot(fig)

        fig = plt.figure(figsize=(15,5))
        df['City'].value_counts().plot.pie()
        plt.ylabel('')
        plt.title('Perbandingan Jumlah Pembeli tiap Cabang')
        st.pyplot(fig)

        Kota = df.groupby('City').sum(numeric_only=True)
        kota2 = [City for City, df in df.groupby('City')]
        fig = plt.figure(figsize=(10,5))
        plt.bar(kota2, Kota['gross income'])
        plt.xticks(kota2,rotation = 'vertical')
        plt.title('Perbandingan Pendapatan Bersih di Setiap Cabang', fontsize=15)
        plt.ylabel('Pendapatan Bersih (dalam USD $)', fontsize=12)
        plt.xlabel('Cabang Supermarket', fontsize=12)
        plt.grid()
        st.pyplot(fig)
    else:
        st.warning("Please Upload File First")

# Marketting Tab
with tab3:
    tab3.subheader("Marketting Data Visualization")
    if dfReady == True:

        fig = plt.figure(figsize= (10,5))
        sns.countplot(x='Jam', data=df, hue='City').set(title='Menunjukan jam melakukan transaksi terbanyak di berbagai cabang')
        plt.xlabel("Count")
        st.pyplot(fig)

        fig = plt.figure(figsize=(10,5))
        df['Customer type'].value_counts().plot.pie()
        plt.ylabel("Customer Type")
        st.pyplot(fig)

        fig = plt.figure(figsize= (10,5))
        sns.countplot(x='City', data=df, hue='Customer type').set(title='Menunjukan tipe pembeli di berbagai cabang')
        plt.ylabel("Jumlah Pembeli")
        st.pyplot(fig)

        Membership = df.groupby('Customer type').sum(numeric_only=True)
        membership = [Customer_type for Customer_type, df in df.groupby('Customer type')]
        fig = plt.figure(figsize=(10,5))
        plt.bar(membership, Membership['Total'])
        plt.title('Perbandingan Pendapatan dari Membership', fontsize=15)
        plt.xticks(membership)
        plt.ylabel('Total dalam USD ($)', fontsize=12)
        plt.xlabel('Jenis Pelanggan', fontsize=12)
        plt.grid()
        st.pyplot(fig)
    else:
        st.warning("Please Upload File First")

# Product Tab
with tab4:
    tab4.subheader("Product Data Visualization")
    if dfReady == True:
        Produk = df.groupby('Product line').sum(numeric_only=True)
        produk = [Product_line for Product_line, df in df.groupby('Product line')]
        fig = plt.figure(figsize=(10,5))
        plt.bar(produk, Produk['Quantity'])
        plt.xticks(produk,rotation = 45)
        plt.title('Perbandingan Jumlah Pembelian dari Setiap Jenis Produk', fontsize=15)
        plt.ylabel('Jumlah Pembelian', fontsize=12)
        plt.xlabel('Jenis Produk', fontsize=12)
        plt.grid()
        st.pyplot(fig)

        fig = plt.figure(figsize=(10,5))
        plt.bar(produk, Produk['Total'])
        plt.xticks(produk,rotation = 45)
        plt.title('Perbandingan Transaksi Pembelian dari Berbagai Jenis Produk', fontsize=15)
        plt.ylabel('Transaksi Pembelian (dalam USD $)', fontsize=12)
        plt.xlabel('Jenis Produk', fontsize=12)
        plt.grid()
        st.pyplot(fig)
    else:
        st.warning("Please Upload File First")
