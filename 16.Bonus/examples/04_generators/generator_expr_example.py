import csv
from collections import namedtuple


'''
#сначала надо скачать файл:
wget https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz

#распаковать
gunzip rib.table.lg.ba.ptt.br-BGP.csv.gz
'''
f =  open('rib.table.lg.ba.ptt.br-BGP.csv')
reader = csv.reader(f)

headers = next(reader)
Route = namedtuple("Route", headers)

####для примера, берем 10 маршрутов
examples = [next(reader) for _ in range(10)]
route_tuples = map(Route._make, examples)
nhop_23 = (route for route in route_tuples if route.nexthop=='200.219.145.23')

print(list(nhop_24)

####для всех маршрутов
from itertools import islice

f =  open('rib.table.lg.ba.ptt.br-BGP.csv')
reader = csv.reader(f)

headers = next(reader)
Route = namedtuple("Route", headers)

route_tuples = map(Route._make, reader)
nhop_23 = (route for route in route_tuples if route.nexthop=='200.219.145.23')
mask_23 = (route for route in nhop_23 if route.netmask == '23')


#так можно брать по 10 строк
print(list(islice(mask_23, 10)))
