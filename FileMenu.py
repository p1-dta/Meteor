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


def callback():
    print('called the callback!')
    pass


def import_pack():
    print('called the import!')
    pass


def export_pack():
    print('called the export!')
    pass


class FileMenu(Menu):
    def __init__(self, window) -> None:
        Menu.__init__(self)
        self.add_command(label='Start Game', command=window.start)
        self.add_command(label='Restart Game', command=callback)
        self.add_command(label='Stop Game', command=callback)
        self.add_separator()
        self.add_command(label='New Set', command=callback)
        self.add_command(label='Import Set Pack', command=import_pack)
        self.add_command(label='Export Set Pack', command=export_pack)
        self.add_separator()
        self.add_command(label='Settings', command=callback)
        self.add_separator()
        self.add_command(label='Exit', command=window.ask_quit)
        return
