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
import codecs
from json import dump, dumps

from words_sets.WordsSet import WordsSet


class WordsSets(list):
    def __init__(self, words: list) -> None:
        super().__init__([WordsSet(words_set) for words_set in words])

    def save(self):
        with codecs.open('sets/sets.json', 'w', encoding='utf-8') as outfile:
            dump(self, outfile, default=lambda o: o.__dict__, indent=2,
                 ensure_ascii=False)
