#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 16:12:24 2021

@author: vand
"""

#%% STEP 2: JOIN
#   If joining on the local network, use 0 for host extension, so join(0, PORT)
#   If joining via network, use the host of the inviter, printed out when inviting.
import pair
socket = pair.pair.join(0, 8035) 

#%% STEP 3 (4): SEND TEXT
#   Can also be done after step 4 indicated by (4). 
#   Likewise, inviding side can start sending.
socket.sendtext('Hello world! ')

#%% STEP 6 (5): RECEIVE TEXT
txt = socket.recvtext()

#%% STEP 8 (7): RECEIVE NP ARRAY
A = socket.recvb() 

#%% STEP 9 (10): SEND NP ARRAY
B = A[:10,:12]
socket.sendb(B)

#%% STEP 12 (11): CLOSE
socket.close()



