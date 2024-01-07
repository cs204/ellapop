from re import search
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

while True:
  try:
    old_date = input("Дата: ")

    if search(r"\d{1,2}\W\d{1,2}\W\d{4}", old_date):
      day, month, year = search(r"(\d{1,2})\W(\d{1,2})\W(\d{4})", old_date).groups()

      day = int(day)
      month = int(month)
      year = int(year)

      if day > 31 or month > 12:
        continue

      print("%04d-%02d-%02d" % (year, month, day))
      break
    elif search(r"\d{1,2}\W\w+\W\d{4}", old_date):
      day, month, year = search(r"(\d{1,2})\W(\w+)\W(\d{4})", old_date).groups()

      if month in months:
        month = str(months.index(month) + 1)
      else:
        continue

      day = int(day)
      month = int(month)
      year = int(year)

      if day > 31 or month > 12:
        continue

      print("%04d-%02d-%02d" % (year, month, day))
      break
  except ValueError:
    pass