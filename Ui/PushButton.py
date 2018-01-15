import time
from threading import Thread, Lock
from tkinter import *


class PushButton(Button):
    def __init__(self, parent, text=None, image=None):
        super().__init__(parent, text=text, image=image)
        self.__thread = None
        self.__lock = Lock()
        self.__started = False
        self.__running = False
        self.__on_press = None
        self.__on_release = None
        self.__refresh_delay = 0.0001  # 1 µs
        self.__set_up(self.on_up)
        self.__set_down(self.on_down)
        self.set_press(self.__on_press)

    def __set_down(self, *fn):
        self.bind('<Button-1>', *fn)

    def __set_up(self, *fn):
        self.bind('<ButtonRelease-1>', *fn)

    def set_press(self, fn):
        self.__on_press = fn

    def set_release(self, fn):
        self.__on_release = fn

    def on_down(self, *x):
        self.__start()

    def on_up(self, *x):
        self.__stop()
        if self.__on_release:
            self.__on_release()

    def __run(self):
        self.__lock.acquire()
        self.__started = True
        started = self.__started
        self.__running = True
        self.__lock.release()
        while (started):
            with self.__lock:
                started = self.__started
            if self.__on_press:
                self.__on_press()
            time.sleep(self.__refresh_delay)

        self.__lock.acquire()
        self.__running = False
        self.__lock.release()

    def __on_press(self):
        print("press")

    def __stop(self):
        self.__lock.acquire()
        self.__started = False
        self.__lock.release()
        if self.__thread:
            self.__thread.join()
            self.__thread = None

    def __start(self):
        with self.__lock:
            running = self.__running
        if not running:
            self.__thread = Thread(target=self.__run)
            self.__thread.start()
