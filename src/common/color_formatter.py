import sys
from typing import TextIO


class ColorFormatter:
    """Output color."""
    GRAY = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    CRIMSON = 38

# Public functions

    def pretty(text, has_color=None, is_bold=False, is_end=True, out_file: TextIO=sys.stdout):
        """Print colored message to the specified file."""

        if out_file.isatty():
            attrs = []

            if has_color:
                attrs.append(str(has_color.value))

            if is_bold:
                attrs.append('1')

            if len(attrs) > 0:
                message = u'\x1b[{}m{}\x1b[0m'.format(';'.join(attrs), text)

        if is_end:
            print(text, file=out_file)
        else:
            print(text, file=out_file, end='')
            out_file.flush()

    def info(text, is_end=True) -> None:
        """Print message to stdout."""
        ColorFormatter.pretty(text, is_end)

    def success(text, is_end=True) -> None:
        """Print message in green to stdout."""
        ColorFormatter.pretty(text, ColorFormatter.GREEN, is_end)

    def error(text, is_end: bool=True) -> None:
        """Print message in red to stderr."""
        ColorFormatter.pretty(text, ColorFormatter.RED, is_end, sys.stderr)