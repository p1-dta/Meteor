#
#     ChiTrain
#     Copyright (C) 2018 Dorian Turba
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from tkinter import Frame, Tk
from tkinter.messagebox import askokcancel


class Window(Frame):
    root: Tk

    def __init__(self, parent=None):
        super().__init__(parent)
        Frame.pack(self)
        self.root = parent

    def askokcancel(self):
        if askokcancel("Quit", "You want to quit now?"):
            self.quit()


