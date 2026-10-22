import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env a os.environ
load_dotenv(override=True)

# Recuperamos las variables de entorno necesarias para la aplicación
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.8-flash")

# Validación preventiva de la clave API
if not GEMINI_API_KEY:
    raise ValueError(
        "ERROR CRÍTICO: No se encontró la variable GEMINI_API_KEY en el archivo .env"
    )