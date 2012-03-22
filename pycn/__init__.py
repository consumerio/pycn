# -*- coding: utf-8 -*-

"""
pycn is a Python library for accessing the Consumer Notebook API.

:copyright: (c) 2012 by Daniel Greenfeld and Audrey Roy.
:license: MIT, see LICENSE for more details.

"""

__title__ = 'pycn'
__author__ = 'Daniel Greenfeld and Audrey Roy'
__license__ = 'MIT'
__copyright__ = 'Copyright 2012, Daniel Greenfeld and Audrey Roy'

VERSION = (0, 1, 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()

from pycn.oauth import OAuth2Handler, AuthorizationURLError, AccessTokenError
from functions import *