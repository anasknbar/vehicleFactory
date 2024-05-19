from car import Car
from motorcycle import Motorcycle



def main():
  
  car = Car('Honda','electric','gray',4)
  #### can not re-assign the following atrributes, because I should use the built-in method
  # car.fuel = 'petrol'
  # car.color = 'black'
  # car.door_number =  2
  # car.model =  'BMW'
  
  #### built-in method to change the atrributes 
  # car.change_fuel_type('petrol')
  # car.change_car_color('black')
  # car.change_door_number(2)
  # car.change_model_name('BMW')
  
  #### method to read the cars production
  # car.read_production()
  
  #### method to read overall production for cars and motorcycle
  # car.overall_production()
  
  # print(car)
  
 

 

if __name__ == "__main__":
    main()