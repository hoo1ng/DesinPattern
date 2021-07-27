from abc import ABCMeta, abstractmethod


class ComputerComponent(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent=" "):
        pass

    def isComposite(self):
        return False

    def startup(self, indent=" "):
        print("%s%s 准备开始工作..." % (indent, self._name))

    def shutdown(self, indent=" "):
        print("%s%s 即将结束工作..." % (indent, self._name))


class CPU(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%sCPU:%s,可以进行告诉运算。 " % (indent, self._name))


class MemoryCard(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s内存:%s,可以缓存数据，读写更快。 " % (indent, self._name))


class HardDisk(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s硬盘:%s,可以永久存储数据，容量大。 " % (indent, self._name))


class GraphicsCard(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显卡:%s,可以高速计算和处理图形图像。 " % (indent, self._name))


class Battery(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s电源:%s,可以持续给主板和外界配件供电。 " % (indent, self._name))


class Fan(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s风扇:%s,可以持续给主板和外界配件供电。 " % (indent, self._name))


class Displayer(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s显示器:%s,可以显示界面和打游戏。 " % (indent, self._name))

class ComputerComposite(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent):
        print("%s,由一下部件组成：" % self._name)
        indent += '\t'
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True

    def addComposite(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def startup(self, indent):
        super().startup(indent)
        indent += '\t'
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent):
        super().shutdown(indent)
        indent += '\t'
        for element in self._components:
            element.shutdown(indent)


class MainBoard(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板：", end="")
        super().showInfo(indent)


class ComputerCase(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "机箱:", end="")
        super().showInfo(indent)


class Computer(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent, "电脑：", end="")
        super().showInfo(indent)


if __name__ == '__main__':
    mainBoard = MainBoard("GIGABYTE Z179M M-ATX")
    mainBoard.addComposite(CPU("Intel Core I5-5500k"))
    mainBoard.addComposite(MemoryCard("Kingston Fury DDR4"))
    mainBoard.addComposite(HardDisk("Kingston V300"))
    mainBoard.addComposite(GraphicsCard("Colorful iGame750"))

    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComposite(mainBoard)
    computerCase.addComposite(Battery("Anter VP 450P"))
    computerCase.addComposite(Fan("DEEPCOOL 120T"))

    computer = Computer("Tony DIV 电脑")
    computer.addComposite(computerCase)
    computer.addComposite(Displayer("AOC Lv24XIP"))

    computer.showInfo("")
    print("\n 开机过程")
    computer.startup("")
    print("\n 关机过程")
    computer.shutdown("")
