from abc import ABCMeta, abstractmethod


class ReceiveParcel(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


class TonyReception(ReceiveParcel):

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def receive(self, parcelContent):
        print("货物主人： %s ,手机号： %s " % (self.getName(), self.getPhoneNum()))
        print("接收到一个包裹，包裹内容： %s " % parcelContent)


class WendyReception(ReceiveParcel):

    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcelContent):
        print("我是%s的朋友，我来帮他收快递！" %(self.__receiver.getName() + " " ))
        if self.__receiver is not None:
            self.__receiver.receive(parcelContent)

        print("代收人：%s" % self.getName())


if __name__ == '__main__':
    tony = TonyReception("Tony", "18888888888")
    print("Tony接受：")
    tony.receive("雪地靴")
    print()

    print("Wendy代收：")
    wendy = WendyReception("Wendy", tony)
    wendy.receive("雪地靴")