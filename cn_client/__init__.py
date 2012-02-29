# -*- coding: utf-8 -*-

"""
requests
~~~~~~~~

:copyright: (c) 2012 by Daniel Greenfeld.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'cn-client'
__author__ = 'Daniel Greenfeld'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012 Daniel Greenfeld'

VERSION = (0, 1, 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()

