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

from menus.EditLengthMenu import EditLengthMenu


class EditGameSettingMenu(Menu):
    edit_length_menu: EditLengthMenu

    def __init__(self):
        Menu.__init__(self)
        self.edit_length_menu = EditLengthMenu()
        self.add_cascade(label='Game Length', menu=self.edit_length_menu)
