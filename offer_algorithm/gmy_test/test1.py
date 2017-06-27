# !usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

