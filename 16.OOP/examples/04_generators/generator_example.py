import re


############# example 1 #############
def generate_nums(number):
     print('Start of generation')
     yield number
     print('Next number')
     yield number+1
     print('The end')

g = generate_nums(10)

for i in g:
    print(i)

############# example 2 #############

#функция
def work_with_items(items):
     result = []
     for item in items:
         result.append('Changed {}'.format(item))
     return result

#аналогичный генератор
def yield_items(items):
    for item in items:
        yield 'Changed {}'.format(item)


for i in yield_items(range(10)):
    print(i)

############# example 3 #############


def filter_lines(filename, regex):
    with open(filename) as f:
        for line in f:
            if re.search(regex, line):
                yield line.rstrip()


for line in filter_lines('config_r1.txt', '^interface'):
    print(line)


for line in filter_lines('config_r1.txt', '^interface| ip address'):
    print(line)

############# example 4 #############
import csv

def open_csv(filename):
    with open(filename) as f:
        for idx, line in enumerate(csv.reader(f), 1):
            yield idx, line


def filter_by_nexthop(iterable, nexthop):
    for idx, line in iterable:
        if line[3] == nexthop:
            yield idx, line


def filter_by_mask(iterable, mask):
    for idx, line in iterable:
        if line[2] == mask:
            yield idx, line


g1 = open_csv('rib.table.lg.ba.ptt.br-BGP.csv')
g2 = filter_by_nexthop(g1, '200.219.145.23')
print(next(g2))

g = filter_by_mask(filter_by_nexthop(open_csv(
    'rib.table.lg.ba.ptt.br-BGP.csv'),'200.219.145.23'), '22')
print(next(g))


g1 = open_csv('rib.table.lg.ba.ptt.br-BGP.csv')
g2 = filter_by_nexthop(g1, '200.219.145.23')
g3 = filter_by_mask(g2, '22')
print(next(g3))
print(next(g3))
print(next(g3))

