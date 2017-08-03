#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from dict402 import *
from pools_dict import *

with open('nonsber.txt') as f:
    for line in f:
        x = line.split()[5]
        y = line.split()[7]
        if x in dict402.keys() and y in pools_dict.keys():
            with open('nonsber_result.txt', 'a') as r:
                r.write(dict402[x] + ' ' + pools_dict[y] + '\n')
