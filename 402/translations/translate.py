#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from dict402 import *
from dict583 import *
from pools_dict import *

with open('translations.txt') as f:
    for line in f:
        x = line.split()[5]
        y = line.split()[7]
        if x in dict402.keys() and y in pools_dict.keys():
            with open('result402.txt', 'a') as r:
                r.write(dict402[x] + ' ' + pools_dict[y] + '\n')

with open('translations.txt') as f:
    for line in f:
        x = line.split()[5]
        y = line.split()[7]
        if x in dict583.keys() and y in pools_dict.keys():
            with open('result583.txt', 'a') as r:
                r.write(dict583[x] + ' ' + pools_dict[y] + '\n')
