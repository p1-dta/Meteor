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
from words_sets.Word import Word


class WordsSet:
    name: str
    first_language: str
    second_language: str
    words: list

    def __init__(self, word_set: dict) -> None:
        self.name = word_set['name']
        self.first_language = word_set['first_language']
        self.second_language = word_set['second_language']
        self.words = [Word(word) for word in word_set['words']]
        return

    def get_len(self) -> int:
        return len(self.words)

    def get_name(self) -> str:
        return '{}({} words)'.format(self.name, self.get_len())
        pass