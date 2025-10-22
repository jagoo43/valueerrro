try:
  num = int(input("enter a number"))
  print(num)

except ValueError:
  print("exception ",ValueError)

  print("i am outside the try block")
