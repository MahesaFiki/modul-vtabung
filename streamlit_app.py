import streamlit as st
import math 

st.title(" Menghitung Volume Tabung :rainbow[Let's Go!] :rocket:")
r = st.number_input("Masukkan Jari-Jari :",0)
t = st.number_input("Masukkan Tinggi :",0)
if st.button("volume",type="primary"):
  v = math.pi*(r**2)*t
  st.success(f"Volume Tabung Adalah {v:.2f}") 
