from gym.envs.registration import register

register(
    id='testenv-v0',
    entry_point='gymTest.env:TestEnv'
)

import gym

env = gym.make('testenv-v0')
