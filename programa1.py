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
  
st.title("Ejemplo de Slider")

# Widget: slider
numero = st.slider("Selecciona un número", min_value=0, max_value=100, value=50)

st.write("El número seleccionado es:", numero)

st.title("Ejemplo de Checkbox")

# Widget: checkbox
mostrar = st.checkbox("Mostrar mensaje secreto")

if mostrar:
    st.success("🎉 ¡Este es el mensaje secreto!")

st.title("Ejemplo de entrada de texto")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")

import datetime

st.title("Ejemplo de fecha")

# Widget: date_input
fecha = st.date_input("Selecciona una fecha", value=datetime.date.today())

st.write("La fecha seleccionada es:", fecha)

# Barco navegando
import streamlit as st
st.title("🐋 Ballena animado navegando en Streamlit")
st.markdown("Relájate y observa cómo la ballena se mueve sobre el horizonte...")

barco_html = """
<style>
@keyframes navegar {
  0%   { left: 0%; }
  50%  { left: 85%; transform: scaleX(1); }
  51%  { transform: scaleX(1); } /* voltea el barco */
  100% { left: 0%; }
}

.mar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: linear-gradient(to top, #0077be, #00aaff);
  z-index: 1;
}

.barco {
  position: fixed;
  bottom: 80px;
  left: 0;
  font-size: 48px;
  animation: navegar 50s infinite linear;
  z-index: 2;
  user-select: none;
}
</style>

<div class="mar"></div>
<div class="barco">🐋</div>
"""

st.markdown(barco_html, unsafe_allow_html=True)
if st.button("click"):
    st.balloons()
