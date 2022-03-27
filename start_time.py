#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:55:10 2022

@author: lcabral4
"""

particle_start_time = []
for p in range(x.shape[0]):
    particle_start_time.append(time[p,0])
    
dat = np.array([particle_start_time])

dat = dat.T

np.savetxt('particle_time.txt', dat ,header = 'particle number',delimiter = ',')