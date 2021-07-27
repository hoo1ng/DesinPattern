class Register:
    def register(self, name):
        print("活动中心： %s 同学报道成功！" % name)


class Payment:
    def pay(self, name, money):
        print("缴费中心：收到%s同学%s元付款，缴费成功！" % (name, money))


class DormitoryManagementCenter:
    def provideLivingGoods(self, name):
        print("生活中心：%s 同学的生活用品已发放。" % name)


class Dormitory:
    def meetRoommate(self, name):
        print("宿舍： 大家好！这是刚来的 %s同学，是你们未来需要共读四年的室友！相互认识一下...." % name)


class Volunteer:
    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcomeFreshmen(self, name):
        print("您好，%s同学！ 我是新生报到的志愿者%s,我将带你完成整个报道流程。" % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)

if __name__ == '__main__':
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("tony")