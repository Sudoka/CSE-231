# lkd: 04/10.
# a couple of functions to illustrate turtle graphics

# these functions do not perform error checking.
# call them with reasonable arguments, or suffer the consequences.

import turtle

def drawSquare(pen, size = 50, fillcolor=""):
    """draw a square of given size using pen; fill it if fillcolor is provided"""
    pen.pencolor("black")           # square will be outlined in black
    if fillcolor:                   
        pen.fillcolor(fillcolor)    # set the fill color and
        pen.fill(True)              # begin filling
    #draw the square
    pen.down()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
        
    pen.fill(False)                 # end filling


def drawCircles(pen, size = 50, num = 6):
    """draw num circles with given radius using pen"""
    colorlst = ["#FF0000", "#FFCC00", "#CC0066", "#996666", "#9900CC",\
                "#6600FF", "#33FFFF", "#330099", "#003300", "#000099"]
    rotation = 360/float(num)

    pen.down()                   # be sure the pen is down
    for i in range(num):         # draw circles with colors from colorlst
        pen.pencolor(colorlst[i%len(colorlst)])
        pen.circle(size)
        pen.left(rotation)
        
    
    
