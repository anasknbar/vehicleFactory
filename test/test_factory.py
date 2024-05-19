import pytest

from factory.car import Car
from factory.motorcycle import Motorcycle



@pytest.fixture
def car_instance():
  return Car('BMW','electric','gray',4)




def test_car_atrributes(car_instance):
  assert car_instance.model == 'BMW'
  assert car_instance.fuel == 'electric'
  assert car_instance.color == 'gray'
  assert car_instance.door_number == 4
 
  

  
def test_car_attributeError(car_instance): # attributes can be modified using only built-in method
  with pytest.raises(AttributeError):
    car_instance.color = 'white'


    
def test_car_built_in_method(car_instance):
  car_instance.change_model_name('Mercedes')
  car_instance.change_fuel_type('electric')
  car_instance.change_car_color('blue')
  car_instance.change_door_number(2)
  
  
  assert car_instance.model == 'Mercedes'
  assert car_instance.fuel == 'electric'
  assert car_instance.color == 'blue'
  assert car_instance.door_number == 2


@pytest.fixture
def motorcycle_instance():
  return Motorcycle('Hundi','diesel',2)

def test_motorcycle_atrributes(motorcycle_instance):
  assert motorcycle_instance.model == 'Hundi'
  assert motorcycle_instance.fuel == 'diesel'
  assert motorcycle_instance.wheels_number == 2

def test_motorcycle_attributeError(motorcycle_instance): # attributes can be modified using only built-in method 
  with pytest.raises(AttributeError):
    motorcycle_instance.fuel = 'diesel'
    
    
def test_motorcycle_built_in_method(motorcycle_instance):
  motorcycle_instance.change_model_name('Harrly Dav')
  motorcycle_instance.change_fuel_type('electric')
  
  assert motorcycle_instance.model == 'Harrly Dav'
  assert motorcycle_instance.fuel == 'electric'
 




