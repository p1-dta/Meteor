#
#     Meteor
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
import webbrowser
from functools import partial
from tkinter import Label, Frame, Button, E, Listbox, Scrollbar, S, N, Canvas, \
    W, NW, TclError

from requests import Response

from windows.Window import Window


class AutoScrollbar(Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)

    @staticmethod
    def pack(**kw):
        print("cannot use pack with this widget")
        raise TclError

    @staticmethod
    def place(**kw):
        print("cannot use place with this widget")
        raise TclError


class UpdateWindow(Window):
    def __init__(self, response: Response, parent=None):
        Window.__init__(self, parent)

        name = response.json()[0]['name']
        html_url = response.json()[0]['html_url']

        release_name_lbl = Label(self, text=name)
        download_file = partial(webbrowser.open, html_url)
        download_btn = Button(self,
                              text='downloads',
                              command=download_file)
        update_lbl = Label(self, text='An update is available:',
                           font=("TkDefaultFont", 14))

        update_lbl.grid(column=0)
        release_name_lbl.grid(row=1, column=0, sticky=W)
        download_btn.grid(row=1, column=2, sticky=W)
        parent.attributes("-topmost", True)
