from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import numpy as np

input=np.zeros((1,5,4))

def setListValue(*arg):
    global input
    ls=list(arg)
    input = np.delete(input, 0, 1)
    input= np.append(input, [[ls]], axis=1)
    print(input)
    pass



def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    print(s)
    print(x)
    print(y)
    pass


def handlerfunctionArray(*arg):
    # Will receive message data unpacked in s, x, y
    print(arg)
    print(type(arg))
    ls=list(arg)
    print(ls)
    pass

def finish():
    osc_terminate()
    pass


def set ():
    osc_startup()
    osc_udp_client("127.0.0.1", 2782, "aclientname")##senf
    osc_udp_server("127.0.0.1", 3723, "aservername")##recieve
    osc_method("/test/*", handlerfunction)
    osc_method("/finish/*", finish)
    pass


def send(arr):


#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    msg = oscbuildparse.OSCMessage("/test/", None, arr)
    osc_send(msg, "aclientname")
    pass

def loop():
    osc_process()
    pass


set()
while True:
    _arr=[10,10]
    send(_arr)
    loop()
