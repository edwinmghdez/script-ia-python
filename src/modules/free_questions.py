from services.gemini_service import reply

def free_questions():
  print("🟣 Modo libre (Escribe 'salir' para terminar la ejecución del programa) 🟣")
  while True:
    entry = input("🤖 Pregunta: ").strip()
    if entry.lower() == "salir":
      print("👋 Adiós.")
      break
    if entry == "":
      continue
    response = reply(entry)
    print("🧠 Respuesta:", response)
    print("-" * 50)