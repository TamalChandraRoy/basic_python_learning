class Car:
  total_car = 0
  def __init__(self, brand, mobel):
    self.__brand = brand
    self.__mobel = mobel
    Car.total_car += 1
  
  def get_brand(self):
    return self.__brand + " !"
  
  def full_name(self):
    return f"{self.__brand} {self.mobel}"
  
  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod
  def general_decription():
    return "Cars are means of transport"
  
  @property
  def mobel(self):
    return self.__mobel

class ElectricCar(Car):
  def __init__(self, brand, mobel, bettery_size):
    super().__init__(brand, mobel)
    self.bettery_size = bettery_size
  
  def fuel_type(self):
    return "Electric charge"

my_tesla_car = ElectricCar("Tesla", "Mobel S", "85kw/h")
# print(my_electric_car.brand)
print(my_tesla_car.get_brand())
print(my_tesla_car.mobel)
print(my_tesla_car.full_name())
print(my_tesla_car.fuel_type())
print("Is a instance ", isinstance(my_tesla_car, Car))
print("Is a instance ", isinstance(my_tesla_car, ElectricCar))

# my_new_car = Car("Rose Royal", "mobel R")
# print(my_new_car.get_brand())
# print(my_new_car.mobel)
# print(my_new_car.full_name())
# print(my_new_car.fuel_type())

# my_car = Car("Bugatti", "Sonic S36")
# print(my_car.brand)
# (my_car.mobel)
# print(my_car.full_name())

# print(Car.total_car)
# print(Car.general_decription()) 

class Battery:
  def battery_info(self):
    return "This is Battery"

class Engine:
  def engine_info(self):
    return "This is Engine"

class ElectricCarTwo(Car, Battery, Engine):
  pass 
