class Customer:
    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class NumeralIterator:
    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        if self.__curIdx < len(self.__data) -1:
            self.__curIdx += 1
            return True
        else:
            return False

    def current(self):
        return self.__data[self.__curIdx] if self.__curIdx < len(self.__data) and self.__curIdx >= 0 else None


class NumberalSystem:
    __clinics = ("1号诊室", "2号正式诊室", "3号正式诊室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        click = NumberalSystem.__clinics[self.__curNum % len(NumberalSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)
        print("%s 您好！ 您已在 %s 成功挂号，序号：%04d，请耐心等待！" % (customer.getName(), self.__name, customer.getNum()))

    def getIterator(self):
        return NumeralIterator(self.__customers)


if __name__ == '__main__':
    numeralSystem = NumberalSystem("挂号台")
    lily = Customer("Lily")
    lily.register(numeralSystem)
    pony = Customer("Pony")
    pony.register(numeralSystem)
    nick = Customer("Nick")
    nick.register(numeralSystem)
    tony = Customer("Tony")
    tony.register(numeralSystem)
    print()

    iterator = numeralSystem.getIterator()
    while(iterator.next()):
        customer = iterator.current()
        print("下一位病人 %04d(%s) 请到 %s 就诊。" % (customer.getNum(), customer.getName(), customer.getClinic()))