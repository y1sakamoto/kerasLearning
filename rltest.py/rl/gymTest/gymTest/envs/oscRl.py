from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import numpy as np


observation=np.zeros((1,1,4))
done=0
reward=0
frameNum=0



def setObservation(*arg):
    global observation
    global frameNum
    ls=list(arg)
    frameNum=arg[0]
    arr=np.array(ls)
    arr=np.delete(arr, 0, 0)
    observation=np.array([arr])
    print('observationDATA:',' frameNum:', frameNum, observation, sep=' ')
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
    osc_udp_server("127.0.0.1", 3722, "aservername")##recieve
    osc_method("/test/*", handlerfunction)
    osc_method("/observation/*", setObservation)

    osc_method("/finish/*", finish)
    pass


def sendAction(_frame,action):
#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    action.insert(_frame)
    msg = oscbuildparse.OSCMessage("/action/", None, action)
    osc_send(msg, "osc_sender")
    pass

def sendReset(_frame):
#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    msg = oscbuildparse.OSCMessage("/reset/", None, _frame)
    osc_send(msg, "osc_sender")
    pass


def loop():
    osc_process()
    pass


def getObservation():
    global observation
    return observation

def getDone():
    global done
    return done

def getReward():
    global reward
    return reward

def getFrameNum():
    global frameNum
    return frameNum




set()
while True:
    loop()
