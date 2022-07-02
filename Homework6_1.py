from time import sleep
class TrafficLight:
    # атрибуты класса
    __traffic_color_name = ["red", "yellow", "green"]

    # методы класса
    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается\n 'f'{TrafficLight.__traffic_color_name[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1

tl = TrafficLight()
print(tl)
print(type(tl))
print(tl._TrafficLight__traffic_color_name)
tl.running()
