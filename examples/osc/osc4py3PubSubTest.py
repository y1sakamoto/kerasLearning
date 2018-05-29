from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import numpy as np

def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    print(s)
    print(x)
    print(y)
    pass

def finish():
    osc_terminate()
    pass


def set ():
    osc_startup()
    osc_udp_client("127.0.0.1", 2782, "aclientname")##senf
    osc_udp_server("127.0.0.1", 3722, "aservername")##recieve
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
