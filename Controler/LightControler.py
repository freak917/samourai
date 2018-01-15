class LightCrontroler:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def led_dg_on(self):
        self.__model.led_dg_state = True
        self.__view.update()

    def led_dg_off(self):
        self.__model.led_dg_state = False
        self.__view.update()


    def led_milieu_on(self):
        self.__model.led_milieu_state = True
        self.__view.update()

    def led_milieu_off(self):
        self.__model.led_milieu_state = False
        self.__view.update()
