class Vehicle():
    licenCode=""
    serialCode=""
    name = ""
    color = ""
    def TurnOn_Air(self):
        print("tern on: air")
    def typeOfCar(self):
        print("Type car:"+self.name)
    def Color(self):
        print("Color:"+self.color)

    def TurnOn_Air(self):
        print("tern on: air")
        print("-----------------------")
class car(Vehicle):
    pass;


class pickUp(Vehicle):
    pass;
class van(Vehicle):
    pass;
class estateCar(Vehicle):
    pass;

car1=car()
car1.name="car1"
car1.color="red"
car1.typeOfCar()
car1.Color()
car1.TurnOn_Air()

pickUp1=pickUp()
pickUp1.name="pickUp"
pickUp1.color="blue"
pickUp1.typeOfCar()
pickUp1.Color()
pickUp1.TurnOn_Air()

van1=van()
van1.name="pickUp"
van1.color="blue"
van1.typeOfCar()
van1.Color()
van1.TurnOn_Air()

estateCar1=estateCar()
estateCar1.name="sport"
estateCar1.color="black"
estateCar1.typeOfCar()
estateCar1.Color()
estateCar1.TurnOn_Air()