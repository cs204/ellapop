def main():
  A = input()
  B = convert(A)
  print(B)

def convert(A):
  A = A.replace(":)", '🙂').replace(":(", '🙁')
  return A

main()