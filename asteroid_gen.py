# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:09:17 2020

@author: GIS
"""

#Asteroid generator

import random

def roll (a,b):
    res = random.randrange(a, b)
    return res

asteroid_body = ['Large asteroid', 'Asteroid Cluster', 'Asteroid belt']

asteroid_count = 0

asteroid_list = []

