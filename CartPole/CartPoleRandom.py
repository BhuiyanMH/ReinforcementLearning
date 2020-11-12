import gym
import numpy as np

env = gym.make('CartPole-v0')

done = False
count  = 0

observation = env.reset()
#Observation: [Cart Position, Cart Velocity, Cart Angle, Pole Angular Velocity]
print(observation)

while not done:
    env.render()
    count = 1
    action = env.action_space.sample() #choose an random action
    observation, reward, done, _ = env.step(action)

    if done:
        break
print('Game lasted: ', count, 'moves')
