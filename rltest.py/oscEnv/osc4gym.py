from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from osc4py3 import oscmethod as osm
import numpy as np


observation=np.zeros((1,1,19))
done=0
reward=0
receiveFrameNum=0



def setObservation(*arg):
    global observation
    global receiveFrameNum
    global reward
    global done

    ls=list(arg)
    #frameNum=arg[0]
    arr=np.array(ls)
    receiveFrameNum=int(arr[0])
    reward=arr[-2]
    done=bool(arr[-1])
    observation=np.array(arr[1:-2])


    #print('receiveFrameNum:', receiveFrameNum)
    #print('observationDATA:', observation)
    #print('reward:', reward)
    #print('done:', done)

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
    osc_udp_client("127.0.0.1", 2782, "osc_sender")##senf
    osc_udp_server("127.0.0.1", 3730, "osc_reciever")##recieve
    osc_method("/test/*", handlerfunction)
    osc_method("/observation/*", setObservation)
    osc_method("/finish/*", finish)
    print('set')
    pass


def sendAction(_frame,action):
#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    arr=np.array(action)
    arr=np.insert(arr,0,_frame)
    #print(arr)
    list=arr.tolist()
    msg = oscbuildparse.OSCMessage("/action/", None, list)
    osc_send(msg, "osc_sender")
    pass

def sendReset(_frame):
#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    msg = oscbuildparse.OSCMessage("/reset/", None, [_frame])
    #print(msg)
    osc_send(msg, "osc_sender")
    pass


def loop():
    osc_process()
    #print('osc_process')
    pass


def getObservation():
    global observation
    return observation

def getDone():
    global done
    #print('getdone:',done)
    return done

def getReward():
    global reward
    return reward

def getReceiveFrameNum():
    global receiveFrameNum
    return receiveFrameNum

def send(arr):
#    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    msg = oscbuildparse.OSCMessage("/test/", None, arr)
    osc_send(msg, "osc_sender")
    pass

'''
set()
while True:
    #send(np.array([10,10]))
    sendReset(10)
    #sendAction(10,[2,10])
    loop()
'''
