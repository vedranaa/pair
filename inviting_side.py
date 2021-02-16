#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:12:24 2021

@author: vand
"""

#%% STEP 1: INVITE
import pair
import numpy as np
socket = pair.pair.invite(8035)

#%% STEP 4 (3): RECEIVE TEXT
txt = socket.recvtext()

#%% STEP 5 (6): SEND TEXT
socket.sendtext('And back to you. ')

#%% STEP 7 (8): SEND NP ARRAY
A = np.arange(1000000).reshape((2500,400))
socket.sendnp(A)

#%% STEP 10 (9): RECEIVE NP ARRAY
B = socket.recvnp()

#%% STEP 11 (12) CLOSE
socket.close()



