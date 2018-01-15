class LightModel:
    def __init__(self):
        self.__led_dg_state = False
        self.__led_milieu_state = False

    @property
    def led_dg_state(self):
        return self.__led_dg_state

    @led_dg_state.setter
    def led_dg_state(self, state):
        self.__led_dg_state = state

    @property
    def led_milieu_state(self):
        return self.__led_milieu_state

    @led_milieu_state.setter
    def led_milieu_state(self, state):
        self.__led_milieu_state = state
