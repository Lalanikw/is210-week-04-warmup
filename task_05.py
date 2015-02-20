#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

BP = int(raw_input('what is your blood pressure ? '))
print ({'LOW': BP <= 89, 'IDEAL':89 <= BP <= 112, 'warning': 120 <= BP <= 139, 
        'high': 140 <= BP <= 159, 'Emergency': BP <= 160})
