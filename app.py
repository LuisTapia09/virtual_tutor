import streamlit as st
from tutor import VirtualTutor

# 1 Configuración de la página web (Título e icono de la pestaña)
st.set_page_config(
    page_title="Tutor Virtual de Inteligente",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Tutor Virtual de Inteligencia Artificial")
st.caption("Tu tutor de aprendizaje interactivo basado en Gemini AI")

# 2 Definimos el prompt del sistema que guiará al tutor (Personalidad y comportamiento).
SYSTEM_PROMPT = ("""
Eres un tutor educativo, paciente, estructurado y claro.
Tu objetivo es explicar conceptos complejos de forma simple utilizando ejemplos prácticos, resolviendo las dudas y guiando al usuario en su proceso de aprendizaje.
Mantén un tono amigable y motivador, y asegúrate de que el usuario comprenda los conceptos antes de avanzar.
Al final de cada respuesta, haz una pregunta corta de comprobación para verificar si el alumno comprendió, entendió y aprendió.""")

# 3 Inicialización del tutor en el estado de la sesión (Session State)
if "tutor" not in st.session_state:
    st.session_state.tutor = VirtualTutor(system_prompt=SYSTEM_PROMPT)

# 4 Renderizado del historial de conversación acumulado.
for message in st.session_state.tutor.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5 Entrada del usuario y generación de respuesta.
if prompt := st.chat_input("Escribe tu pregunta o mensaje aquí..."):
    # Mostramos el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtenemos la respuesta del tutor y la mostramos en la interfaz
    with st.chat_message("assistant"):
        with st.spinner("El tutor está pensando..."):
            respuesta = st.session_state.tutor.ask(prompt)
            st.markdown(respuesta)