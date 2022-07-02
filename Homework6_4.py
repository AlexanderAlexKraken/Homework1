class Car:
# атрибуты класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def on_go(self):
        return('Машина поехала')
    def to_stop(self):
        return('Машина остановилась')
    def to_turn_left(self):
        return('Машина повернула налево')
    def show_speed(self, speed):
        self.speed = speed
        return('Текущая скорость')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость')
        if self.speed < 60:
            return("speed Ok")
        else:
            return("speed limit!")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        print(f'Текущая скорость')
        if self.speed < 40:
            print (f'speed Ok')
        else:
            print(f'speed limit!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = SportCar(100, 'green', 'Tesla', False)
a_2 = TownCar(48, 'Black', 'Ford', True)
a_3 = WorkCar(66, 'Red', 'Skoda Kodiaq', False)
a_4 = PoliceCar(40, 'grey', 'Kia', True)

print(a.name, a.color, a.speed, a.is_police)
print(a_2.to_turn_left())
print(a_4.to_turn_left())
print(a_2.to_stop())
print(a.on_go())
print(a_4.is_police)
print(a_3.show_speed)
print(a_2.show_speed, a.is_police)