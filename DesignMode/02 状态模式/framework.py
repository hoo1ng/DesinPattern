from abc import ABCMeta, abstractmethod


class Context:
    def __init__(self):
        self.__states = []
        self.__state_info = None
        self.__current_state = None

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        self.__current_state = state
        self.add_state(state)

    def set_state_info(self):
        for state in self.__states:
            if state.is_match(self.__state_info):
                self.change_state(state)

    def behavior(self):
        self.__current_state.behavior(self)


class State(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_match(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass
