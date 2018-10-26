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
import codecs
from json import load
from tkinter import IntVar, Label, Checkbutton, NE, Tk, W, Button, EW

from windows import GameWindow
from menus.MainMenuBar import MainMenuBar
from windows.Window import Window
from words_sets.WordsSets import WordsSets


class MainWindow(Window):
    var: list
    menu: MainMenuBar
    words_sets: WordsSets
    set_checkbutton: Checkbutton
    game_window: GameWindow

    def __init__(self, parent=None):
        Window.__init__(self, parent)
        self.root.protocol('WM_DELETE_WINDOW', self.ask_quit)
        select_label = Label(self, text='Select a set of word', anchor=NE)
        select_label.grid(column=0, columnspan=2)
        self.var = list()
        with codecs.open('sets/sets.json', 'r', encoding='utf-8') as sets:
            self.words_sets = WordsSets(load(sets))
            for words_set in self.words_sets.w_s_array:
                self.var.append(IntVar())
                self.set_checkbutton = Checkbutton(self,
                                                   text=words_set.get_name(),
                                                   variable=self.var[-1],
                                                   command=self.cb)
                self.set_checkbutton.grid(column=0, sticky=W)
        self.start_button = Button(self, text='Start Game', command=self.start)
        self.start_button.grid(column=0)
        self.menu = MainMenuBar(self)
        self.cb()
        self.root.config(menu=self.menu)

    def cb(self):
        if len([value for value in self.var if value.get() > 0]):
            self.menu.file_menu.entryconfig('Start Game', state='normal')
            self.start_button.config(state='normal')
        else:
            self.menu.file_menu.entryconfig('Start Game',
                                            state='disabled')
            self.start_button.config(state='disabled')

    def start(self):
        window = Tk()
        self.game_window = GameWindow.GameWindow(self, root=window)

    def save(self):
        self.words_sets.save()

    def ask_quit(self):
        self.save()
        Window.ask_quit(self)
