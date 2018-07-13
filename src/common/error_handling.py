import errno
import os
import sys

from enum import Enum
from typing import Any, Optional


class FileType(Enum):
    """File type."""
    ANY = 0
    FILE = 1
    DIR = 2


class ProgramExit(Exception):
    """Raise to express the will to exit from the program."""
    pass


def raise_exit(message):
    """Raise a ProgramExit with the specified message."""
    raise ProgramExit(message)


def raise_io_error(err_no: int, path: Optional[str]=None, message: Optional[str]=None):
    """Raise an IOError with an auto-generated message based on err_no."""
    if not message:
        message = os.strerror(err_no) + '.'

    if path:
        message += ' Path: ' + path

    e = IOError(message)
    e.errno = err_no

    raise e


def raise_not_found(path: Optional[str]=None, message: Optional[str]=None):
    """Raise a 'file not found' exception."""
    raise_io_error(errno.ENOENT, path, message)


def raise_if_none(**kwargs: Any) -> None:
    """Raise exception if any of the args is None."""
    for key in kwargs:
        if kwargs[key] is None:
            raise ValueError('Illegal "None" value for: ' + key)


def raise_if_falsy(**kwargs: Any):
    """Raise exception if any of the args is falsy."""
    for key in kwargs:
        value = kwargs[key]
        if not value:
            if value is None:
                adj = '"None"'
            elif value == 0:
                adj = 'zero'
            else:
                adj = 'empty'
            raise ValueError('Illegal {} value for: {}'.format(adj, key))


def raise_if_not_found(path, file_type):
    """Raise exception if the specified file does not exist."""
    raise_if_falsy(path)

    if file_type == FileType.FILE:
        test_func = os.path.isfile
    elif file_type == FileType.DIR:
        test_func = os.path.isdir
    else:
        test_func = os.path.exists

    if not test_func(path):
        raise_not_found(path)


def raise_if_exists(path):
    """Raise exception if a file already exists at a given path."""
    raise_if_falsy(path)
    if os.path.exists(path):
        raise_io_error(errno.EEXIST, path)


def raise_if_not_root():
    """Raise exception if the effective user is not root."""
    if os.geteuid() != 0:
        raise_io_error(errno.EPERM, message='This operation requires root privileges.')


def re_raise_new_message(exception: Exception, message: str):
    """Re-raise exception with a new message."""
    raise type(exception)(message).with_traceback(sys.exc_info()[2])
