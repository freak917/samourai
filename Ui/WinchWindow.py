from tkinter import *
from tkinter.ttk import *

from Ui.ToggleButton import ToggleButton
from Ui.ToplevelModal import ToplevelModal


class WinchWindow(ToplevelModal):
    def __init__(self, parent):
        super().__init__(parent, title="Treuil")
        label = Label(self, text="Activer : ")
        label.grid(row=1, column=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        button = ToggleButton(self)
        button.grid(row=1, column=2)

    def build_enable_button(self):
        pass


if __name__ == "__main__":
    root = Tk()
    window = WinchWindow(root)
    # window.show()
    root.wait_window(window)
    # root.mainloop()
