import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit dan Matplotlib Demo')

# Input pengguna untuk periode fungsi sinus
periode = st.slider('Pilih periode untuk fungsi sinus:', min_value=1.0, max_value=10.0, value=2.0)

# Menghitung nilai x dan y untuk plot
x = np.linspace(0, periode * np.pi, 100)
y = np.sin(x)

# Membuat plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Plot Fungsi Sinus')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

# Menampilkan plot pada aplikasi Streamlit
st.pyplot(fig)
