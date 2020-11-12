'''
In this program, we will play 100 games with 100 different weights.
For each weight, we play 100 games and take the average.
Throughout this, we track the best weight
Then we play game with the best weight and save the gameplay
'''

import gym
import numpy as np
from gym import wrappers

env = gym.make('CartPole-v0')

best_length = 0
episode_lengths = []
best_weights = np.zeros(4)

for i in range(100):
    #play 100 games with 100 different weights
    new_weights = np.random.uniform(-1.0, 1.0, 4)

    length = []
    #for each weight, play 10 games and take the average
    for j in range(100):
        # Observation: [Cart Position, Cart Velocity, Cart Angle, Pole Angular Velocity]
        observation = env.reset()
        done = False
        count = 0

        while not done:
            #env.render()
            count = 1
            #chose actions as: Move Left if negative, Move Right if positive
            action = 1 if np.dot(observation, new_weights) > 0 else 0

            observation, reward, done, _ = env.step(action)

            if done:
                break
        length.append(count)

    average_length = float(sum(length)/len(length))
    if average_length > best_length:
        best_length = average_length
        best_weights = new_weights
    episode_lengths.append(average_length)

    if i%10 == 0:
        print('Best length is: ', best_length)

#Now we play the game we developed by playing 100 games with 100 different weights
done = False
count = 0
env = wrappers.Monitor(env, 'RenderedVideos', force=True)
observation = env.reset()

while not done:
    count = 1
    action = 1 if np.dot(observation, best_weights) > 0 else 0
    observation, reward, done, _ = env.step(action)

    if done:
        break

print('Game lasted with best weights: ', count, 'moves')
