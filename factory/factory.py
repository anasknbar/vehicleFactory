from abc import ABC,abstractmethod
from prettytable import PrettyTable
class Factory(ABC):

  def __init__(self,model,fuel):
    self._model = model 
    self._fuel = fuel
  
  
     
  
  @property
  def model(self):
    return self._model
  @model.setter
  def model(self,model):
    raise AttributeError("modification of 'model' attribute is not allowed directly. use 'change_model_type' method.")  
  
  
  @property
  def fuel(self):
    return self._fuel
  
  @fuel.setter
  def fuel(self,fuel):
    raise AttributeError("modification of 'fuel' attribute is not allowed directly. use 'change_fuel_type' method.")
  
  
  # method to calculate the overall production of cars and motorcycles
  def overall_production(self):
    overall_prduction = 0
    car_production = 0 
    motorcycle_production = 0
    with open('production/car.txt') as file:
      prduction,cars_count = file.readline().split(',')
      car_production = cars_count
      overall_prduction+=int(cars_count)
    with open('production/motorcycle.txt') as file:
      prduction,motorcycle_count = file.readline().split(',')
      motorcycle_production = motorcycle_count
      overall_prduction+=int(motorcycle_count)
    print(f'until now we produce {car_production} cars and {motorcycle_production} motorcycles with {overall_prduction} overall production ')
    
  # common function are abstracted in the Factory(parent) class
  @abstractmethod
  def change_model_name(self,new_model_name):
    pass
  @abstractmethod
  def change_fuel_type(self,new_fuel_type):
    pass