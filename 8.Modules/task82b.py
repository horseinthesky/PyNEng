#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from task82 import parse_cdp_neighbors
from draw_network_graph import draw_topology

infiles = ['sh_cdp_n_sw1.txt',
           'sh_cdp_n_r1.txt',
           'sh_cdp_n_r2.txt',
           'sh_cdp_n_r3.txt']

topology = {}

for f in infiles:
    with open(f, 'r') as show_command:
        parsed = parse_cdp_neighbors(show_command.read())
        for box, neighbor in parsed.items():
            if not neighbor in topology:
                topology[box] = neighbor

draw_topology(topology)
