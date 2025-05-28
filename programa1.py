import streamlit as st

st.title("Ejemplo de entrada de texto")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")
    
# Seleccion multiple
options = st.multiselect(
    "Cuales son tus dudas de hoy?",
    ["Proposiciones logicas", "Conjuntos", "Grafos"],
    default=["Proposiciones logicas"],
)

st.write("Seleccionaste:", options)
