#!/bin/env python

import random
import sys

try:
    nb_grilles = int(sys.argv[1])
except IndexError:
    nb_grilles = 1

for nbg in range(0, nb_grilles):
    nombres = []
    for i in range(0, 5):
        nombre = random.randint(1, 49)
        while nombre in nombres:
            nombre = random.randint(1, 49)
        nombres.append(nombre)
    nombres.sort()
    print(nombres, '\t', random.randint(1, 10))

