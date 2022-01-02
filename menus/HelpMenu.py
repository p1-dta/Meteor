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
import webbrowser
from tkinter import Menu


def callback():
    print('called the callback!')
    pass


def repository_redirect():
    webbrowser.open('https://github.com/Vikka/Meteor')


def issue_redirect():
    webbrowser.open('https://github.com/Vikka/Meteor/issues')


def trello_redirect():
    webbrowser.open('https://trello.com/b/BzJe34V1/Meteor')


class HelpMenu(Menu):
    def __init__(self) -> None:
        Menu.__init__(self)
        self.add_command(label='Getting Started', command=callback)
        self.add_separator()
        self.add_command(label='Github Repository',
                         command=repository_redirect)
        self.add_command(label='Report Problem', command=issue_redirect)
        self.add_command(label='Trello', command=trello_redirect)
        self.add_command(label='About', command=callback)
        # disable : Under construction
        self.entryconfig('Getting Started', state='disabled')
        self.entryconfig('About', state='disabled')
