from tkinter import *


class ToplevelModal(Toplevel):
    def __init__(self, parent=None, title=None, width=300, height=300):
        super().__init__(parent)
        self.transient(parent)
        self.__parent = parent
        self.__width = width
        self.__height = height
        if title:
            self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.delete)

        self.center()
        self.grab_set()

    def delete(self):
        self.__parent.focus_set()
        self.destroy()

    def center(self):
        if self.__parent:
            x = self.__parent.winfo_x()
            y = self.__parent.winfo_y()
            w = self.__parent.winfo_width()
            h = self.__parent.winfo_height()
            self.geometry("%dx%d+%d+%d" % (
                self.__width, self.__height, x + w / 2 - self.__width / 2, y + h / 2 - self.__height / 2))
