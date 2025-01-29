#  Copyright 2025 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import tkinter as tk
from time import strftime
from tkinter.font import Font


class DigitalClock:
    """
    Digital Clock Graphical User Interface
    """

    __label: tk.Label
    """
    The clock label
    """

    __master: tk.Tk
    """
    The main window
    """

    def __init__(self, master: tk.Tk):
        """
        Initializes the Digital Clock

        :param master: the main window
        """
        self.__master = master
        self.__master.title(string="Digital Clock")
        self.__master.configure(background="white")
        self.__master.geometry(newGeometry="300x100")
        self.__master.resizable(width=False, height=False)

        self.__label = tk.Label(
            master=self.__master,
            background="white",
            foreground="black",
            font=Font(size=30, family="ariel", weight="bold"),
            relief="flat"
        )
        self.__label.place(x=20, y=20)
        self.update()

    # noinspection PyTypeChecker
    def update(self) -> None:
        """
        Updates the time

        :return: None - "void" function
        """
        current_time: str = strftime("%H: %M: %S\n %m-%d-%Y")
        self.__label.configure(text=current_time)
        self.__label.after(ms=80, func=self.update)
        self.__label.pack(anchor="center")


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    DigitalClock(root)
    root.mainloop()
