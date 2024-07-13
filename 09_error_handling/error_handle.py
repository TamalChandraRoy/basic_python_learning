file = open("youtube.txt", "w")

try:
  file.write("YouTube channel number one")
finally:
  file.close()
  
with open("youtube.txt", "w") as file:
  file.write("YouTube channel two ")