class WinchModel:
    def __init__(self):
        self.__enable_winch = False

    @property
    def state(self):
        return self.__enable_winch

    @state.setter
    def state(self, state):
        self.__enable_winch = state
