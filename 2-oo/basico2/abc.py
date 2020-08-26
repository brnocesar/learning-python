from abc import ABC

from collections.abc import MutableSequence
from numbers import Complex

class Playlist(MutableSequence):
    pass

# filmes = Playlist()
# Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert


class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

# filmes = Numero()
# Can't instantiate abstract class NumberSeries with abstract methods __abs__, __add__, __complex__, __eq__, __mul__, __neg__, __pos__, __pow__, __radd__, __rmul__, __rpow__, __rtruediv__, __truediv__, conjugate, imag, real