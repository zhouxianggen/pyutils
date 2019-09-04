# coding: utf8
from __future__ import absolute_import, unicode_literals

import json 
from datetime import datetime


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, bytes):
            return obj.decode('utf8')
        else:
            return json.JSONEncoder.default(self, obj)

