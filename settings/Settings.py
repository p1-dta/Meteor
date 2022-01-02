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
from json import load, dump

SETTINGS_PATH = 'settings/settings.json'

with open(SETTINGS_PATH, encoding='utf-8') as settings_file:
    _raw_settings = load(settings_file)
repetition_limit = _raw_settings['repetition_limit']
time_limit = _raw_settings['time_limit']
mode = _raw_settings['mode']


def save():
    tmp_settings = {
        'repetition_limit': repetition_limit,
        'time_limit': time_limit,
        'mode': mode
    }
    with open(SETTINGS_PATH, 'w', encoding='utf-8') as settings_file:
        dump(tmp_settings, settings_file)
