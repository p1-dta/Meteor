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
    Entry, Tk, Button, EW
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
    incorrect_btn: Button
    first_lang_lbl: Label

    def __init__(self, parent, root=None):
        Window.__init__(self, root)
        self.parent = parent
        self.parent.menu.file_menu.entryconfig("Start Game",
                                               state='disabled')
        words_sample = list()
        words_weight = list()
        for it, value in enumerate(self.parent.var):
            if value.get():
                for it2, word in enumerate(
                        self.parent.words_sets.w_s_array[it].words):
                    print(word.second)
                    words_sample.append((word, it, it2))
                    if len(words_weight) > 0:
                        words_weight.append(words_weight[-1] + word.weight)
                    else:
                        words_weight.append(word.weight)
        self.words_choice = choices(words_sample, cum_weights=words_weight,
                                    k=self.parent.menu.edit_menu.
                                    edit_game_settings_menu.edit_length_menu.
                                    game_length.get())
        self.it = 0
        self.first_turn()
        print(words_sample)
        print(words_weight)
        # for words in self.parent.words_sets.ws_array
        # weight = sum()
        # self.root.var

    def first_turn(self):
        first_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets.w_s_array[
                self.words_choice[self.it][1]].first_language,
            self.words_choice[self.it][0].first)
        sec_lang_lbl_txt = '{} ?'.format(
            self.parent.words_sets.w_s_array[
                self.words_choice[self.it][1]].second_language)
        self.first_lang_lbl = Label(self, text=first_lang_lbl_txt,
                                    font=("TkDefaultFont", 12))
        self.scd_lang_lbl = Label(self, text=sec_lang_lbl_txt,
                                  font=("TkDefaultFont", 12))
        self.show_solution_btn = Button(self, text='Show solution',
                                        font=("TkDefaultFont", 12),
                                        command=self.show_solution)
        self.first_lang_lbl.grid(column=0)
        self.scd_lang_lbl.grid(column=0)
        self.show_solution_btn.grid(column=0)
        print(self.words_choice[self.it])

    def show_solution(self):
        self.show_solution_btn.destroy()
        sec_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets.w_s_array[self.words_choice[self.it][1]]
                .second_language, self.words_choice[self.it][0].second)
        self.scd_lang_lbl.config(text=sec_lang_lbl_txt)
        self.correct_btn = Button(self, text='Correct',
                                  font=("TkDefaultFont", 12),
                                  command=self.correct)
        self.incorrect_btn = Button(self, text='False',
                                    font=("TkDefaultFont", 12),
                                    command=self.incorrect)
        self.correct_btn.grid(column=0)
        self.incorrect_btn.grid(column=0)

    def correct(self):
        self.parent.words_sets.w_s_array[self.words_choice[self.it][1]].words[
            self.words_choice[self.it][2]].weight -= \
            self.parent.words_sets.w_s_array[self.words_choice[
                self.it][1]].words[self.words_choice[self.it][2]].weight / 10
        print(int(self.parent.words_sets.w_s_array[
                      self.words_choice[self.it][1]].words[
                      self.words_choice[self.it][2]].weight))
        self.it += 1
        if self.it < len(self.words_choice):
            self.next_turn()
        else:
            self.master.destroy()

    def incorrect(self):
        self.parent.words_sets.w_s_array[self.words_choice[self.it][1]].words[
            self.words_choice[self.it][2]]. \
            weight += (100 - self.parent.words_sets.
                       w_s_array[self.words_choice[self.it][1]].
                       words[self.words_choice[self.it][2]].weight) / 10
        print(int(self.parent.words_sets.w_s_array[
                      self.words_choice[self.it][1]].words[
                      self.words_choice[self.it][2]].weight))
        self.it += 1
        if self.it < len(self.words_choice):
            self.next_turn()
        else:
            self.master.destroy()

    def next_turn(self):
        self.correct_btn.destroy()
        self.incorrect_btn.destroy()
        self.scd_lang_lbl.destroy()
        self.first_lang_lbl.destroy()
        first_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets.w_s_array[
                self.words_choice[self.it][1]].first_language,
            self.words_choice[self.it][0].first)
        sec_lang_lbl_txt = '{} ?'.format(
            self.parent.words_sets.w_s_array[
                self.words_choice[self.it][1]].second_language)
        self.first_lang_lbl = Label(self, text=first_lang_lbl_txt,
                                    font=("TkDefaultFont", 12))
        self.scd_lang_lbl = Label(self, text=sec_lang_lbl_txt,
                                  font=("TkDefaultFont", 12))
        self.show_solution_btn = Button(self, text='Show solution',
                                        font=("TkDefaultFont", 12),
                                        command=self.show_solution)
        self.first_lang_lbl.grid(column=0)
        self.scd_lang_lbl.grid(column=0)
        self.show_solution_btn.grid(column=0)
        print(self.words_choice[self.it])

    def destroy(self):
        print('TEST DESTRUCTION')
        self.parent.menu.file_menu.entryconfig("Start Game",
                                               state='normal')
        Window.destroy(self)
        return


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
        self.cb()
        self.root.config(menu=self.menu)

    def cb(self):
        if len([value for value in self.var if value.get() > 0]):
            self.menu.file_menu.entryconfig("Start Game", state='normal')
            print('true')
        else:
            self.menu.file_menu.entryconfig("Start Game",
                                            state='disabled')
            print('false')
        print('variable is {}'.format(list(map(lambda i: i.get(), self.var))))

    def start(self):
        window = Tk()
        self.game_window = GameWindow(self, root=window)

    def save(self):
        print('save')
        self.words_sets.save()

    def ask_quit(self):
        self.save()
        askokcancel(self)


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
        first_lang_lbl = Label(self, text=words_set.first_language)
        sec_lang_lbl = Label(self, text=words_set.second_language)
        weight_lang_lbl = Label(self, text='Weight')
        first_lang_lbl.grid(row=0, column=0)
        sec_lang_lbl.grid(row=0, column=1)
        weight_lang_lbl.grid(row=0, column=2)
        for word in words_set.words:
            frame = Frame(self)
            frame.grid(column=0, columnspan=3)
            first_txt_var = StringVar()
            sec_txt_var = StringVar()
            weight_txt_var = StringVar()
            word_entry_left = Entry(frame,
                                    textvariable=first_txt_var)
            word_entry_left.grid(row=0, column=0)
            word_entry_right = Entry(frame,
                                     textvariable=sec_txt_var)
            word_entry_right.grid(row=0, column=1)
            word_entry_weight = Entry(frame,
                                      textvariable=weight_txt_var)
            word_entry_weight.grid(row=0, column=2)
            word_entry_left.insert(0, word.first)
            word_entry_right.insert(0, word.second)
            word_entry_weight.insert(0, word.weight)

        save_btn = Button(self, text='Save',
                          command=self.edit_menu.window.save)
        save_btn.grid(column=0, columnspan=3, sticky=EW)

    def destroy(self):
        self.menu.entryconfig(self.words_set.get_name(),
                              state='normal')
        Window.destroy(self)
        return
