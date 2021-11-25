#Idris Adeyemi
#11/14/21
#Problem 6, a code that shows the type,year and model of a car

class car:
    def __init__(self, model, year, color,manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return self.model + '' + str(self.year) + '' + self.color + '' + self.manufacturer

car1 = car("sports", 2021, "Red", "Acura")
car2 = car("sedan", 2021, "blue", "Acura")
print(car1.get_color())
print(car2.get_color())
print(car1.fullspecs())
print(car1.fullspecs())
