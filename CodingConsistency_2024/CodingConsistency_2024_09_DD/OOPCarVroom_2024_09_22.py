class Car:
    def __init__(self, make, model, year, fuel_level):
        self.make = make 
        self.model = model  
        self.year = year 
        self.fuel_level = fuel_level  
        self.is_running = False  

    def start(self):
        if self.fuel_level > 0:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} is running.")
        else:
            self.is_running = False
            print(f"Cannot start the {self.make} {self.model}. Fuel tank is empty.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.make} {self.model} is already off.")
    
    def refuel(self, amount):
        self.fuel_level += amount
        print(f"The {self.make} {self.model} is refueled {amount} liters. Fuel level is {self.fuel_level}")

my_car = Car("toyota", "corola", 2022, 10)
my_car.start()  
my_car.stop()   
my_car.refuel(5)  
my_car.start()  

#OOP Class practice, couldn't do C again right now since im super sick.