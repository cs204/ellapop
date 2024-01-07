while True:
  try:
    fraction = input("Дробь: ").split("/")
    fuel = round((int(fraction[0]) / int(fraction[1])) * 100)

    if fuel > 100:
      continue

    if fuel <= 1:
      print("E")
    elif fuel >= 99:
      print("F")
    else:
      print("%d%%" % fuel)

    break
  except (ValueError, ZeroDivisionError, IndexError):
    pass