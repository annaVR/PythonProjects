__author__ = 'anna'

from operator import itemgetter
from itertools import groupby

students = [{'name': 'Anna', 'university': 'Lesgaft'}, {'name': 'Sasha', 'university': 'SPBGU'},
            {'name': 'Masha', 'university': 'Lesgaft'}, {'name': 'Sergey', 'university': 'LITMO'},
            {'name': 'Olya', 'university': 'Lesgaft'}, {'name': 'Stas', 'university': 'LITMO'},
            {'name': 'Victor', 'university': 'SPBGU'}]
students1 = sorted(students, key=lambda k: k['university'])
getuniversity = itemgetter('university')
for key, group in groupby(students1, getuniversity):
    print('University:', key)
    for record in group:
        print(record['name'])
for key, group in groupby(students1, lambda k: k['university']):
    for record in group:
        print('{} graduated from {} university'.format(record['name'], record['university']))

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", 'car'), ('animal', 'cat'),
          ('plant', 'flower'), ('vehicle', 'motorcycle')]
for k, group in groupby(sorted(things), lambda k: k[0]):
    print(k)
    for record in group:
        print('   ', record[1])

for k, group in groupby(sorted(things), lambda k: k[0]):
    for thing in group:
        print('{} is a {}'.format(thing[1], thing[0]))