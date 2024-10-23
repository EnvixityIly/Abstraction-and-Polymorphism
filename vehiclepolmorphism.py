class Ferrari:
    def fuel_type(self):
        print("Petrol")
    def max_speed(self):
        print("Max speed 350")
class BMW:
    def fuel_type(self):
        print("diesel")
    def max_speed(self):
        print("max speed 240")
class Tesla:
    def fuel_type(self):
        print("electric")
    def max_speed(self):
        print("322")
class Bugatti:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("420")
class Porsche:
    def fuel_type(self):
        print("petrol")
    def max_speed(self):
        print("330")

ferrari = Ferrari()
bmw = BMW()
bugatti = Bugatti()
tesla = Tesla()
porsche = Porsche() 
for car in (ferrari,bmw,bugatti,tesla,porsche):
    car.max_speed()
    car.fuel_type()