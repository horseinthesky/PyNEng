#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import yaml
from draw_network_graph import draw_topology

def topology_transform(raw_topology):
    formatted_topology = {}
    for l_device, peer in raw_topology.items():
        for l_int, remote in peer.items():
            r_device, r_int = list(remote.items())[0]
            if not (r_device, r_int) in formatted_topology:
                formatted_topology[(l_device, l_int)] = (r_device, r_int)
    return formatted_topology

with open('topology.yaml') as f:
    topology = yaml.load(f)

formatted_topology = topology_transform(topology)
# print(formatted_topology)
draw_topology(formatted_topology)
