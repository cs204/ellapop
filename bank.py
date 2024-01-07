greetings = input("Приветствие: ")

if greetings.startswith("здравствуйте"):
  print("$0")
elif greetings.startswith("з"):
  print("$20")
else:
  print("$100")