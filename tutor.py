from google import genai
from google.genai import types
import config

class VirtualTutor:
    def __init__(self, system_prompt: str):
        # 1. Inicializamos el cliente oficial de Gemini
        self.client = genai.Client(api_key=config.GEMINI_API_KEY)
        self.model = config.MODEL_NAME
        
        # 2. Creamos una sesión de chat con la instrucción del sistema (System Prompt)
        self.chat = self.client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7
            )
        )

    def ask(self, user_message: str) -> str:
        try:
            # 3. Enviamos el mensaje al chat. Gemini mantiene el historial automáticamente.
            response = self.chat.send_message(user_message)
            return response.text

        except Exception as e:
            return f"Ocurrió un error al comunicarse con el tutor: {str(e)}"

    @property
    def history(self):
        """
        Propiedad auxiliar para reconstruir el historial en el formato
        que la interfaz gráfica (Streamlit) necesita.
        """
        formatted_history = []
        # Recorremos los mensajes almacenados en la sesión de Gemini
        for message in self.chat.get_history():
            role = "user" if message.role == "user" else "assistant"
            content = message.parts[0].text if message.parts else ""
            formatted_history.append({"role": role, "content": content})
        return formatted_history


# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    PROMPT_SISTEMA = "Eres un tutor de programación paciente y claro. Explica conceptos con analogías simples."
    
    print("Inicializando el tutor con Gemini...")
    tutor_demo = VirtualTutor(system_prompt=PROMPT_SISTEMA)
    
    pregunta = "¡Hola! ¿Me puedes explicar qué es una función en Python usando una analogía?"
    print(f"\nUsuario: {pregunta}\n")
    
    respuesta = tutor_demo.ask(pregunta)
    print(f"Tutor:\n{respuesta}")