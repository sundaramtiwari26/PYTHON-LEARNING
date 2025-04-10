class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

car1=Car('toyata','carry',2022)
car2=Car('ford','mustang',2021)
car1.display_info()
car2.display_info()