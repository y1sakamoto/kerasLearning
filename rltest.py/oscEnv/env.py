import sys

import gym
import numpy as np
import gym
import oscEnv.osc4gym as osc
#import osc4gym as osc

from gym import spaces
import gym.spaces

class OSCEnv(gym.Env):

    def __init__(self):
        super().__init__()
        #self.action_space = spaces.Box(low=-10, high=10, shape=(1,))
        #self.reward_range = [-10., 10.]
        self.max_torque=0.01
        self.sendFrameNum=1
        #self.action_space = spaces.Box(low=-self.max_torque, high=self.max_torque, shape=(1,))
        self.action_space = spaces.Box(low=-self.max_torque, high=self.max_torque, shape=(2,))


        #self.action_space = spaces.Discrete(2)

        self.observation_space = spaces.Box(-1.0, 1.0, shape=(19,))

        osc.set()

        #self.reset()




    #def seed(self, seed=None):
    #    self.np_random, seed = seeding.np_random(seed)
    #    return [seed]

    def reset(self):
        self.sendFrameNum=self.sendFrameNum+1
        self.done = False
        self.steps = 0

        osc.sendReset(self.sendFrameNum)

        receiveFrameNum=osc.getReceiveFrameNum()

        while receiveFrameNum != self.sendFrameNum:
            receiveFrameNum=osc.getReceiveFrameNum()
            osc.loop()
        self.observation = osc.getObservation()
        return self.observation


    def step(self, action):
        #print('sendAction')
        self.sendFrameNum=self.sendFrameNum+1
        osc.sendAction(self.sendFrameNum,action)

        receiveFrameNum=osc.getReceiveFrameNum()

        while receiveFrameNum != self.sendFrameNum:
            receiveFrameNum=osc.getReceiveFrameNum()
            #print('receiveFrameNum:',receiveFrameNum,' sedFrameNum:',  self.sedFrameNum, sep=' ')

            osc.loop()
            #print('loop')
        #print('loopOut')
        self.observation = osc.getObservation()
        self.reward = osc.getReward()
        self.done = osc.getDone()
        return self.observation, self.reward, self.done, {}


    def render(self, mode='human', close=False):
        # human の場合はコンソールに出力。ansiの場合は StringIO を返す
        #outfile = StringIO()
        pass
        #return outfile

    def oscLoop():
        osc.loop()
        pass

    def getSendFrameNum(self):
        return self.sendFrameNum


'''
env=OSCEnv()

while True:
    arr=[10,10]
    env.step(arr)
'''
