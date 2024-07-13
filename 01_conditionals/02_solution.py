age = int(input("Give me your age"))
day = "sunday"

price = 12 if age >= 18 else 8

if day == "wednesday":
  price -= 2

print("Tickets price for you is $", price)