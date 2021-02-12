#!/bin/env python

import random
import sys

try:
    nb_grilles = int(sys.argv[1])
except IndexError:
    nb_grilles = 1

for nbg in range(0, nb_grilles):
    nombres = []
    etoiles = []
    for i in range(0, 5):
        nombre = random.randint(1, 50)
        while nombre in nombres:
            nombre = random.randint(1, 50)
        nombres.append(nombre)
    nombres.sort()
    for i in range(0, 2):
        etoile = random.randint(1, 12)
        while etoile in etoiles:
            etoile = random.randint(1, 12)
        etoiles.append(etoile)
    etoiles.sort()
    print(nombres, '\t', etoiles)

