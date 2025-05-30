import streamlit as st
from openai import OpenAI

# Configurar la interfaz
st.set_page_config(page_title="Asistente Discretas", page_icon="📚")
st.title("📚 Asistente de Matemáticas Discretas")
st.markdown("Bienvenido al chatbot para el curso de **Matemáticas Discretas**.\n\n"
            "👩‍🏫 Este asistente está diseñado para estudiantes de **negocios de primer semestre**.\n"
            "Puedes hacer preguntas como:\n"
            "- ¿Cómo aplico conjuntos en ejemplos de marketing?\n"
            "- ¿Qué es un grafo y cómo lo uso en logística?\n"
            "- ¿Qué ejercicios puedo hacer para entender relaciones binarias?\n")

# Obtener la API key
openai_api_key = st.secrets["api_key"] 
client = OpenAI(api_key=openai_api_key)

# Input del usuario
prompt = st.chat_input("Escribe tu pregunta sobre matemáticas discretas:")

if not prompt:
    st.stop()

# Mostrar mensaje del usuario
with st.chat_message("user", avatar="😊"):
    st.markdown(prompt)

# Definir contexto específico para el curso
contexto = """
Actúa como un profesor de matemáticas discretas que enseña a estudiantes de primer semestre de carreras de negocios.
Tus respuestas deben ser claras, con ejemplos aplicados al mundo empresarial o económico.
Evita tecnicismos innecesarios y ofrece analogías cuando sea posible. Utiliza un tono amigable y motivador.
"""

# Solicitar respuesta al modelo
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": contexto},
        {"role": "user", "content": prompt}
    ],
    max_tokens=800,
    temperature=0.1,
)

respuesta = response.choices[0].message.content

# Mostrar respuesta del asistente
with st.chat_message("assistant", avatar="🧠"):
    st.write(respuesta)
st.balloons
