import oscEnv
import gym

env = gym.make('oscEnv-v0')
observation = env.reset()

#env.render()

action = env.action_space.sample() # your agent here (this takes random actions)
observation, reward, done, info = env.step(action)
