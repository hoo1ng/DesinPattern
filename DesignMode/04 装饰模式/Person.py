from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("着装：")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        print("我是 " + self.getSkill() + "工程师" + self._name, end=", ")
        super().wear()


class Teacher(Person):
    def __init__(self, name, title):
        super(Teacher, self).__init__(name)
        self.__title = title

    def getTitle(self):
        return self.__title

    def wear(self):
        print("我是 " + self._name + self.getTitle(), end=", ")
        super().wear()


class ClothingDecorator(Person):
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasulPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条卡其色休闲裤")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一条樱色针扣头的黑色腰带")


class LeatherShoesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一双深色休闲皮鞋")


class KnittedSweaterDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件红色针织毛衣")


class WhiteShirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一件白色衬衫")


class GlassedDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("一副方形黑框眼镜")


if __name__ == '__main__':
    tony = Engineer("Tony", "客户端开发")
    pant = CasulPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    sweater = KnittedSweaterDecorator(shoes)
    glasses = GlassedDecorator(sweater)
    glasses.wear()

    print()

    decorateTeacher = GlassedDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells", "教授"))))
    decorateTeacher.wear()

