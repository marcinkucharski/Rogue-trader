#Rogue Trader system generator

#Generate system feature

import pandas
import random

df = pandas.read_csv('System.csv', sep=';')

#print (df)

row = random.randrange(1,100)

#print (row)

i = 0 
while row > df.at[i, 'R1']:
    i +=1
    if i == 11:
        break
    
#nieudolna pętla wymaga korekty
i -= 1
    
#Paramentry range do funkcji randrange do generowania 
#typu gwiazdy zawarte w tabeli system, przypisane jako zmienne dla wygody
        
sr1 = df.at[i, 'SR1']
sr2 = df.at[i, 'SR2']


#SF star feature
sf = df.at[i, 'Feature']

print ('System feature:\t\t', sf)                                          

#stt star type table
stt = pandas.read_csv('Star.txt', sep = '\t')

#random_star - star type determined by sr1 & sr2
random_star = random.randrange(sr1,sr2)
#print (random_star)                         #dotąd ok

star_row = 0

while random_star > stt.at[star_row, 'Range2']:
    star_row += 1
    if random_star == 100:
        star_row = 11
        break
    
print ('Star type:\t\t',stt.at[star_row, 'Class'])
print ('Star description:', '\n',stt.at[star_row, 'Description'], '\n')

inner_flag = stt.at[star_row, 'Inner']
biosphere_flag = stt.at[star_row, 'Biosphere']
outer_flag = stt.at[star_row, 'Outer']
life_flag = stt.at[star_row, 'Natural Life']

#test flag:
print ('Inner Cauldron:\t\t\t\t', inner_flag)
print ('Primary biosphere: \t\t\t', biosphere_flag)
print ('Outer reaches: \t\t\t\t', outer_flag)
print ('Possible natural life in the system: \t', life_flag, '\n')

#inner cauldron objects
inner_objects = 0
if inner_flag == 'Weak':
    inner_objects = random.randrange(1,6) -2
    if inner_objects < 0:
        inner_objects = 0
elif inner_flag == 'Normal':
    inner_objects = random.randrange(1,6)
elif inner_flag == 'Dominant':
    inner_objects = random.randrange(1,6) +2
else:
    inner_objects = 0
    
#print ('Number of objects in Inner Cauldron is\t', inner_objects)

#primary biosphere objects
biosphere_objects = 0
if biosphere_flag == 'Weak':
    biosphere_objects = random.randrange(1,6) -2
    if biosphere_objects < 0:
        biosphere_objects = 0
elif biosphere_flag == 'Normal':
    biosphere_objects = random.randrange(1,6)
elif biosphere_flag == 'Dominant':
    biosphere_objects = random.randrange(1,6) +2
else:
    biosphere_objects = 0
    
#print ('Number of primary biosphere objects is:\t', biosphere_objects)

#outer reaches objects
outer_objects = 0
if outer_flag == 'Weak':
    outer_objects = random.randrange(1,6) -2
    if outer_objects < 0:
        outer_objects = 0
elif outer_flag == 'Normal':
    outer_objects = random.randrange(1,6)
elif outer_flag == 'Dominant':
    outer_objects = random.randrange(1,6) +2
else:
    outer_objects = 0
    
#print ('Number of objects in outer reaches is:\t', outer_objects, '\n')
        
#inner_features - table with objects in inner cauldron

inner_features = pandas.read_csv('Inner Cauldron.tsv', sep = '\t')

inner_list = []

def system_feature (roll1, roll2, source_table):
    result = random.randrange(roll1, roll2)
    feature_row = 0
    while result > int(source_table.at[feature_row, 'Range2']):
        feature_row += 1
        if random_star == 100:
            feature_row = source_table.size
            break
    return source_table.at[feature_row, 'Element']
    
 
#Test funkcji
    
#feature_test = system_feature(1, 101, inner_features, 'range2')
#
#print (feature_test)
    
#test udany!

for i in range(inner_objects):
    inner_list.append(system_feature(1,101,inner_features))
    
print ('Features in inner cauldron: ')

for i in inner_list:
    if len(inner_list) == 0:
        print ('No features in inner cauldron')
    else:
        if i != 'Nothing':
            print ('\t\t\t\t\t', i)

biosphere_table = pandas.read_csv('Biosphere.tsv', '\t')
biosphere_list = []

for i in range(biosphere_objects):
    biosphere_list.append(system_feature(1,101,inner_features))
    
print ('Features in primary biosphere: ')

for i in biosphere_list:
    if len(biosphere_list) == 0:
        print ('No features in primary biosphere')
    else:
        if i != 'Nothing':
            print ('\t\t\t\t\t', i)

outer_table = pandas.read_csv('Outer Reaches.tsv', '\t')
outer_list = []

for i in range(outer_objects):
    outer_list.append(system_feature(1,101,outer_table))
    
print ('Features in outer reaches: ')

for i in outer_list:
    if len(outer_list) == 0:
        print ('No features in outer reaches')
    else:
        if i != 'Nothing':
            print ('\t\t\t\t\t', i)
            
import stellar_classes

#generowanie asteroid

def roll (a,b):
    res = random.randrange(a, b)
    return res

asteroid_body = ['Large asteroid', 'Asteroid Cluster', 'Asteroid belt']
asteroid_composition = ['ice', 'rock', 'crystal', 'metal']

asteroid_count = 0

asteroid_list = []

for i in inner_list:
    if i == 'Asteroid':
        asteroid_count +=1
        
for i in biosphere_list:
    if i == 'Asteroid':
        asteroid_count +=1 
        
for i in outer_list:
    if i == 'Asteroid':
        asteroid_count +=1

ast_num = 0

for i in range(0, asteroid_count):
    asteroid_list.append('Asteroid no. ' + str(ast_num))
    ast_num += 1
    
asteroid_obj_list = []
    
for i in asteroid_list:
    asteroid_obj_list.append(stellar_classes.asteroid(i, 
                                                      random.choice(asteroid_body), 
                                                      random.choice(asteroid_composition), 
                                                      'water', 'noble gas', 
                                                      roll(1,500), roll(1,500), 
                                                      False))

    
for i in asteroid_obj_list:
    print ('\n', i.name,':', i.bodytype, 'mainly composed of ', i.composition)
    





























