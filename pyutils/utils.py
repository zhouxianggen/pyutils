# coding: utf8 
import re
import time
import json
import uuid
import random
import socket
import logging
from functools import wraps
from datetime import datetime, timedelta
from configparser import ConfigParser
from time import mktime, monotonic as now


def get_logger(name, level=logging.INFO):
    log = logging.getLogger(name)
    log.setLevel(level)
    log.propagate = False
    if not log.handlers:
        fmt = ('[%(name)-15s %(thread)-18d '
                '%(levelname)-8s %(asctime)s] %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt))
        log.addHandler(handler)
    return log


def took(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        start = now()
        r = func(obj, *args, **kwargs)
        ms = (now() - start) * 1000
        obj.log.info('%s took %.2f ms' % (func.__name__, ms)) 
        return r
    return wrapper


def get_uuid(prefix=''):
    return prefix + str(uuid.uuid4()).replace('-', '')


def get_id32():
    return '{}{}'.format(int(time.time() * 1000), random.randint(10000, 99999))
        

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


def get_hostname():
    return socket.gethostname()


def mk_datetime(timestamp):
    if not timestamp:
        return None
    return datetime.fromtimestamp(timestamp)


def mk_timestamp(dt):
    if not dt:
        return 0
    return time.mktime(dt.timetuple())


def mk_xml(params):
    return '<xml>\n%s\n</xml>' % '\n'.join(['<%s><![CDATA[%s]]></%s>' % 
            (k, v, k) for k,v in params.items()])

    
def parse_xml(content):
    root = ElementTree.fromstring(content)
    items = {}
    for e in list(root):
        items[e.tag] = e.text
    return items


def parse_datetime(s, default=None):
    s = re.sub(r'\D+', ' ', s)
    a = [int(x.strip()) for x in s.split() if x.strip()]
    if len(a) >= 3:
        a += [0] * 3
        return datetime(year=a[0], month=a[1], day=a[2], hour=a[3], 
                minute=a[4], second=a[5], microsecond=a[6])
    return default


def read_dummy_config(conf):
    if not conf:
        return {}
    string = '[dummy_section]\n' + conf
    config = ConfigParser()
    config.read_string(string)
    return dict(config.items('dummy_section'))


def yesterday():
    return datetime.now() - timedelta(days=1)

