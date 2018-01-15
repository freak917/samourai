from tkinter import *
from tkinter.ttk import *


class Window(Tk):
    def __init__(self, title=None, width=None, height=None):
        super().__init__()
        self.__style = None
        self.set_properties(title, width, height)
        self.define_style()

    def define_style(self):
        self.__style = Style()
        self.__style.theme_use('default')

    def set_properties(self, title, width, height):

        if title is not None:
            self.title(title)

        if width is not None and height is not None:
            geometry = str(width) + "x" + str(height)
            self.geometry(geometry)
        self.protocol("WM_DELETE_WINDOW", self.quit)

    def quit(self):
        self.destroy()
