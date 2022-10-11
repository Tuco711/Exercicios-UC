from configparser import RawConfigParser
from email.mime import base
from math import dist
import turtle
import random
import math

from matplotlib.colors import to_rgb
from matplotlib.legend_handler import _Line2DHandleList
from numpy import size


def QCocentro ():

    dist = 100
    DELTA = 4
    QUAD = 7

    n = 0

    while (n < QUAD):
        turtle.pencolor(random.random(), random.random(), random.random())

        for i in range(4):
            turtle.forward(QUAD + n*2*DELTA)
            turtle.left(90)

        dist = dist*2

        turtle.left(15)

        n = n+1

def estrela (lados):
    
    for i in range(lados):
        turtle.forward(10*i)
        turtle.right(144)


def hexa ():
    for i in range(6):

        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.left(60)

def passeio(vezes):
    for i in range(vezes):
        turtle.pencolor(random.random(), random.random(),random.random())
        turtle.forward(random.random()*100)
        turtle.setheading(random.random()*1000)

def piramide(dist, base):
    linhas = 0
    x0 = -( dist/2 * base)
    


    turtle.penup()
    turtle.setpos(x0, x0)
    turtle.pendown()
    for i in range(base):
        for i in range(base - linhas):
            for i in range(4):
                turtle.forward(dist)
                turtle.left(90)
            turtle.forward(dist)
        
        linhas = linhas + 1
        turtle.penup()
        turtle.setpos(x0 + linhas*dist/2, turtle.ycor() + dist)
        turtle.pendown()
    
    turtle.done()

def piramidetri(dist,base):
    linhas = 0
    x0 = -( dist/2 * base)

    h = math.sqrt(dist**2 - (dist/2)**2)

    turtle.penup()
    turtle.setpos(x0, x0)
    turtle.pendown()

    for i in range(base):
        for i in range(base - linhas):
            for i in range(3):
                turtle.forward(dist)
                turtle.left(120)
            turtle.forward(dist)
        
        linhas = linhas + 1
        turtle.penup()
        turtle.setpos(x0 + linhas*dist/2, x0 + linhas*h)
        turtle.pendown()
    
    turtle.done()

piramidetri(80, 5)