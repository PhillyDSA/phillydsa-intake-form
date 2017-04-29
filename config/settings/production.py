#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import os
import configparser
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = False

config = configparser.ConfigParser()

try:
    config.read(os.path.join(BASE_DIR, 'conf.ini'))  # noqa
except Exception:
    raise ImproperlyConfigured('BASE_DIR/confi.ini not found')

try:
    SECRET_KEY = config['django_keys']['secret_key']
    ACTION_NETWORK_API_KEY = config['actionnetwork']['api_key']
except KeyError:
    raise ImproperlyConfigured(
        "Keys not found. Ensure you have ['actionnetwork']['api_key'] "
        "and ['django_keys']['secret_key'] properly set.")
