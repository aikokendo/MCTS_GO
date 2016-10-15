#!/usr/bin/python

import tkinter
import roles
import canvas


#initilize game variables

gameroles = roles.roles([1,2],['blue','red'],[1,0])
state = [[0 for i in range(0,16)] for i in range(0,16)]

w = canvas.canvasManager(gameroles,state)




