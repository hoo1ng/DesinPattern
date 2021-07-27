from copy import  copy, deepcopy


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMySelf(self):
        print("我是" + self.__name + ",年龄" + str(self.__age) + ",")

    def coding(self):
        print("我是码农，我用程序改变世界，Coding...")

    def reading(self):
        print("阅读是我快乐！知识是我成长！如饥似渴地阅读是生活的一部分....")

    def fallInLove(self):
        print("春风吹，月亮明，花前月下好相约....")

    def clone(self):
        return copy(self)


if __name__ == '__main__':
    tony = Person("Tony", 27)
    tony.showMySelf()
    tony.coding()

    print()

    tony1 = tony.clone()
    tony1.showMySelf()
    tony1.reading()

    print()

    tony2 = tony.clone()
    tony2.showMySelf()
    tony2.fallInLove()
