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
from webbrowser import open

import Window
import WordsSets


def callback():
    print('called the callback!')
    pass


def repository_redirect():
    open('https://github.com/Vikka/ChiTrain')


def issue_redirect():
    open('https://github.com/Vikka/ChiTrain/issues')


def import_pack():
    pass


def export_pack():
    pass


class FileMenu(Menu):
    def __init__(self, window) -> None:
        Menu.__init__(self)
        self.add_command(label='New Set', command=callback)
        self.add_command(label='Import Set Pack', command=import_pack)
        self.add_command(label='Export Set Pack', command=export_pack)
        self.add_separator()
        self.add_command(label='Settings', command=callback)
        self.add_separator()
        self.add_command(label='Exit', command=window.ask_quit)
        return


class EditMenu(Menu):
    main_menu: Menu
    window: Window
    show_set_menu: Menu
    edit_set_menu: Menu

    def __init__(self, main_menu) -> None:
        Menu.__init__(self)
        self.main_menu = main_menu
        self.window = main_menu.parent
        self.show_set_menu = Menu(self)
        self.add_cascade(label='Show Sets', menu=self.show_set_menu)
        self.edit_set_menu = Menu(self)
        self.add_cascade(label='Edit Sets', menu=self.edit_set_menu)
        self.update_menu()

    def update_menu(self) -> None:
        if self.window.words_sets == 0:
            self.entryconfig('Show Sets', state='disabled')
            self.entryconfig('Edit Sets', state='disabled')
        else:
            self.entryconfig('Show Sets', state='normal')
            self.entryconfig('Edit Sets', state='normal')
            self.window.words_sets.iter_on_word(self.func_example)
        return

    def func_example(self, a):
        p_show = partial(self.create_set_window, a,
                         Window.SHOW_SET_WINDOW)
        p_edit = partial(self.create_set_window, a,
                         Window.EDIT_SET_WINDOW)
        self.show_set_menu.add_cascade(label=a.get_name(),
                                       command=p_show)
        self.edit_set_menu.add_cascade(label=a.get_name(),
                                       command=p_edit)

    def create_set_window(self, word_set: WordsSets, window_type: int):
        window = Tk()
        Window.SetWindow(self, word_set, window_type, window)
        return


class HelpMenu(Menu):
    def __init__(self) -> None:
        Menu.__init__(self)
        self.add_command(label='Getting Started', command=callback)
        self.add_separator()
        self.add_command(label='Github Repository',
                         command=repository_redirect)
        self.add_command(label='Report Problem', command=issue_redirect)
        self.add_command(label='About', command=callback)


class MainMenuBar(Menu):
    parent: Window
    file_menu: FileMenu
    edit_menu: EditMenu
    help_menu: HelpMenu

    def __init__(self, parent: Window) -> None:
        Menu.__init__(self)
        self.parent = parent
        self.file_menu = FileMenu(self.parent)
        self.edit_menu = EditMenu(self)
        self.help_menu = HelpMenu()
        self.add_cascade(label='File', menu=self.file_menu)
        self.add_cascade(label='Edit', menu=self.edit_menu)
        self.add_cascade(label='Help', menu=self.help_menu)
        return
