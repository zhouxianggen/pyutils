# coding: utf8
from __future__ import absolute_import, unicode_literals

from config_utils import Config


cfg = Config('/etc/wss2.conf')
print(cfg.get_option('sink', 'name2'))
