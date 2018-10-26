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
from tkinter import Menu, IntVar


class EditLengthMenu(Menu):
    game_length: IntVar

    def __init__(self):
        Menu.__init__(self)
        self.game_length = IntVar(None, 10)
        self.add_radiobutton(label="10 words (default)",
                             value=10,
                             variable=self.game_length)
        self.add_radiobutton(label="25 words",
                             value=25,
                             variable=self.game_length)
        self.add_radiobutton(label="50 words",
                             value=50,
                             variable=self.game_length)
