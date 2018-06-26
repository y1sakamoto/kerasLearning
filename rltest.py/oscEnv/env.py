import sys

import gym
import numpy as np
import gym
import oscEnv.osc4gym as osc
from gym import spaces

class OSCEnv(gym.Env):

    def __init__(self):
        super().__init__()
        #self.action_space = spaces.Box(low=-10, high=10, shape=(1,))
        #self.reward_range = [-10., 10.]

        self.frameNum=0
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(-10, 10, shape=(3,))
        self.reset()


    #def seed(self, seed=None):
    #    self.np_random, seed = seeding.np_random(seed)
    #    return [seed]

    def reset(self):
        self.frameNum=0
        self.done = False
        self.steps = 0
        backFrameNum=osc.getFrameNum()
        while backFrameNum != self.frameNum:
            backFrameNum=osc.getframeNum()
        self.observation = osc.getObservation()
        return self.observation


    def step(self, action):
        osc.sendAction(self.frameNum,action)

        backFrameNum=osc.getFrameNum()
        while backFrameNum != self.frameNum:
            backFrameNum=osc.getframeNum()

        self.observation = osc.getObservation()
        self.reward = osc.getReward()
        self.done = osc.getDone()
        self.frameNum=self.frameNum+1
        return self.observation, self.reward, self.done, {}


    def render(self, mode='human', close=False):
        # human の場合はコンソールに出力。ansiの場合は StringIO を返す
        #outfile = StringIO()
        return outfile
