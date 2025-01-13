"""tap-name helper functions module."""
import enum
import os
import re

from singer import get_logger

LOGGER = get_logger()


def get_abs_path(path: str) -> str:
    """Returns absolute path for URL."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)