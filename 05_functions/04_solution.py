import math

def corcle_stats(radius):
  area = math.pi * radius ** 2
  circuference  = 2 * math.pi * radius
  return area, circuference

are, cir_feren = corcle_stats(5)
print("Area: ", are, "circuference: ", cir_feren)