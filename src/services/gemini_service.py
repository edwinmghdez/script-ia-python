import os
import google.generativeai as genai
from dotenv import load_dotenv
from yaspin import yaspin

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
  raise ValueError("No se encontró la API KEY en .env")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")  # o gemini-pro, si usas ese

def reply(question: str, context: str = "") -> str:
  """Envía la pregunta a la API de Gemini y devuelve la respuesta"""
  try:
    prompt = f"{context}\n\nPregunta: {question}" if context else question
    with yaspin(text="Generando respuesta...", color="cyan"):
      respuesta = model.generate_content(prompt)
    return respuesta.text.strip()
  except Exception as e:
    return f"❌ Error al generar respuesta: {str(e)}"