class Road:
    def road_need(self, lenght, width):
        if width is not None:
            print (lenght * width * 25 * 0.05)
        else:
            print("none")

a = Road()
a.road_need(20, 30)