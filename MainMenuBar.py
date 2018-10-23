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
from tkinter import Menu

import EditMenu
import FileMenu
import HelpMenu
import Window


class MainMenuBar(Menu):
    parent: Window
    file_menu: FileMenu
    edit_menu: EditMenu
    help_menu: HelpMenu

    def __init__(self, parent: Window) -> None:
        Menu.__init__(self)
        self.parent = parent
        self.file_menu = FileMenu.FileMenu(self.parent)
        self.edit_menu = EditMenu.EditMenu(self)
        self.help_menu = HelpMenu.HelpMenu()
        self.add_cascade(label='File', menu=self.file_menu)
        self.add_cascade(label='Edit', menu=self.edit_menu)
        self.add_cascade(label='Help', menu=self.help_menu)
        return
