from gym.envs.registration import register

register(
    id='oscEnv-v0',
    entry_point='oscEnv.env:OSCEnv'
)
