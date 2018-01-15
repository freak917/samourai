class MainCrontroler:
    def __init__(self, view):
        self.__view = view

    def on_escape(self, *event):
        self.__view.attributes("-fullscreen", False)

    def on_quit(self, *event):
        self.__view.destroy()

    def on_F11_pressed(self, *event):
        self.__view.attributes("-fullscreen", True)

    def on_winch_button(self, *event):
        self.__view.open_winch_win()
