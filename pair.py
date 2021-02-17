#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:41:01 2021

@author: vand
"""
import socket
import pickle


class pair(socket.socket):
    '''
    Extension of the socket.socket class with functionality usefull for sending 
    data between two computers on the same wireless network.
    
    It requires coordinantion between the sender and receiver, as receiving side
    will keep on waiting for the data. The intended usage is when two operators
    are sitting close by, and can (verbaly) agree when something is on the way.
    
    Author: vand@dtu.dk, 2021
    '''   
      
    def __init__(self, *args, **kwargs):
       super(pair, self).__init__(*args, **kwargs)
    
    chunk = 4096 # chunk size in bytes
    header = 64 # header size in bytes
        
    @classmethod
    def invite(cls, PORT):
        s = socket.socket()
        s.bind(('', PORT)) # binds to all available interfaces
        host = socket.gethostbyname(socket.gethostname())
        EXT = host.split('.')[3]
        s.listen()
        print(f'Inviting to {EXT}, {PORT}')
        c, address = s.accept()
        s.close()
        print('Paired!')
        return cls.copy(c)
        
    @classmethod
    def join(cls, EXT, PORT):
        if EXT == 0:
            HOST = '127.0.0.1'
        else:
            host = socket.gethostbyname(socket.gethostname())
            common = '.'.join(host.split('.')[:2])
            HOST = common + '.' + str(EXT)       
        s = socket.socket()
        s.connect((HOST, PORT))
        print('Paired!')
        return cls.copy(s)   
    
    @classmethod
    def copy(cls, s):
        fn = socket.dup(s.fileno())
        copy = cls(s.family, s.type, s.proto, fileno=fn)
        copy.settimeout(s.gettimeout())
        return copy

    def sendtext(self,text):
        self.send(text.encode())
    
    def recvtext(self):
        return self.recv(self.chunk).decode()
         
    def sendb(self, nparray):
        k = pickle.dumps(nparray)
        self.sendtext(f'{len(k):{str(self.header)}d}')
        self.sendall(k)
        
    def recvb(self):
        lenk = int(self.recv(self.header).decode())
        k = b''
        while len(k)<lenk:
            k = k + self.recv(self.chunk)
        return pickle.loads(k)
            
            
    
    
    