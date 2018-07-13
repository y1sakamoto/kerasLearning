import gym
from gym import envs

env = gym.make('Pendulum-v0')
print(envs.registry.all())
for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):

        if i_episode == 0 and t == 0:
            print(env.action_space)

        if i_episode == 0 and t == 0:
            print(env.observation_space)



        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
