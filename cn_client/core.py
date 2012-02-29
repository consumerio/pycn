# -*- coding: utf-8 -*-

"""
cn_client.core
~~~~~~~~~~~~~~

This module provides the base entrypoint for Consumer Notebook.
"""

from .api import ConsumerNotebook

def login(username, password):
    """Returns an authenticated ConsumerNotebook instance, via API Key."""

    cn = ConsumerNotebook()

    # Login.
    cn.login(username, password)

    return cn