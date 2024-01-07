menu = {
  "кофе": 20.00,
  "чай": 10.00,
  "булочка": 5.00,
  "салат": 30.40,
  "пирожное": 45.50
}

sum_ = 0.0

while True:
  try:
    dish = input("Блюдо: ")

    if dish in menu.keys():
      sum_ += menu[dish]
  except EOFError:
    print("\nСумма: %.2f" % sum_)
    break