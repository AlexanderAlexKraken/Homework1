class Road:
    # атрибуты класса
    __lenght = 0
    __width = 0

    # методы класса
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def road_need(self):
        asphalt = self.lenght * self.width * 25 * 0.05
        print(f'нужно {asphalt} тонн для покрытия всей дороги')

a = Road(1, 2)
a.road_need()