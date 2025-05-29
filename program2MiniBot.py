# mini bot
import streamlit as st

#st.set_page_config(page_title="Ejemplo Chat", layout="centered")

st.title("💬 Mini Chatbot (propuesta ejercicios proposiciones logicas)")

# Entrada tipo chat (abajo de la pantalla)
user_input = st.chat_input("Sugerencias de ejercicios de proposiciones logicas")

# Si el usuario escribe algo, mostramos los mensajes
if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user").write(user_input)

    # Mostrar una respuesta simple del asistente
    st.chat_message("assistant").write(f"{user_input} <- eso dijiste")
    st.write("¡Buen día! Claro, aquí van unos ejercicios para que te diviertas un rato: \n\n1. Demuestra que \\( p \\land (q \\lor r) \\) es equivalente a \\( (p \\land q) \\lor (p \\land r) \\).\n2. Crea una tabla de verdad para la proposición \\( (p \\rightarrow q) \\land (\\neg q \\rightarrow \\neg p) \\).\n3. Encuentra el valor de verdad de la proposición \\( p \\lor (q \\land \\neg p) \\) cuando \\( p \\) es verdadero y \\( q \\) es falso.\n\n¡Diviértete!")
    
