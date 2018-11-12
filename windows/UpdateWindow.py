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
import webbrowser
from functools import partial
from tkinter import Label, Frame, Button, E

from requests import Response

from windows.Window import Window


class UpdateWindow(Window):
    def __init__(self, response: Response, parent=None):
        Window.__init__(self, parent)
        tag_name = response.json()[0]['tag_name']
        name = response.json()[0]['name']
        release_author = response.json()[0]['author']['login']
        author_url = response.json()[0]['author']['url']
        update_lbl = Label(self, text='An update is available',
                           font=("TkDefaultFont", 16))
        name_lbl = Label(self, text='Release name: {}'.format(name),
                         font=("TkDefaultFont", 16))
        version_lbl = Label(self, text='Version: {}'.format(tag_name),
                            font=("TkDefaultFont", 16))
        release_aut_lbl = Label(self, text='Release Author: {}'
                                .format(release_author),
                                font=("TkDefaultFont", 16))
        update_lbl.grid(column=0)
        name_lbl.grid(column=0)
        version_lbl.grid(column=0)
        release_aut_lbl.grid(column=0)
        for asset in response.json()[0]['assets']:
            download_frame = Frame()
            file_name = asset['name']
            file_url = asset['browser_download_url']
            download_count = asset['download_count']
            file_name_lvl = Label(download_frame, text='{}'.format(file_name),
                                  font=("TkDefaultFont", 16))
            download_file = partial(webbrowser.open, file_url)
            download_btn = Button(download_frame, text='Download',
                                  command=download_file)
            download_count_lvl = Label(download_frame, text='Downloads: {}'
                                       .format(download_count),
                                       font=("TkDefaultFont", 16))
            file_name_lvl.grid(row=0, column=0)
            download_btn.grid(row=0, column=1)
            download_count_lvl.grid(row=0, column=2, sticky=E)
            download_frame.grid(column=0)
        parent.attributes("-topmost", True)

