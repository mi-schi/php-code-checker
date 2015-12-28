#!/usr/bin/env python

import sys
from app import initialization

php_bin = 'php'

if 1 in sys.argv:
    php_bin = sys.argv[1]

initialization.update(php_bin)
