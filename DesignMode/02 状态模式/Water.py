from abc import ABCMeta, abstractmethod


class Water:
    def __init__(self):
        self.__temperatrue = 0
        self.__state = None

    def change_state(self, state):
        if self.state is None:
            print("初始化状态为：", state.get_name())
        else:
            print("状态由", self.__state.get_name(), "变更为：", state.get_name())

        self.__state = state

    def set_temperature(self, temperature):
        if temperature <= 0:
            self.change_state(SolidState())
        elif temperature <= 100:
            self.change_state(LiquidState())
        else:
            self.change_state(GaseousState())

    def get_temperatrue(self):
        return self.__temperatrue

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def behavior(self, water):
        pass


class SolidState(State):
    def __init__(self):
        super().__init__()
        self.name = "固态"

    def behavior(self, water):
        print("我是固态，当前温度为：", water.get_temperatrue())


class LiquidState(State):
    def __init__(self):
        super().__init__()
        self.name = "液态"

    def behavior(self, water):
        print("我是液态，当前温度为：", water.get_temperatrue())


class GaseousState(State):
    def __init__(self):
        super().__init__()
        self.name = "气态"

    def behavior(self, water):
        print("我是液态，当前温度为：", water.get_temperatrue())
