# coding: utf8
from __future__ import absolute_import, unicode_literals

from configparser import ConfigParser


class Config(object):
    def __init__(self, conf):
        self.cfg = ConfigParser()
        self.cfg.read(conf)


    def get_option(self, section, option, type=None, default=None):
        if (self.cfg.has_section(section) and 
                self.cfg.has_option(section, option)):
            v = self.cfg.get(section, option)
        elif default is not None:
            return default
        else:
            raise Exception('缺少配置项 {}.{}'.format(section, option))
        if type is not None:
            try:
                v = type(v)
            except Exception as e:
                raise Exception('配置项值类型错误 {}.{}={}'.format(
                        section, option, v))
        return v

