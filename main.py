#!/usr/bin/python

import tkinter
import roles
import canvas
import random



#initilize game variables

ai_order = [0,0]
ai_order[random.randint(0,1)]=1
game_roles = roles.Roles(ai_order)
state = [[0 for i in range(0,16)] for i in range(0,16)]

w = canvas.CanvasManager(state)


