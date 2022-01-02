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
from functools import partial
from tkinter import Menu, Tk

from windows import Window, SetWindow
from words_sets import WordsSets
from menus.EditGameSettingMenu import EditGameSettingMenu


class EditMenu(Menu):
    main_menu: Menu
    window: Window
    show_set_menu: Menu
    edit_set_menu: Menu
    edit_game_settings_menu: EditGameSettingMenu

    def __init__(self, main_menu) -> None:
        Menu.__init__(self)
        self.main_menu = main_menu
        self.window = main_menu.parent
        self.edit_set_menu = Menu(self)
        self.edit_game_settings_menu = EditGameSettingMenu()
        self.add_cascade(label='Edit Sets', menu=self.edit_set_menu)
        self.add_cascade(label='Edit Game Settings',
                         menu=self.edit_game_settings_menu)
        self.update_menu()

    def update_menu(self) -> None:
        if self.window.words_sets == 0:
            self.entryconfig('Edit Sets', state='disabled')
            return

        self.entryconfig('Edit Sets', state='normal')
        for words_set in self.window.words_sets:
            p_edit = partial(self.create_set_window, words_set)
            self.edit_set_menu.add_cascade(label=words_set.get_name(),
                                           command=p_edit)

    def create_set_window(self, word_set: WordsSets):
        window = Tk()
        SetWindow.SetWindow(self, word_set, window)
        return
