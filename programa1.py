import streamlit as st

st.title("¡Hola, Streamlit!")
st.write("Tu primer app con Streamlit está corriendo.")

# 02_entrada_texto.py
nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋")

# 03_operaciones_numeros.py
a = st.number_input("Ingresa un número", value=0)
b = st.number_input("Ingresa otro número", value=0)

st.write("Suma:", a + b)
st.write("Producto:", a * b)
  
