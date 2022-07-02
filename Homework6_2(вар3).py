class Road:
    # атрибуты класса
    _lenght = 0
    _width = 0
    # методы класса
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def road_need(self):
        self.weigth = 25
        self.thickness = 0.05
        asphalt = self.lenght * self.width * self.weigth * self.thickness
        print(f'нужно {asphalt} тонн')

a = Road (10, 20)
a.road_need()