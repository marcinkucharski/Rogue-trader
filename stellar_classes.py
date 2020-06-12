# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 08:30:47 2020

@author: Marcin
"""

#proponowane klasy obiektów

class phenomena:
    def __init__(self, kind):
        self.kind = kind                          #what kind of phenomena (solar flares, radiation burst etc)

class gas_giant:
    def __init__(self, size, moons, anomaly):
        self.size = size                        #captain obvious
        self.moons = moons                      #satellites - natural and artificial
        self.anomaly = anomaly                  #stellaris anomaly
    
class cloud:
    def __init__(self, composition, resource, ammount):
        self.composition = composition
        self.resource = resource
        self.ammount = ammount
    
class asteroid:
    def __init__(self, name, bodytype, composition, 
             resource1, resource2, ammount1, ammount2,
             anomaly):                          #asteroidy,pola asteroid
        self.name = name
        self.bodytype = bodytype                #asteroida / pas /etc
        self.composition = composition          #ice / carbon / rocky / crystalline
        self.resource1 = resource1              #resource - RT book
        self.resource2 = resource2
        self.ammount1 = ammount1                #ammount of resource
        self.ammount2 = ammount2
        self.anomaly = anomaly                  #stellaris anomaly
        
class barren:               #lifeless planet
    def __init__(self, bodytype, gravity, gs, 
                 resource1, resource2, ammount1, ammount2,
                 anomaly):
        self.bodytype = bodytype                 #body type from RT (small & dense, etc)
        self.gravity = gravity                   #gravity - warhammer standards (lower/ normal / higher)
        self.gs = gs                             #number of Gs 
        self.resource1 = resource1
        self.resource2 = resource2
        self.ammount1 = ammount1
        self.ammount2 = ammount2
        self.anomaly = anomaly
    
class livingplanet:
    def __init__(self, bodytype, gravity, gs,
                 resource1, resource2, resource3,
                 ammount1, ammount2, ammount3, anomaly):
        self.bodytype = bodytype
        self.gravity = gravity
        self.gs = gs  
        self.resource1 = resource1
        self.resource2 = resource2
        self.resource3 = resource3
        self.ammount1 = ammount1
        self.amomunt2 = ammount2
        self.ammount3 = ammount3
        self.anomaly = anomaly
    
class graveyard:
    def __init__(self, origin, ships, xenotech, archeotech):
        self.origin = origin
        self.ships = ships
        self.xenotech = xenotech                #ammount of xeno resources
        self.archeotech = archeotech             #archeo reseources

class hull:
    def __init__(self, faction, hullclass,
                 condition, xenotech, archeotech):                 #hulls for graveyard
        self.faction = faction
        self.hullclass = hullclass
        self.condition = condition
        self.xenotech = xenotech
        self.archeotech = archeotech
    
class station:
    def __init__(self, faction, role, condition, xenotech, archeotech):
        self.faction = faction
        self.role = role                            #observation, reaserch, military,fortress
        self.condition = condition
        self.xenotech = xenotech
        self.archeotech = archeotech

    