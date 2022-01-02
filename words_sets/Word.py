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
from dataclasses import dataclass


@dataclass
class Word:
    first: str
    second: str
    weight: int

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.__dict__}>'

    def __str__(self):
        return f'{self.__class__.__name__}: ({", ".join((str(v) for v in self.__dict__.values()))})'
