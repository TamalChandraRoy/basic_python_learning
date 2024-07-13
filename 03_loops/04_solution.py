input_str = input("Enter your reverse string")
reverse_str = ""

for char in input_str:
  reverse_str = char + reverse_str
  
print(reverse_str)