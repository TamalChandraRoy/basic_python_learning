import time 

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    results = func(*args, **kwargs)
    end = time.time()
    print(f"{func.__name__} run in {end - start} time")
    return results
  return wrapper

@timer
def example_func(n):
  time.sleep(n)

example_func(3)
# timer(example_func(3))