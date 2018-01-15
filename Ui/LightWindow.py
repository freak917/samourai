from tkinter import *
from tkinter.ttk import *

from Controler.LightControler import LightCrontroler
from Ui.ToggleButton import ToggleButton
from Ui.ToplevelModal import ToplevelModal


class LightWindow(ToplevelModal):
    def __init__(self, parent):
        super().__init__(parent, title="Eclairage")

        self.__controler = LightCrontroler(self)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        label = Label(self, text="Led D/G : ")
        label.grid(row=1, column=1)

        led_dg_button = ToggleButton(self)
        led_dg_button.grid(row=1, column=2)

        led_dg_button.set_on_callback(self.__controler.led_dg_on)
        led_dg_button.set_off_callback(self.__controler.led_dg_off)

        label = Label(self, text="Led Milieu : ")
        label.grid(row=3, column=1)

        led_milieu = ToggleButton(self)
        led_milieu.grid(row=3, column=2)

        led_milieu.set_on_callback(self.__controler.led_milieu_on)
        led_milieu.set_off_callback(self.__controler.led_milieu_off)
