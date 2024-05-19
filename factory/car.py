
from factory import Factory
from prettytable import PrettyTable




class Car(Factory):
  def __init__(self,model,fuel,color,door_number=4):
    super().__init__(model,fuel)
    
    if door_number not in [2,4]:
      raise ValueError("door number can be 4 or 2")
    self._door_number = door_number
    self._color = color 
    self.write_production() # this function for writing the production in the file
    
      
  def change_model_name(self,new_model_name): # implemtation of the absracted function in the children, model attrubute is protected in the parent class (Factory)
    self._model = new_model_name 
    
  def change_fuel_type(self,new_fuel_type): # implemtation of the absracted function in the children,fuel attrubute is protected in the parent class (Factory)
    if new_fuel_type in ['electric', 'petrol', 'diesel']:
      self._fuel = new_fuel_type
    else:
      raise ValueError('choose electric, petrol, or diesel type')
    
  def change_car_color(self,new_color):
    self._color = new_color
  def change_door_number(self,new_door_number):
    if new_door_number not in [2,4]:
      raise ValueError("door number can be 4 or 2")
    self._door_number = new_door_number
  
  @property
  def color(self):
    return self._color
  @color.setter
  def color(self,color):
    raise AttributeError("modification of 'color' attribute is not allowed directly. use 'change_car_color' method.")   
   
  @property
  def door_number(self):
    return self._door_number
  @door_number.setter
  def door_number(self,door_number):
    raise AttributeError("modification of 'door number' attribute is not allowed directly. use 'change_door_number' method.")  
  
   
  def write_production(self):
    with open('production/car.txt','r') as file:
      production,count  = file.readline().split(',')
      count = int(count) +  1
      with open('production/car.txt','w') as file:
        file.write(f'car prduction,{count}')
 
  def read_production(self):
    with open('production/car.txt','r') as file:
      production,count  = file.readline().split(',')
      print(f'the factory have been creating {count} cars until now')
   
  def __str__(self):

   
    table = PrettyTable(['Car Model', 'Fuel Type', 'Color', 'Door Number'])
    table.add_row([self.model, self.fuel, self.color, self.door_number])
    table.align = 'l'
    return(f'{table}\n')