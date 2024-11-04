class car:
    def __init__(self,make, model, year, price, mileage, sold_status):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.sold_status = sold_status
    def det_info(self):
        return f'make: {self.make}, model: {self.model}, year: {self.year}, price: {self.price}$, mileage: {self.mileage}km, sold status: {self.sold_status}'
    def apply_discount(self, percent):
        return f'the price of this car is {self.price}$.  but you can buy this car at a discount of {self.price - ((self.price/100)*percent)}$'
    def mark_as_sold(self):
        return f'{self.model} is sold!'
x = car('bmw', 'm3 compitition', 2019, 1000000, 100000, 'new')
a = x.det_info()
b = x.apply_discount(15)
c = x.mark_as_sold()
print(f'{a}\n{b}\n{c}')