# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:07:19 2020

@author: GIS
"""


import random

planets = random.randrange(1,5)


class bodies:
    def __init__(self, name, body):
        self.name = name
        self.body = body
    
celestials = []

celestial_num = 0

for i in range(0, planets):
    celestials.append('planet' + str(celestial_num))
    celestial_num += 1
    
celist = []

body_list = ['Barren World','Frozen World','Molten World', 'Toxic World', 'Broken	World']

for i in celestials:
    celist.append(bodies(i, random.choice(body_list)))
    
for i in celist:
    print(i.name, i.body)

