import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

pwd = os.getcwd()

def byhour(df):
    hour_rent = df.groupby(by='hour')['count'].mean()
    return hour_rent

def bymonth(df):
    month_rent = df.groupby(by='month')['count'].mean()  # Memperbarui pengelompokkan berdasarkan 'month'
    return month_rent

def byseason(df):
    season_rent = df[df['year'] == 2012].groupby(by='season')['count'].mean()
    return season_rent

# Import dataframe
day_data = pd.read_csv("day_data.csv")
hour_data = pd.read_csv("hour_data.csv")

# Menyiapkan dataframe yang dikelompokkan
byhour = byhour(hour_data)
bymonth = bymonth(day_data)  # Menggunakan fungsi bymonth yang diperbarui
byseason = byseason(day_data)

st.header('Bike Sharing Dashboard')
st.markdown("""
<div style="text-align: justify">
  Pada Dashboard ini, kami menampilkan visualisasi data yang menunjukkan perkembangan rental sepeda tahun 2011-2012. Kami menampilkan rush hour rental sepeda agar dapat mengetahui jam-jam sepi dan  menampilkan musim terbaik untuk menikmati rental sepeda.
</div>
""", unsafe_allow_html=True)

st.markdown("\n")

st.subheader('Rush Hour Pengguna Rental Sepeda')
# Plotting Rata-rata Pengguna Rental Sepeda Tiap Jam

fig, ax = plt.subplots(figsize=(10, 7))  # Perbaiki ukuran figsize

sns.barplot(x='hour', y='count', data=hour_data, hue='year', ax=ax)

plt.xlabel("Hour")
plt.ylabel("Jumlah Rental Sepeda")
plt.title("Rush Hour Rental Sepeda")

ax.set_title("Berdasarkan Jam Perhari", loc="center", fontsize=30)
ax.set_ylabel("Jumlah Rental Sepeda")
ax.set_xlabel("Hour")
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

st.markdown("\n")

st.subheader('Musim Terbaik untuk bersepeda')
# Plotting Rental Sepeda Tiap Musim

fig, ax = plt.subplots(figsize=(7, 7))  # Perbaiki ukuran figsize
season = ('fall', 'summer', 'winter', 'spring')
values = [641479, 571273, 515476, 321348]
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.1, 0, 0, 0)

ax.pie(values, labels=season, autopct='%1.1f%%', colors=colors, explode=explode)
st.pyplot(fig)

st.markdown("\n")

st.subheader('Kenaikan Rental Sepeda tahun 2011-2012')
# Plotting Kenaikan Rental Sepeda tahun 2011-2012

fig, ax = plt.subplots(figsize=(7, 7))  # Perbaiki ukuran figsize

sns.barplot(x='month', y='count', data=day_data, hue='year', ax=ax)

plt.xlabel("Bulan")
plt.ylabel("Jumlah Rental Sepeda")
plt.title("Kenaikan Rental Sepeda pada 2011 - 2012")

ax.set_title("Berdasarkan Bulan Perhari", loc="center", fontsize=30)
ax.set_ylabel("Jumlah Rental Sepeda")
ax.set_xlabel("Bulan")
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

st.markdown("\n")

st.caption('Copyright (c) Khairunnisa Syahirah Naifah 2023')
