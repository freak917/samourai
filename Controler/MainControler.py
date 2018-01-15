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

    def on_light_button(self, *event):
        self.__view.open_light_win()

    def on_up_winch_press(self, *event):
        print("up press")

    def on_up_winch_release(self, *event):
        print("up release")

    def on_down_winch_press(self, *event):
        print("down press")

    def on_down_winch_release(self, *event):
        print("down release")

    def led_dg_on(self):
        print("led droite/gauche on")

    def led_dg_off(self):
        print("led droite/gauche off")

    def led_milieu_on(self):
        print("led milieu on")

    def led_milieu_off(self):
        print("led milieu off")

    def winch_enable(self):
        print("treuil activer")
        # TODO
        self.__view.winch_window().enable()

    def winch_disable(self):
        print("treuil desactiver")
        # TODO
        self.__view.winch_window().disable()
