class Car:
    def __init__(self, make, model, color, km, price, year, number, speed=0):
        self.__make = make
        self.__model = model
        self.color = color
        self.__km = km
        self.__price = price
        self.__year = year
        self.__number = number
        self.__speed = speed

    def get_info(self):
        return f"make: {self.__make}, model: {self.__model}, color: {self.color}, mileage: {self.__km}km, price: {self.__price}$, year: {self.__year}, car number: {self.__number}, car speed: {self.__speed}"
    
    def get_km(self):
        return self.__km

    def add_km(self, km):
        if km > 0:
            self.__km += km
        else:
            return 'error'

class Electro_car(Car):
    def __init__(self, make, model, color, km, price, year, number, speed, accumulator):
        super().__init__(make, model, color, km, price, year, number, speed)
        self.accumulator = accumulator
    
    def get_w(self):
        return self.accumulator
    
    def set_w(self, km):
        """mashina akkumulyatorining hajmi 325 000kw.
        mashina akkumulyatori har 100 kmda 1% kamayadi. 
        sizga qancha km mashina haydaganingiz berilgan bolsa. 
        mashina akkumulyarida qolgan kw ni hisoblang """
        a = km // 100
        b = (self.accumulator - a) / 100
        return self.accumulator - b
    


c = Electro_car('tesla', 'm5', 'black', 1000, 1000000, 2023, '30-77-ZZZ-7', 300, 325_000)
print(c.set_w(5000))
