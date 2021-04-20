import time


class TrafficLight:
    # атрибуты
    __color = 'мигающий желтый'
    __color_dict = {'красный': 7, 'желтый': 2, 'зеленый': 6}

    def running(self):
        for i in self.__color_dict:
            self.__color = i
            print(self.__color)
            time.sleep(self.__color_dict[i])


a = TrafficLight()
print(a.running())
