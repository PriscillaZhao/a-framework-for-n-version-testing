from typing import TextIO
from src.common import color_formatter


class Logger(object):
    """A logger object that logs to both a file and stdout."""

    # Properties

    indent_level = 0  # type: int
    indent_string = '    '  # type: str

    # Public methods

    def __init__(self, file_path: str):
        # exc.raise_if_falsy(file_path=file_path)

        self.file_path = file_path  # type: str
        self.file = None  # type: TextIO
        self.should_indent = False  # type: bool

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def log(self, message, color=None, is_end=True):
        """Logs a given message to both a file and stdout."""
        should_close = False

        if not self.file:
            self.open()
            should_close = True

        if self.should_indent:
            for _ in range(self.indent_level):
                color_formatter.ColorFormatter.pretty(self.indent_string, is_end=False, out_file=self.file)
                color_formatter.ColorFormatter.pretty(self.indent_string, is_end=False)

        color_formatter.ColorFormatter.pretty(message, is_end, out_file=self.file)
        color_formatter.ColorFormatter.pretty(message, color, is_end)

        self.should_indent = is_end

        if should_close:
            self.close()

    # Private methods

    def open(self):
        """Opens log file in append mode."""
        self.file = open(self.file_path, mode='a')

    def close(self):
        """Closes log file."""
        if self.file:
            self.file.close()
            self.file = None
