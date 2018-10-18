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


class WordsSet:
    name: str
    first_language: str
    second_language: str
    words: list

    def __init__(self, word_set: dict) -> None:
        self.name = word_set['name']
        self.first_language = word_set['first_language']
        self.second_language = word_set['second_language']
        self.words = [a for a in word_set['words']]
        return

    def get_len(self) -> int:
        return len(self.words)

    def get_name(self) -> str:
        return '{}({} words)'.format(self.name, self.get_len())
        pass

    def iter_on_word(self, execute):
        [execute(word_dict) for word_dict in self.words]


class WordsSets:
    author: str
    w_s_array: list

    def __init__(self, words_sets: dict) -> None:
        self.author = words_sets["Author"]
        self.w_s_array = [WordsSet(words_set)
                          for words_set in words_sets["sets"]]
        return

    def get_len(self) -> int:
        return len(self.w_s_array)

    def iter_on_word(self, execute):
        [execute(elem) for elem in self.w_s_array]
