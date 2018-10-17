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
from json import load
from tkinter import IntVar, Label, Checkbutton, Button, NE, Frame, EW, \
    Menu, StringVar, Entry, Tk
from tkinter.messagebox import askokcancel
from tkinter.ttk import Separator

from MainMenuBar import MainMenuBar, EditMenu
from WordsSets import WordsSet, WordsSets

SHOW_SET_WINDOW: str = '_show_set_window_'
EDIT_SET_WINDOW: str = '_edit_set_window_'


class Window(Frame):
    root: Tk

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.pack(self)
        self.root = parent

    def ask_quit(self):
        if askokcancel("Quit", "You want to quit now?"):
            self.quit()


class MainWindow(Window):
    var: list
    menu: MainMenuBar
    words_sets: WordsSets
    set_checkbutton: Checkbutton

    def __init__(self, parent=None):
        Window.__init__(self, parent)
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        select_label = Label(self, text='Select a set of word', anchor=NE)
        select_label.grid(column=0, columnspan=2)
        self.var = list()
        with open('sets.json', 'r') as sets:
            self.words_sets = WordsSets(load(sets))
            self.words_sets.iter_on_word(self.func_test)
        self.menu = MainMenuBar(self)
        self.root.config(menu=self.menu)

    def func_test(self, a):
        self.var.append(IntVar())
        self.set_checkbutton = Checkbutton(self,
                                           text=a.get_name(),
                                           variable=self.var[-1],
                                           command=self.cb)
        self.set_checkbutton.grid(column=0)

    def cb(self):
        print('variable is {}'.format(list(map(lambda i: i.get(), self.var))))

    def start(self):
        print('start')
        pass


class SetWindow(Window):
    menu: Menu
    words_set: WordsSet

    def __init__(self, edit_menu: EditMenu, words_set: WordsSet,
                 window_type: int, parent=None, ):
        Window.__init__(self, parent)
        self.window = parent
        self.edit_menu = edit_menu
        self.words_set = words_set
        self.window_type = window_type
        if window_type == SHOW_SET_WINDOW:
            edit_menu.show_set_menu.entryconfig(words_set.get_name(),
                                                state='disabled')
            self.menu = edit_menu.show_set_menu
        elif window_type == EDIT_SET_WINDOW:
            edit_menu.edit_set_menu.entryconfig(words_set.get_name(),
                                                state='disabled')
            self.menu = edit_menu.edit_set_menu
        self.master.title(words_set.get_name())
        first_language_label = Label(self,
                                     text=words_set.first_language)
        second_language_label = Label(self,
                                      text=words_set.second_language)
        first_language_label.grid(row=0, column=0)
        second_language_label.grid(row=0, column=1)
        if window_type == SHOW_SET_WINDOW:
            separator = Separator(self)
            separator.grid(row=1, column=1, sticky="we")
        self.words_set.iter_on_word(self.func_iter)

    def func_iter(self, a):
        if self.window_type == SHOW_SET_WINDOW:
            frame = Frame(self)
            frame.grid(column=0, columnspan=2)
            print(a)
            word_label_left = Label(frame, text=a['first'])
            word_label_left.grid(row=0, column=0)
            word_label_right = Label(frame, text=a['second'])
            word_label_right.grid(row=0, column=1)
        elif self.window_type == EDIT_SET_WINDOW:
            first_text_variable = StringVar()
            second_text_variable = StringVar()
            word_entry_left = Entry(self,
                                    textvariable=first_text_variable)
            word_entry_left.grid(row=it + 1, column=0)
            word_entry_right = Entry(self,
                                     textvariable=second_text_variable)
            word_entry_right.grid(row=it + 1, column=1)
            word_entry_left.insert(0, a['first'])
            word_entry_right.insert(0, a['second'])

    def destroy(self):
        print('test')
        self.menu.entryconfig(self.words_set.get_name(),
                              state='normal')
        Window.destroy(self)
        return


class GameWindow(Window):
    def __init__(self, parent=None):
        Window.__init__(self, parent)
        return
