#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:36:54 2022

@author: lcabral4
"""

data = np.loadtxt('test.txt')

#print(type(data[0,:]))

#plt.figure()
plt.figure(1)
CO = len(data[:,1])
bins = int(np.sqrt(CO))
#plt.yscale('log', nonpositive='clip')
y = data[:,1]
print(len(y))
x = data[:,0]
print(x)
print(y)
#print(bins)
#print("Time std is", np.std(y))
plt.title('time particle reaches polygon')
plt.ylabel('Number of Particles',fontsize=16)
plt.xlabel('t (Day)',fontsize=16)
plt.hist(y, bins=bins)
plt.savefig('bin.png')