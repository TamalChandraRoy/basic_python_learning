number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0

for num in number:
  if num > 0:
    positive_number_count += 1
print("Final positive number count: ", positive_number_count)