#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('result402.txt') as f:
    f = set(f.read().split('\n'))
    with open('nonsber.txt') as s:
        for line in s:
            line = line.rstrip('\n')
            f.discard(line)

for i in f:
    print(i)

