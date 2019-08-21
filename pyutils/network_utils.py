# coding: utf8
from __future__ import absolute_import, unicode_literals

import socket


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        n = s.getsockname()
        ip = n[0] if n else None
        s.close()
        return ip
    except Exception as e:
        return None

