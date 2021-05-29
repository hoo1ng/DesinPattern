from abc import ABCMeta, abstractmethod


class WaterHeater:

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is : " + str(self.__temperature) + "C")
        self.notifies()

    def addObservers(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):

    def update(self, waterHeater):
        if 50 < waterHeater.getTemperature() < 70:
            print("washing mode ...")


class DrinkingMode(Observer):
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("drinking mode ...")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()

    heater.addObservers(washingObser)
    heater.addObservers(drinkingObser)

    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)

if __name__ == '__main__':
    testWaterHeater()
