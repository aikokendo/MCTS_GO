#!/usr/bin/python

import tkinter
import roles
import canvas


#initilize game variables

game_roles = roles.Roles([1,2],['blue','red'],[1,0])
state = [[0 for i in range(0,16)] for i in range(0,16)]

w = canvas.CanvasManager(game_roles,state)




