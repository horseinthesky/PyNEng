#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('test.txt') as f:
    f = f.read().split('\n')
    set_test = {i for i in f}
    for i in set_test:
        print(i)
