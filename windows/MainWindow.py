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
from tkinter import IntVar, Label, Checkbutton, NE, Tk, W, Button

import requests

from menus.MainMenuBar import MainMenuBar
from settings.Settings import Settings
from version.Version import Version
from windows import GameWindow
from windows.UpdateWindow import UpdateWindow
from windows.Window import Window
from words_sets.WordsSets import WordsSets


class MainWindow(Window):
    var: list
    menu: MainMenuBar
    words_sets: WordsSets
    set_checkbutton: Checkbutton
    game_window: GameWindow
    soft_update_win: UpdateWindow
    settings: Settings

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
        self.settings = Settings()
        with codecs.open('version/version.json', 'r', encoding='utf-8')\
                as version:
            self.version = Version(load(version))
        self.start_button = Button(self, text='Start Game', command=self.start)
        self.start_button.grid(column=0)
        self.menu = MainMenuBar(self)
        self.cb()
        self.root.config(menu=self.menu)
        self.software_update()

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

    def software_update(self):
        url = 'https://api.github.com/repos/Vikka/ChiTrain/releases'
        try:
            response = requests.get(url, timeout=2)
        except requests.exceptions.Timeout:
            print('timeout')
            return()
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            print('toomanyredirect')
            return ()
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            print('requestexception')
            print(e)
            return ()

        if response.status_code == 200:
            if response.json()[0]['tag_name'] != self.version.version_num:
                self.soft_update_win = UpdateWindow(response, Tk())
            else:
                print('same version' + self.version.version_num)
