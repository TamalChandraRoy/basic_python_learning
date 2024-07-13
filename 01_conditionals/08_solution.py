password = str(input("Enter your password"))
passLen = len(password)

if passLen < 8:
  strength = "Week"
elif passLen < 10:
  strength = "Medium"
else:
  strength = "Strong"

print("Your password is", strength)