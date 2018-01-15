class WinchCrontroler:
    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def winch_enable(self):
        self.__model.state = True
        self.__view.update()

    def winch_disable(self):
        self.__model.state = False
        self.__view.update()

    def on_up_winch_press(self, *event):
        print("up press")

    def on_up_winch_release(self, *event):
        print("up release")

    def on_down_winch_press(self, *event):
        print("down press")

    def on_down_winch_release(self, *event):
        print("down release")
