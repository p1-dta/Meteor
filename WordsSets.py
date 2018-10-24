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
from json import load, dump

from WordsSet import WordsSet


class WordsSets:
    w_s_array: list

    def __init__(self, words_sets: dict) -> None:
        self.w_s_array = [WordsSet(words_set)
                          for words_set in words_sets["sets"]]
        return

    def get_len(self) -> int:
        return len(self.w_s_array)

    def save(self):
        save_words_sets = dict()
        save_words_sets['sets'] = list()
        for words_set in self.w_s_array:
            tmp_words_set = dict()
            tmp_words_set['name'] = words_set.name
            tmp_words_set['first_language'] = words_set.first_language
            tmp_words_set['second_language'] = words_set.second_language
            tmp_words_set['words'] = list()
            for words in words_set.words:
                tmp_words = dict()
                tmp_words['first'] = words.first
                tmp_words['second'] = words.second
                tmp_words['weight'] = words.weight
                tmp_words_set['words'].append(tmp_words)
            save_words_sets['sets'].append(tmp_words_set)
        with codecs.open('sets.json', 'w', encoding='utf-8') as outfile:
            dump(save_words_sets, outfile, ensure_ascii=False)
        return save_words_sets
