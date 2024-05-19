# lab oop1
## How To use the programm?

### create an instance of Car
    car = Car('Honda','electric','gray',4)

### can not re-assign the following atrributes, because I should use the built-in method

    car.fuel = 'petrol'   
    car.color = 'black'  
    car.door_number =  2  
    car.model =  'BMW'  
  
### built-in method to change the atrributes 

    car.change_fuel_type('petrol')  
    car.change_car_color('black')  
    car.change_door_number(2)  
    car.change_model_name('BMW')  
  
### method to read the cars production  

    car.read_production()  
  
### method to read overall production for cars and motorcycle

    car.overall_production()  

### print the result 

    print(car)



### create an instance of Motorcycle
    motorcycle = Motorcycle('Harrly','electric',4)

### can not re-assign the following atrributes, because I should use the built-in method

    motorcycle.fuel = 'petrol'    
    motorcycle.wheels_number =  2  
    motorcycle.model =  'Yamhua'  
  
### built-in method to change the atrributes 

    motorcycle.change_fuel_type('petrol')  
    motorcycle.change_wheels_number(2)  
    motorcycle.change_model_name('Yamhua')  
  
### method to read the cars production  

    motorcycle.read_production()  
  
### method to read overall production for cars and motorcycle

    motorcycle.overall_production()  

### print the result 

    print(motorcycle)