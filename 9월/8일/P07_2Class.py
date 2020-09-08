class Car:
    def __init__(self, name, eg, ss, mx, fl):
        self.name = name
        self.engine = eg
        self.seats = ss
        self.max_power = mx
        self.fuel = fl
        self.distance = 0

    def ready(self):
        print(f"{self.name} 준비됨!")

    def increase_distance(self):
        self.distance += self.engine
        self.fuel -= 15
        print(f"{self.name} = {self.distance}m")
        if self.fuel <= 0:
            print(f"Warning {self.name}")


class Bicycle:
    def __init__(self, name, eg,  mx):
        self.name = name
        self.engine = eg
        self.seats = 1
        self.max_power = mx
        self.distance = 0

    def ready(self):
        print(f"{self.name} 준비됨!")

    def increase_distance(self):
        self.distance += self.engine
        print("%s = %dm" % (self.name, self.distance))


class Human:
    def __init__(self, name, eg, ss, mx):
        self.name = name
        self.engine = eg
        self.seats = ss
        self.max_power = mx
        self.distance = 0
        self.health = 100

    def ready(self):
        print(f"{self.name} 준비됨!")

    def increase_distance(self):
        self.distance += self.engine
        print("%s = %dm" % (self.name, self.distance))


# Main
car1 = Car("차", 10, 4, 100, 100)
sports_car = Car("스포츠 카", 20, 2, 200, 200)
car2 = Car("보통차", 8, 4, 100, 50)
bicycle = Bicycle("자전거", 2, 10)
human = Human("사람", 1, 0, 2)


print("Ready!!-----------------")
racing_units = [car1, sports_car, car2, bicycle, human]
for i in racing_units:
    i.ready()

print("Racing-----------------")
for distance in range(100):
    for i in racing_units:
        i.increase_distance()

    just_waiting = input("next?---------------")
