def even_generator(limite):
  for i in range(2, limite + 1, 2):
    yield i

generat = even_generator(10000)
for i in generat:
  print(i)