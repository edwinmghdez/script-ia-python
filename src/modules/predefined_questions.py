from services.gemini_service import reply

def load_context(path="./src/config/context.txt") -> str:
  with open(path, "r", encoding="utf-8") as f:
    return f.read().strip()

def load_questions(path="./src/config/questions.txt") -> list:
  with open(path, "r", encoding="utf-8") as f:
    return [line.strip() for line in f if line.strip()]

def predefined_questions():
  context = load_context()
  questions = load_questions()

  print("🟣 Modo predefinido 🟣")
  print("\n📌 Opciones disponibles:")
  print("0. Salir")
  for idx, question in enumerate(questions, start=1):
    print(f"{idx}. {question}")

  while True:
    option = input("Selecciona una opción: ").strip()
    if option == "0":
      print("👋 Adiós.")
      break
    if not option.isdigit() or int(option) not in range(1, len(questions) + 1):
      print("❌ Opción inválida.")
      continue

    question = questions[int(option) - 1]
    response = reply(question, context=context)
    print(f"🤖 {question}")
    print("🧠 Respuesta:", response)
    print("-" * 50)