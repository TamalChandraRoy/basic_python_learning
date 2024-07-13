number = 72
is_prime = True

if number > 1:
  for i in range(1, number):
    if (number % i )== 0:
      is_prime = False
      break
    
print(is_prime)