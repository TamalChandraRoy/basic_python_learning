number = int(input("Enter factorial Number "))
factorial = 1

while (number > 0):
  factorial *= number
  number -= 1

print("Factorial value of number is: ", factorial)