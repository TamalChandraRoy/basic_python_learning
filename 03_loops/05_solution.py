input_str = input("Enter your name ")

for  char in input_str:
  if (input_str.count(char)) == 1:
    print("Char is : ", char)
    break