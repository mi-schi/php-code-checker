#!/usr/bin/env python

from app import *

mode = helper.get_mode()
initialization.run(helper.get_project_dir())

if mode == 'all' or mode == 'check':
    wrapper.check()

if mode == 'all' or mode == 'metric':
    wrapper.metric()

if mode == 'coverage':
    wrapper.coverage()



