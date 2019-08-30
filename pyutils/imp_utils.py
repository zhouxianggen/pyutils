# coding: utf8
from __future__ import absolute_import, unicode_literals

import os
import sys
import inspect
from importlib.machinery import SourceFileLoader


def imp_subclasses(path, Base):
    if not os.path.isfile(path):
        raise Exception('{} is not a file'.format(path))
    name, ext = os.path.splitext(os.path.basename(path))
    if ext != '.py':
        raise Exception('{} is not a python file'.format(path))
    if name in sys.modules:
        raise Exception('{} already in modules'.format(name))

    subs = []
    m = SourceFileLoader(name, path).load_module()
    for k,cls in m.__dict__.items():
        if inspect.isclass(cls) and issubclass(cls, Base):
            subs.append(cls)
    return subs

