import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot")

openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("¿Hola, en que te puedo ayudar hoy?")
if prompt==None:
   st.stop 

with st.chat_message("user", avatar="😊"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.
contexto = "en el curso de matematicas discretas son estudiantes de carreras de negocios "
promptfinal = contexto + prompt
stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Eres un asistente para un curso de matematicas discretas de primer semestre de universidad"},
            {"role": "user", "content": promptfin}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content

with st.chat_message("assistant"):
   st.write(respuesta)
