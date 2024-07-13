score = int(input ("Enter your score"))

if score > 100:
  print("Your score is wrong")
  exit ()
elif score >= 90:
  great = "A"
elif score >= 80:
  Great = "B"
elif score >= 70:
  great = "C"
elif score >= 60:
  great = "D"
else:
  great = "F"

print(great)