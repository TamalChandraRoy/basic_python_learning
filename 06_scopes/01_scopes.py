def fun1(num):
  def fun2(x):
    return x ** num
  return fun2
f = fun1(2)
g = fun1(4)
print(f(3))
print(g(3))