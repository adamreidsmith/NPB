# Valid text and background colors
_VALID_COLORS = {
    'black': ('\033[30m', '\033[40m'),
    'red': ('\033[31m', '\033[41m'),
    'green': ('\033[32m', '\033[42m'),
    'yellow': ('\033[33m', '\033[43m'),
    'blue': ('\033[34m', '\033[44m'),
    'magenta': ('\033[35m', '\033[45m'),
    'cyan': ('\033[36m', '\033[46m'),
    'white': ('\033[37m', '\033[47m'),
}
_RESET_TF = '\033[0m'  # Resets the typeface to its default
_RAINBOW = tuple(_VALID_COLORS[c][0] for c in ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta'))
