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
from random import choices
from tkinter import IntVar, Label, Checkbutton, NE, Frame, Menu, StringVar, \
    Entry, Tk, Button
from tkinter.messagebox import askokcancel

from MainMenuBar import MainMenuBar, EditMenu
from WordsSets import WordsSet, WordsSets


class Window(Frame):
    root: Tk

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.pack(self)
        self.root = parent

    def ask_quit(self):
        if askokcancel("Quit", "You want to quit now?"):
            self.quit()


class GameWindow(Window):
    words_choice: list
    show_solution_btn: Button
    scd_lang_lbl: Label
    correct_btn: Button

    def __init__(self, parent, root=None):
        Window.__init__(self, root)
        self.parent = parent
        words_sample = list()
        words_weight = list()
        for it, value in enumerate(self.parent.var):
            if value.get():
                for word in self.parent.words_sets.w_s_array[it].words:
                    print(word.second)
                    words_sample.append((word, it))
                    if len(words_weight) > 0:
                        words_weight.append(words_weight[-1] + word.weight)
                    else:
                        words_weight.append(word.weight)
        self.words_choice = choices(words_sample, cum_weights=words_weight,
                                    k=self.parent.menu.edit_menu.
                                    edit_game_settings_menu.edit_length_menu.
                                    game_length.get())
        self.it = 0
        self.next_turn()
        print(words_sample)
        print(words_weight)
        # for words in self.parent.words_sets.ws_array
        # weight = sum()
        # self.root.var

    def next_turn(self):
        first_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets.w_s_array[self.words_choice[self.it][1]].
                first_language, self.words_choice[self.it][0].first)
        sec_lang_lbl_txt = '{} ?'.format(
            self.parent.words_sets.w_s_array[self.words_choice[self.it][1]].
                second_language)
        first_lang_lbl = Label(self, text=first_lang_lbl_txt,
                               font=("TkDefaultFont", 12))
        self.scd_lang_lbl = Label(self, text=sec_lang_lbl_txt,
                                  font=("TkDefaultFont", 12))
        self.show_solution_btn = Button(self, text='Show solution',
                                        font=("TkDefaultFont", 12),
                                        command=self.show_solution)
        first_lang_lbl.grid(column=0)
        self.scd_lang_lbl.grid(column=0)
        self.show_solution_btn.grid(column=0)
        print(self.words_choice[self.it])

    def show_solution(self):
        self.show_solution_btn.destroy()
        sec_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets.w_s_array[self.words_choice[self.it][1]]
                .second_language, self.words_choice[self.it][0].second)
        self.scd_lang_lbl.config(text=sec_lang_lbl_txt)
        self.it += 1
        self.correct_btn = Button(self, text='Correct',
                                  font=("TkDefaultFont", 12),
                                  command=self.correct)

    def correct(self):
        pass


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
        with codecs.open('sets.json', 'r', encoding='utf-8') as sets:
            self.words_sets = WordsSets(load(sets))
            for words_set in self.words_sets.w_s_array:
                self.var.append(IntVar())
                self.set_checkbutton = Checkbutton(self,
                                                   text=words_set.get_name(),
                                                   variable=self.var[-1],
                                                   command=self.cb)
                self.set_checkbutton.grid(column=0)
        self.menu = MainMenuBar(self)
        self.root.config(menu=self.menu)

    def cb(self):
        print('variable is {}'.format(list(map(lambda i: i.get(), self.var))))

    def start(self):
        window = Tk()
        self.game_window = GameWindow(self, root=window)
        print('start')
        pass


class SetWindow(Window):
    menu: Menu
    words_set: WordsSet

    def __init__(self, edit_menu: EditMenu, words_set: WordsSet,
                 parent=None, ):
        Window.__init__(self, parent)
        self.window = parent
        self.edit_menu = edit_menu
        self.words_set = words_set
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
        for word in words_set.words:
            frame = Frame(self)
            frame.grid(column=0, columnspan=2)
            first_text_variable = StringVar()
            second_text_variable = StringVar()
            word_entry_left = Entry(frame,
                                    textvariable=first_text_variable)
            word_entry_left.grid(row=0, column=0)
            word_entry_right = Entry(frame,
                                     textvariable=second_text_variable)
            word_entry_right.grid(row=0, column=1)
            word_entry_left.insert(0, word.first)
            word_entry_right.insert(0, word.second)

    def destroy(self):
        print('test')
        self.menu.entryconfig(self.words_set.get_name(),
                              state='normal')
        Window.destroy(self)
        return
