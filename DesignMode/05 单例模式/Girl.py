class MyBeaultifulGril(object):
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeaultifulGril.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇见" + name + ", 我一见钟情")
            self.__isFirstInit = True
        else:
            print("遇见" + name + ", 我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就是我心中的唯一！")


if __name__ == '__main__':
    jenny = MyBeaultifulGril("Jenney")
    jenny.showMyHeart()
    print()
    kimi = MyBeaultifulGril("kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), "id(kimi)", id(kimi))