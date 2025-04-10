class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
#inheritance super class
class ElectricCar(Car):
    def __init__(self, make, model, year,battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity=battery_capacity
    def display_info(self):
        super().display_info()
        print(f"{self.battery_capacity}")
car1=Car('toyata','carry',2022)
car2=Car('ford','mustang',2021)
car1.display_info()
car2.display_info()
electric_car1=ElectricCar('toyata','carry',2022, 5500)
electric_car1.display_info()