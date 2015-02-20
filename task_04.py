#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# You code goes here
print len(MYINPUT)

if len(MYINPUT) > 2:
    print 'long'
    print 'That certainly was a {} story'.format('long')
else:
    print 'That certainly was a {} story'.format(LONGSTR)
