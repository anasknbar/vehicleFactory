
from factory import Factory
from prettytable import PrettyTable


class Motorcycle(Factory):
  def __init__(self,model,fuel,wheels_number=2):
    super().__init__(model,fuel)
    
    
    if wheels_number not in [2,4]:
      raise ValueError('wheels can be 2 or 4')
    self._wheels_number = wheels_number
    self.write_production()
 
  @property
  def wheels_number(self):
    return self._wheels_number
  @wheels_number.setter
  def wheels_number(self,wheels_number):
    raise AttributeError('you can not change wheels_number')
    
  
 
  
  
  def change_model_name(self,new_model_name):
    self._model = new_model_name
  
  def change_fuel_type(self,new_fuel_type):
    if new_fuel_type in ['electric', 'petrol', 'diesel']:
      self._fuel = new_fuel_type
    else:
      raise ValueError(f'choose electric, petrol, or diesel type')
    
 
  def write_production(self):
    with open('production/motorcycle.txt','r') as file:
      production,count  = file.readline().split(',')
      count = int(count) +  1
      with open('production/motorcycle.txt','w') as file:
        file.write(f'motorcycle prduction,{count}')
 
  def read_production(self):
    with open('production/motorcycle.txt','r') as file:
      production,count  = file.readline().split(',')
      print(f'the factory have been creating {count} motorcycles until now')
      
        
    
  
  def __str__(self):
   
    
    table = PrettyTable(['Motorcycle Model', 'Fuel Type', 'Wheels Number'])
    table.add_row([self.model, self.fuel, self.wheels_number])
    table.align = 'l'
    return(f'{table}\n')











