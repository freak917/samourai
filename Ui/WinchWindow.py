from tkinter import *
from tkinter.ttk import *

from Ui.PushButton import PushButton
from Ui.ToggleButton import ToggleButton
from Ui.ToplevelModal import ToplevelModal


class WinchWindow(ToplevelModal):
    def __init__(self, parent):
        super().__init__(parent, title="Treuil")
        label = Label(self, text="Activer : ")
        label.grid(row=1, column=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        button = ToggleButton(self)
        button.grid(row=1, column=2)

        button.set_on_callback(self._parent.controler().winch_enable)
        button.set_off_callback(self._parent.controler().winch_disable)

        self.__up_button = self.__build_up_button()
        self.__up_button.grid(row=3, column=1)

        self.__down_button = self.__build_down_button()
        self.__down_button.grid(row=3, column=2)

        self.disable()

    def __build_up_button(self):
        photo = PhotoImage(file="Images/caret-square-o-up.png")
        photo = photo.subsample(int(64 / 32), int(64 / 32))
        up_button = PushButton(self, image=photo)
        up_button.image = photo
        up_button.set_press(self._parent.controler().on_up_winch_press)
        up_button.set_release(self._parent.controler().on_up_winch_release)

        return up_button

    def __build_down_button(self):
        photo = PhotoImage(file="Images/caret-square-o-down.png")
        photo = photo.subsample(int(64 / 32), int(64 / 32))
        down_button = PushButton(self, image=photo)
        down_button.image = photo
        down_button.set_press(self._parent.controler().on_down_winch_press)
        down_button.set_release(self._parent.controler().on_down_winch_release)

        return down_button

    def enable(self):
        self.__up_button.config(state=NORMAL)
        self.__down_button.config(state=NORMAL)

    def disable(self):
        self.__up_button.config(state=DISABLED)
        self.__down_button.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    window = WinchWindow(root)
    # window.show()
    root.wait_window(window)
    # root.mainloop()
