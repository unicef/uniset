import os

from .monkeypatch import patcher

VERSION = __version__ = '0.3'
NAME = 'uniset'

ROOT = os.path.dirname(__file__)


patcher.patch1()
