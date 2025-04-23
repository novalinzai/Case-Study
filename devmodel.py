import streamlit as st
import joblib
import numpy as np

# Memuat model regresi linear yang sudah disimpan
lin_reg_loaded = joblib.load('lin_reg_model_new.joblib')

#Judul aplikasi
st.title("Prediksi Gaji Berdasarkan Masa Dinas")

#Input Masa Dinas
years_experience = st.number_input("Masukkan Masa Dinas:", min_value=0.0, step=0.1)

#Prediksi gaji
if st.button("Prediksi Gaji"):
   gaji = lin_reg_loaded.predict([[Years_of_Experience]])
   st.write(f"Gaji seseorang setelah bekerja selama {Years_of_Experience} tahun adalah ${salary[0]:,.2f}")