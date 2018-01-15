from tkinter import *
from tkinter.ttk import *

from Controler.MainControler import MainCrontroler
from Ui.LightWindow import LightWindow
from Ui.WinchWindow import WinchWindow
from Ui.Window import Window as UiWindow


class MainWindow(UiWindow):
    def __init__(self, title=None, width=None, height=None):
        super().__init__(title, width, height)

        self.__controler = MainCrontroler(self)
        self.__winch_window = None
        self.__light_window = None

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        self.__build_frame()

        # self.bind('<Escape>', self.__controler.on_escape)
        # self.bind('<F11>', self.__controler.on_F11_pressed)

    def quit(self):
        self.__controler.on_quit()

    def __build_frame(self):
        winch_button = self.__build_winch_button()
        winch_button.grid(row=1, column=1, ipadx=30, ipady=30)
        light_button = self.__build_light_button()
        light_button.grid(row=1, column=3, ipadx=30, ipady=30)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def __build_winch_button(self):
        photo = PhotoImage(file="Images/gear.png")
        photo = photo.subsample(int(256 / 32), int(256 / 32))
        winch_button = Button(self, image=photo, text="Treuil", compound=TOP, command=self.__controler.on_winch_button)
        winch_button.image = photo
        winch_button.height = 128
        winch_button.width = 128

        return winch_button

    def __build_light_button(self):
        photo = PhotoImage(file="Images/lightbulb-o.png")
        photo = photo.subsample(int(256 / 32), int(256 / 32))
        light_button = Button(self, image=photo, text="Eclairage", compound=TOP,
                              command=self.__controler.on_light_button)
        light_button.image = photo

        return light_button

    def open_winch_win(self):
        self.__winch_window = WinchWindow(self)

    def open_light_win(self):
        self.__light_window = LightWindow(self)

    def controler(self):
        return self.__controler

    def winch_window(self):
        # TODO
        return self.__winch_window


if __name__ == '__main__':
    window = MainWindow(title="Pull&Light", width=800, height=600)
    window.mainloop()
