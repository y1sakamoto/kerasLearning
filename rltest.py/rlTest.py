import oscEnv
import gym
import gym.spaces

env = gym.make('oscEnv-v0')
print('start')

observation = env.reset()

#env.render()

#action = env.action_space.sample() # your agent here (this takes random actions)
print('start')

#while True:
    #print('loop')
#    action = [1,2]
#    observation, reward, done, info = env.step(action)
#    print(observation)I

for i_episode in range(20):
    observation = env.reset()
    print(observation.shape)
    for t in range(10000):

        if i_episode == 0 and t == 0:
            print(env.action_space)

        if i_episode == 0 and t == 0:
            print(env.observation_space)

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        #print('observation::',observation)
        print('sendFrame::',env.getSendFrameNum())
        print(observation)
        print('done::',done)
        print('t::',t)



        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
