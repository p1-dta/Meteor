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

from Singleton import Singleton


class Settings(metaclass=Singleton):
    repetition_limit: int
    time_limit: int
    mode: int

    def __init__(self):
        with codecs.open('settings/settings.json', 'r', encoding='utf-8')\
                as settings:
            raw_settings = load(settings)
        self.repetition_limit = raw_settings['repetition_limit']
        self.time_limit = raw_settings['time_limit']
        self.mode = raw_settings['mode']
