class Vehicle:              #Mother Class
    licenseNumber = ""
    serialCode = ""
    face = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):         #Daughter Class
    pass

class PickUp(Vehicle):      #Daughter Class
    pass

class Van(Vehicle):         #Daughter Class
    pass

class Estatecar(Vehicle):   #Daughter Class
    pass

car1 = Car()
PickUp1 = PickUp()
Van1 = Van()
Estatecar1 = Estatecar()

car1.turnOnAirConditioner()
PickUp1.turnOnAirConditioner()
Van1.turnOnAirConditioner()
Estatecar1.turnOnAirConditioner()

