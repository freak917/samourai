class WinchCrontroler:
    def __init__(self, view):
        self.__view = view

    def winch_enable(self):
        print("treuil activer")
        self.__view.enable()

    def winch_disable(self):
        print("treuil desactiver")
        self.__view.disable()

    def on_up_winch_press(self, *event):
        print("up press")

    def on_up_winch_release(self, *event):
        print("up release")

    def on_down_winch_press(self, *event):
        print("down press")

    def on_down_winch_release(self, *event):
        print("down release")
