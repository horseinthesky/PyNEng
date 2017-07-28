#!/usr/bin/env python3
#-*- coding: utf-8 -*-

with open('result402.txt') as f:
    for line in f:
        with open('nonsber.txt') as m:
            for string in m:
                if not string == line:
                    print(line)
