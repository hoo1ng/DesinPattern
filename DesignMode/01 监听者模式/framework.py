from abc import ABCMeta, abstractmethod


# 观察者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, object):
        pass


# 被观察者
class Observable:

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifesObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前的水温是： " + str(self.getTemperature()) + "摄氏度")
        self.notifesObservers()


class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() > 50 and observable.getTemperature() < 70:
            print("水已经烧好了!温度正好，可以用来洗澡")


class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已经烧开! 可以用来饮用了~")
