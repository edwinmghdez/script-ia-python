from modules.free_questions import free_questions
from modules.predefined_questions import predefined_questions

def main():
  print("Bienvenido al Asistente de IA")
  print("1. Modo libre (Haz las preguntas que quieras)")
  print("2. Modo predefinido (Selecciona preguntas previamente definidas)")
  print("3. Salir")
  option = input("Selecciona una opción: ").strip()

  if option == "1":
    free_questions()
  elif option == "2":
    predefined_questions()
  else:
    print("👋 Adiós.")

if __name__ == "__main__":
  main()
