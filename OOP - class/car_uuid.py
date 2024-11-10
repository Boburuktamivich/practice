from uuid import uuid4
class Car:
    def __init__(self, make: str, model: str, color: str, price: int, year: int, km: int):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.year = year
        self.__km = km
        self.__id = uuid4()
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        if km >  0:
            self.__km += km
        else:
            print('the mileage of the car cannot be reduced')
x = Car('bmw', 'm3 compitition', 'green', 1_000_000, 2023, 1000)
print(x.add_km(100))
print(x.get_km())
print(x.get_id())