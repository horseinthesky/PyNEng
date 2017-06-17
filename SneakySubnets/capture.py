import telnetlib
import time

host = '10.10.30.1'

connect = telnetlib.Telnet(host)

connect.write(("admin\n").encode('ascii'))
connect.write(("admin\n").encode('ascii'))

connect.read_until(('Password:').encode('ascii'))
connect.write(("sh ip int br\n").encode('ascii'))
connect.write(("sh ip ro\n").encode('ascii'))
time.sleep(1)

print (connect.read_very_eager().decode('ascii'))
