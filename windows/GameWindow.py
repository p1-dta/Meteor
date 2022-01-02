#
#     Meteor
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
from random import choices
from tkinter import Button, Label

from windows.Window import Window


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
        self.parent.menu.file_menu.entryconfig("Start",
                                               state='disabled')
        words_sample = list()
        words_weight = list()
        for it, value in enumerate(self.parent.var):
            if value.get():
                for it2, word in enumerate(
                        self.parent.words_sets[it].words):
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

    def first_turn(self):
        first_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets[self.words_choice[self.it][1]].first_language,
            self.words_choice[self.it][0].first)
        sec_lang_lbl_txt = '{} ?'.format(
            self.parent.words_sets[
                self.words_choice[self.it][1]].second_language)
        self.first_lang_lbl = Label(self, text=first_lang_lbl_txt,
                                    font=("TkDefaultFont", 20))
        self.scd_lang_lbl = Label(self, text=sec_lang_lbl_txt,
                                  font=("TkDefaultFont", 20))
        self.show_solution_btn = Button(self, text='Show solution',
                                        font=("TkDefaultFont", 12),
                                        command=self.show_solution)
        self.first_lang_lbl.grid(column=0)
        self.scd_lang_lbl.grid(column=0)
        self.show_solution_btn.grid(column=0)

    def show_solution(self):
        self.show_solution_btn.destroy()
        sec_lang_lbl_txt = '{} : {}'.format(
            self.parent.words_sets[self.words_choice[self.it][1]]
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
        self.parent.words_sets[self.words_choice[self.it][1]].words[
            self.words_choice[self.it][2]].weight -= \
            self.parent.words_sets[self.words_choice[
                self.it][1]].words[self.words_choice[self.it][2]].weight / 10
        self.it += 1
        if self.it < len(self.words_choice):
            self.next_turn()
        else:
            self.master.destroy()

    def incorrect(self):
        self.parent.words_sets[self.words_choice[self.it][1]].words[
            self.words_choice[self.it][2]]. \
            weight += (100 - self.parent.words_sets[self.words_choice[self.it][1]].
                       words[self.words_choice[self.it][2]].weight) / 10
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
            self.parent.words_sets[
                self.words_choice[self.it][1]].first_language,
            self.words_choice[self.it][0].first)
        sec_lang_lbl_txt = '{} ?'.format(
            self.parent.words_sets[
                self.words_choice[self.it][1]].second_language)
        self.first_lang_lbl = Label(self, text=first_lang_lbl_txt,
                                    font=("TkDefaultFont", 20))
        self.scd_lang_lbl = Label(self, text=sec_lang_lbl_txt,
                                  font=("TkDefaultFont", 20))
        self.show_solution_btn = Button(self, text='Show solution',
                                        font=("TkDefaultFont", 12),
                                        command=self.show_solution)
        self.first_lang_lbl.grid(column=0)
        self.scd_lang_lbl.grid(column=0)
        self.show_solution_btn.grid(column=0)

    def destroy(self):
        self.parent.menu.file_menu.entryconfig("Start",
                                               state='normal')
        Window.destroy(self)
        return
