weather = input("Enter Your weather")
weather = weather.lower()
# print(weather)
if weather == "sunny":
  activitys = "Go for a walk"
elif weather == "rainy":
  activitys = "Read a book"
elif weather == "snowy":
  activitys = "Build a snowman"
else:
  print("I have not a information")
  exit()
print(activitys)