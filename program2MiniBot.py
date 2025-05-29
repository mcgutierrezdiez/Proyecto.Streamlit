import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("¿En qué te puedo ayudar hoy?")
if prompt==None:
   st.stop()

with st.chat_message("user",avatar = "😊"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.
contexto = '''en este curso de matematicas discretas hay estudiantes de carreras de negociosde primer semestre en universidad 
que necesitan explicaciones detalladas de ejercicios relacionados con negocios

'''
stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Eres un asistente para el curso de matemáticas discretas"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content

with st.chat_message("assistant"):
   st.write(respuesta)
