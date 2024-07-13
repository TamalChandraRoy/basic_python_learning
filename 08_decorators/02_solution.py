
def debug(func):
  def wrapper(*args, **kwargs):
    args_value = ", ".join(str(arg) for arg in args)
    kwargs_value = ", ".join(f"{k}, {v}" for k, v in kwargs.items())
    print(f"calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
    results = func(*args, **kwargs)
    return results
  return wrapper





@debug
def greet(name, greeting= "Hello"):
  print(f"{greeting}  {name}")
  
greet("John", "Hi")

@debug
def hello(hello):
  print(hello)
hello("Hello World")