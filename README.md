# Proyecto: Tutor Virtual Inteligente 🎓

Este proyecto es un **Tutor Virtual Inteligente** interactivo desarrollado con Python y Streamlit. Permite a los alumnos interactuar con un asistente conversacional que mantiene el contexto de la sesión, explica conceptos de manera didáctica y realiza preguntas de comprobación.

---

## 📌 Contexto del Proyecto

Este desarrollo nació como un **proyecto académico de LLMs (Large Language Models)**. Inicialmente se contempló el uso de la API de OpenAI, pero con el fin de optimizar costos y aprovechar las capacidades de acceso gratuito para desarrollo, se migró la arquitectura a la **API de Google Gemini** (`google-genai`).

### 🎯 Objetivos de Aprendizaje
1. Comprender el rol de los Modelos de Lenguaje de Gran Escala (LLM) en la IA moderna.
2. Interactuar con APIs de modelos generativos y gestionar la autenticación mediante variables de entorno.
3. Desarrollar habilidades prácticas en el diseño e implementación de aplicaciones modulares basadas en LLMs.
4. Aplicar técnicas de procesamiento de lenguaje natural (NLP) y *Prompt Engineering* en un entorno real.

---

## 📐 Estructura del Proyecto

```text
tutor-virtual/
│
├── .env.example          # Plantilla de variables de entorno (sin claves reales)
├── .gitignore            # Archivos excluidos de Git
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Instrucciones de instalación y ejecución
│
├── config.py             # Carga y validación de variables de entorno
├── tutor.py              # Clase principal del motor del Tutor (Lógica del LLM)
└── app.py                # Interfaz de usuario interactiva (Streamlit)

