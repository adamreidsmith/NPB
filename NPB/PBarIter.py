import time
from typing import Optional, Any
from collections.abc import Iterable

from config import _VALID_COLORS


class PBarIter:
    '''A helper class that wraps the supplied iterators to track iteration times.'''

    def __init__(
        self,
        iterable: Iterable,
        length: Optional[int],
        desc: Optional[str],
        fill_char: str,
        ncols: Optional[int],
        text_color: Optional[str],
        bg_color: Optional[str],
        rainbow: bool,
        options_dict: dict,
    ) -> None:

        # Validate the iterable
        try:
            self._iterator = iter(iterable)
        except (TypeError, AttributeError):
            raise TypeError(f'\'{type(iterable).__name__}\' object is not iterable')

        # Compute the length if possible
        self._len = None
        try:
            self._len = len(iterable)
        except (TypeError, AttributeError):
            if length is not None:
                try:
                    self._len = int(length)
                except Exception:
                    raise TypeError('\'length\' must be a non-negative integer')

        # Validate the description
        self._desc = desc
        if self._desc is not None:
            if not isinstance(self._desc, str):
                raise TypeError('\'desc\' must be a string')
            if len(self._desc) == 0:
                self._desc = None

        # Validate the fill character
        self._fill_char = fill_char
        if not isinstance(self._fill_char, str):
            raise TypeError('\'fill_char\' must be a string of length one')
        if len(self._fill_char) != 1:
            raise ValueError('\'fill_char\' must be a string of length one')

        # Validate ncols
        if ncols is not None:
            try:
                ncols = int(ncols)
            except Exception:
                raise TypeError('If specified, \'ncols\' must be an integer')
        self._ncols = ncols

        # Validate text_color
        if text_color is not None and text_color not in _VALID_COLORS:
            raise ValueError(f'\'text_color\' must be a string in {set(_VALID_COLORS.keys())}')
        self._text_color = _VALID_COLORS[text_color][0] if text_color is not None else None

        # Validate bg_color
        if bg_color is not None and bg_color not in _VALID_COLORS:
            raise ValueError(f'\'bg_color\' must be a string in {set(_VALID_COLORS.keys())}')
        self._bg_color = _VALID_COLORS[bg_color][1] if bg_color is not None else None

        # Validate rainbow
        self._rainbow = rainbow
        if not isinstance(self._rainbow, bool):
            raise TypeError('\'rainbow\' must be a boolean')

        # Validate the options dictionary
        self._options_dict = options_dict
        if any(not isinstance(opt, bool) for opt in options_dict.values()):
            raise TypeError('Only boolean values are accepted for option arguments')

        self._time_of_current_it: float = None
        self._it_time_delta: float = None
        self._start_time: float = None
        self._current_index: int = -1

    def __len__(self) -> int | None:
        return self._len

    def __iter__(self) -> 'PBarIter':
        self._current_index = -1
        self._it_time_delta = None
        self._start_time = None
        self._time_of_current_it = None
        return self

    def __next__(self) -> Any:
        raise_se = False
        try:
            next_item = next(self._iterator)
        except StopIteration:
            raise_se = True

        curr_time = time.perf_counter()
        if self._time_of_current_it is not None:
            self._it_time_delta = curr_time - self._time_of_current_it
        self._time_of_current_it = curr_time
        if self._start_time is None:
            self._start_time = curr_time

        self._current_index += 1

        if raise_se:
            raise StopIteration

        return next_item
