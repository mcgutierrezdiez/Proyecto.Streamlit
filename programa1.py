import streamlit as st

st.title("Ejemplo de entrada de texto")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")

# Calendario
import datetime
st.title("Ejemplo de fecha")
# Widget: date_input
fecha = st.date_input("Selecciona una fecha para asesoria", value=datetime.date.today())
st.write("La fecha seleccionada es:", fecha)

st.title("Ejemplo de Checkbox")
l=True)
if st.button("click"):
    st.balloons()
