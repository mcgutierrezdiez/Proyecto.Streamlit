import streamlit as st

st.title("Ejemplo de entrada de texto")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")

# Calendario
import streamlit as st
import datetime

st.title("Ejemplo de fecha")

# Widget: date_input
fecha = st.date_input("Selecciona una fecha para asesoria", value=datetime.date.today())

st.write("La fecha seleccionada es:", fecha)



st.title("Ejemplo de Checkbox")


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
