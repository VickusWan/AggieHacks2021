# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:51:11 2021

@author: Victor
"""

import os

directories = ['employ', 'food', 'housing', 'spending']
cwd = os.getcwd()

for d in directories:
    path = "/googleHacks/{}".format(d)
    
    try:
        os.mkdir(cwd+path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

