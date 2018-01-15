from tkinter import *


class ToggleButton(Button):
    def __init__(self, parent, width=256, height=256, state=False):
        super().__init__(parent, relief=FLAT)

        self.__on_func = None
        self.__off_func = None

        self.__toggle_on_img = PhotoImage(file="Images/toggle-on.png")
        self.__toggle_off_img = PhotoImage(file="Images/toggle-off.png")
        if state == False:
            self.config(image=self.__toggle_off_img, command=self.__toggle)
        else:
            self.config(image=self.__toggle_on_img, command=self.__toggle)

        parent.bind('<Button-1>', self.__keep_flat)  # bind the application to left mouse click
        self.__state = state

    def set_on_callback(self, fn):
        self.__on_func = fn

    def set_off_callback(self, fn):
        self.__off_func = fn

    def __toggle(self):
        if self.__state:
            self.image = self.__toggle_off_img
            self.config(image=self.__toggle_off_img)
            self.__state = False
            if self.__off_func:
                self.__off_func()
        else:

            self.image = self.__toggle_on_img
            self.config(image=self.__toggle_on_img)
            self.__state = True
            if self.__on_func:
                self.__on_func()

    def __keep_flat(self, event):  # on click,
        if event.widget is self:  # if the click came from the button
            event.widget.config(relief=FLAT)  # enforce an option


if __name__ == "__main__":
    root = Tk()
    button = ToggleButton(root)
    button.pack()
    root.mainloop()
