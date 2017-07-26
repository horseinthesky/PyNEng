#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

"""Решение"""
def parse_sh_version(output):
    """
    Функция ожидает элемент, в котором находится вывод команды
    sh version с устройств Cisco

    Возвращает кортеж из 3-х элементов
    	ios - в формате "12.4(5)T"
	image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
	uptime - в формате "5 days, 3 hours, 3 minutes"
    """
    regex_ios = 'Cisco IOS Software.*Version (\S+),'
    regex_image = 'System image file is (\S+)'
    regex_uptime = 'router uptime is (.*)'

    for line in output:
        match_ios = re.search(regex_ios, line)
        match_image = re.search(regex_image, line)
        match_uptime = re.search(regex_uptime, line)
        if match_ios:
            ios = match_ios.group(1)
        elif match_image:
            image = match_image.group(1)
        elif match_uptime:
            uptime = match_uptime.group(1)

    return ios, image, uptime

def write_to_csv(filename, data):
    with open(filename, 'w') as w:
        writer = csv.writer(w)
        for row in data:
            writer.writerow(row)

data = []
data.append(headers)

for box in sh_version_files:
    with open(box) as f:
        data.append(list(parse_sh_version(f)))

write_to_csv('my_first_csv.csv', data)
