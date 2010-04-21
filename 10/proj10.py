# Project 10
# Draws a scene with Turtle using classes

# Algorithm
'''
Get time of day
Draw scene()
'''

# Imports
import pdb, turtle

# Classes
class cloud(object):
    '''Draws a cloud.'''

    def __init__(self, pen, color = '#FFFFFF'):
        '''
        Initializes and draws a cloud.

        Arguments: pen object, color
        Algorithm:
            Change colors
            Draw
        '''
        pen.pencolor('#FFFFFF')
        pen.fillcolor(color)
        self.draw(pen)

    def __str__(self):
        '''Prints the draw message for cloud.'''
        print 'Drawing a cloud.'

    def circle(self, pen, xpos, ypos):
        '''
        Draws a circle.

        Arguments: pen, coordinates
        Algorithm:
            Move
            Circle
        '''
        # Move
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Circle
        pen.fill(True)
        pen.down()
        pen.circle(20)
        pen.up()
        pen.fill(False)

    def draw(self, pen, xpos = -20, ypos = 175):
        '''
        Draws a cloud.

        Arguments: pen object, coordinates
        Algorithm:
            Print
            Move
            Draw circle segments
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Draw
        self.circle(pen, xpos, ypos)
        self.circle(pen, (xpos + 20), (ypos + 15))
        self.circle(pen, (xpos + 40), (ypos + 20))
        self.circle(pen, (xpos + 65), (ypos + 25))
        self.circle(pen, (xpos + 90), (ypos + 20))
        self.circle(pen, (xpos + 110), (ypos + 15))
        self.circle(pen, (xpos + 130), ypos)
        self.circle(pen, (xpos + 110), ypos)
        self.circle(pen, (xpos + 90), ypos)
        self.circle(pen, (xpos + 65), ypos)
        self.circle(pen, (xpos + 40), ypos)
        self.circle(pen, (xpos + 20), ypos)

class door(object):
    '''Draws the door.'''

    def __init__(self, pen, color):
        '''
        Initializes and draws a window.

        Arguments: pen object, colors
        Algorithm:
            Change colors
            Draw
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen, color)

    def __str__(self):
        '''Prints the draw message for door.'''
        print 'Drawing the door.'

    def draw(self, pen, color, xpos = -130, ypos = -295):
        '''
        Draws the door using rectangle().

        Arguments: pen object, color, coordinates
        Algorithm:
            Print message
            Draw rectangle
            Time of day
                Doorknob
        '''
        # Print
        self.__str__()
        # Draw
        rectangle(pen, color, xpos, ypos, 80, 60)
        # Time/ Doorknob
        if color == '#FFFF99':# Day
            doorknob(pen, '#FFFF33')
        if color == '#000066':# Night
            doorknob(pen, '#666600')

class doorknob(object):
    '''Draws the doorknob.'''
    
    def __init__(self, pen, color):
        '''
        Initializes and draws a doorknob

        Arguments: pen object, color
        Algorithm:
            Change colors
            draw()
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen)
    
    def __str__(self):
        '''Prints the draw message for doorknob.'''
        print 'Drawing the doorknob.'

    def draw(self, pen, xpos = -85, ypos = -275):
        '''
        Draws the doorknob.

        Arguemnts: pen object, coordinates
        Algorithm:
            Print
            Move
            Circle
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Circle
        pen.fill(True)
        pen.down()
        pen.circle(5)
        pen.up()
        pen.fill(False)

class house(object):
    '''Draws the house.'''

    def __init__(self, pen, color):
        '''
        Initializes and draws the house.

        Arguments: pen object, color
        Algorithm:
            Change colors
            Draw
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen, color)

    def __str__(self):
        '''Prints the draw message for house.'''
        print 'Drawing the house.'

    def draw(self, pen, color, xpos = -175, ypos = -295):
        '''
        Draws the house base.

        Arguments: pen, coordinates
        Algorithm:
            Print message
            Move
            Rectagle
            Time of day
                Door
                Windows
                Roof
        '''
        # Print
        self.__str__()
        # Rectangle
        rectangle(pen, color, xpos, ypos, 200, 150)
        # Time of day
        if color == '#FF0000':# Day
            door(pen, '#FFFF99')
            window(pen, '#FFFFFF', -160, -180)
            window(pen, '#FFFFFF', -80, -180)
            roof(pen, '#333333')
        if color == '#330000':# Night
            door(pen, '#000066')
            window(pen, '#FFCC33', -160, -180)
            window(pen, '#FFCC33', -80, -180)
            roof(pen, '#000000')
           
class leaves(object):
    '''Draws tree leaves.'''

    def __init__(self, pen, color):
        '''
        Initializes and draws leaves.

        Arguments: pen object, color
        Algorithm:
            Set colors
            Draw
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen)
       
    def __str__(self):
        '''Prints the draw message for leaves.'''
        print 'Drawing the tree leaves.'

    def cluster(self, pen, xpos, ypos):
        '''
        Draws a cluster of leaves.

        Arguments: coordinates
        Algorithm:
            Move
            Circle
        '''
        # Move
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Circle
        pen.fill(True)
        pen.down()
        pen.circle(40)
        pen.up()
        pen.fill(False)

    def draw(self, pen, xpos = 170, ypos = -15):
        '''
        Draws the leaves.

        Arguments: pen object, coodinates
        Algorithm:
            Print
            Move
            For 6 clusters
                Circle
                Move
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Draw circles
        self.cluster(pen, (xpos - 46), (ypos + 25))
        self.cluster(pen, (xpos - 40), (ypos - 20))
        self.cluster(pen, (xpos + 40), (ypos - 25))
        self.cluster(pen, (xpos - 80), (ypos + 60))
        self.cluster(pen, xpos, (ypos + 50))
        self.cluster(pen, (xpos - 95), (ypos + 30))
        self.cluster(pen, (xpos + 85), (ypos + 15))
        self.cluster(pen, (xpos + 30), (ypos + 30))
        self.cluster(pen, (xpos + 75), (ypos + 45))
        self.cluster(pen, (xpos - 25), (ypos + 80))
        self.cluster(pen, (xpos + 30), (ypos + 75))
        self.cluster(pen, xpos, ypos)

class moon(object):
    '''Draws the moon.'''

    def __init__(self, pen, color='#FFFF99'):
        '''
        Initializes and draws the moon.

        Arguments: pen object, color
        Algorithm:
            Set colors
            Draw
        '''
        pen.pencolor(color)
        pen.fillcolor(color)
        self.draw(pen)

    def __str__(self):
        '''Prints the draw message for moon.'''
        print 'Drawing the moon.'

    def draw(self, pen, xpos = -200, ypos = 170):
        '''
        Draws the moon.

        Arguments: pen object, coordinates
        Algorithm:
            Print draw message
            Move to coordinates
            Lower
            Semicircle
            Fill
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Draw
        pen.fill(True)
        pen.down()
        pen.circle(30,180)
        pen.goto(xpos,ypos)
        pen.up()
        pen.fill(False)

class rectangle(object):
    '''Draws a rectangle.'''

    def __init__(self, pen, color, xpos, ypos, height, width = 0):
        '''
        Initializes and draws a rectangle.

        Arguments: coordinates, dimensions
        Algorithm: 
            Set color
        '''
        # Set colors
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen, xpos, ypos, height, width)

    def __str__(self):
        '''Prints the draw message.'''
        print 'Drawing the rectangle.'

    def draw(self, pen, xpos, ypos, height, width):
        '''
        Draws a rectangle.

        Arguments: pen, coordinates, dimensions
        Algorithm:
            Assign width if only 1 dimension given
            Move
            Draw
        '''
        # Square
        if width == 0:
            width = height
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(90)
        # Draw
        pen.fill(True)
        pen.down()
        pen.forward(height)
        pen.right(90)
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
        pen.forward(width)
        pen.up()
        pen.fill(False)
 
class roof(object):
    '''Draws the roof.'''

    def __init__(self, pen, color):
        '''
        Initialize and draw the roof.

        Arguments: pen object, color
        Algorithm:
            Set color
            draw()
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen)

    def __str__(self):
        '''Prints draw message for roof.'''
        print 'Drawing the roof.'

    def draw(self, pen, xpos = -190, ypos = -95):
        '''
        Draws the roof.

        Arguments: pen, coordinates
        Algorithm:
            Move
            Draw triangle
        '''
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(45)
        # Draw
        pen.fill(True)
        pen.down()
        pen.forward(127)
        pen.right(90)
        pen.forward(127)
        pen.right(45)
        pen.goto(xpos, ypos)
        pen.up()
        pen.fill(False)

class sun(object):
    '''Draws the sun.'''
    
    def __init__(self, pen, color = '#FFFF66'):
        '''
        Initializes and draws the sun.

        Arguments: color, coordinates
        Algorithm:
            Set color
            draw()
        '''
        pen.pencolor(color)
        pen.fillcolor(color)
        self.draw(pen)

    def __str__(self):
        ''' Prints draw message for sun.'''
        print 'Drawing the sun.'

    def draw(self, pen, xpos = -200, ypos = 170):
        '''
        Draws the sun.

        Arguments: pen object, coordinates
        Algorithm:
            Print draw message
            Move to coordinates
            Create circle
            Create sunbeam lines
                Return to center of circle
                Rotate 30 degrees
                Draw line
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(0)
        # Draw circle
        pen.fill(True)
        pen.down()
        pen.circle(30)
        pen.up()
        pen.fill(False)
        # Draw Beams
        for i in range(0,12):
            pen.goto(xpos, (ypos + 30))
            pen.forward(30)
            pen.down()
            pen.forward(30)
            pen.up()
            pen.left(30)

class tree(object):
    '''Draws a tree.'''

    def __init__(self, pen, color):
        '''
        Initializes and draws the tree.

        Arguments: pen object, color
        Algorithm:
            Set colors
            Draw
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen, color)

    def __str__(self):
        '''Prints the draw message for tree.'''
        print 'Drawing the tree.'

    def draw(self, pen, color, xpos = 150, ypos = -295):
        '''
        Draws the tree.

        Arguments: pen object, coodinates
        Algorithm:
            Print
            Draw rectangle
            Time of Day
                Draw leaves
        '''
        # Print
        self.__str__()
        # Rectangle
        rectangle(pen, color, xpos, ypos, 300, 40)
        # Time of Day/ Draw Leaves
        if color == '#996600':# Day
            leaves(pen, '#33CC00')
        if color == '#333300':# Night
            leaves(pen, '#003300')

class ufo(object):
    '''Draws a flying saucer.'''

    def __init__(self, pen, color1 = '#336666', color2 = '#00FF00'):
        '''
        Initialize and draw a flying saucer.

        Arguments: pen, colors
        Algorithm:
            Set colors
            draw()
        '''
        pen.pencolor('#000000')
        self.draw(pen, color1, color2)

    def __str__(self):
        '''Prints the draw message for ufo.'''
        print 'Drawing something else.'

    def draw(self, pen, color1, color2, xpos = -20, ypos = 175):
        '''
        Draws a flying saucer.

        Arguments: pen object, coordinates
        Algorithm:
            Print
            Move
            Draw body
            Draw cockpit
        '''
        # Print
        self.__str__()
        # Move
        pen.up()
        pen.goto(xpos, ypos)
        pen.setheading(-160)
        # Draw body
        pen.fillcolor(color1)
        pen.fill(True)
        pen.down()
        pen.circle(300, -40)
        pen.goto(xpos,ypos)
        pen.up()
        pen.fill(False)
        # Draw cockpit
        pen.goto(xpos,ypos)
        pen.setheading(-160)
        pen.circle(300, -16)
        pen.setheading(-90)
        pen.fillcolor(color2)
        pen.fill(True)
        pen.down()
        pen.circle(20, -180)
        pen.up()
        pen.fill(False)

class window(object):
    '''Draws a window.'''

    def __init__(self, pen, color, xpos, ypos):
        '''
        Initialize and draw a window.

        Arguments: pen, color, coordinates
        Algorithm:
            Set colors
            draw()
        '''
        pen.pencolor('#000000')
        pen.fillcolor(color)
        self.draw(pen, color, xpos, ypos)

    def __str__(self):
        '''Prints the draw message for window.'''
        print 'Drawing a window.'

    def draw(self, pen, color, xpos, ypos):
        '''
        Draws a window.

        Arguments: pen object, coordinates
        Algorithm:
            Print
            Move
            Draw frame
            Draw crossbars
        '''
        # Print
        self.__str__()
        # Rectangle
        rectangle(pen, color, xpos, ypos, 40)
        # Draw crossbars
        pen.goto((xpos + 20), ypos)
        pen.setheading(90)
        pen.down()
        pen.forward(40)
        pen.up()
        pen.goto(xpos, (ypos + 20))
        pen.setheading(0)
        pen.down()
        pen.forward(40)
        pen.up()


# Functions
def scene(pen, time=True):
    '''
    Draws the scene.

    Arguments: time of day (True = day, False = night)
    Algorithm:
        Determine Time of Day
            Set background color
            Draw heavenly body
            Draw house
                Door
                    Doorknob
                Windows
                Roof
            Draw tree
                Trunk
                Leaves
    '''
    if time == True:
        turtle.bgcolor('#99CCFF')
        sun(pen)
        house(pen, '#FF0000')
        tree(pen, '#996600')
        cloud(pen)

    if time == False:
        turtle.bgcolor('#000033')
        moon(pen)
        house(pen, '#330000')
        tree(pen, '#333300')
        ufo(pen)


# Get time of day
time = True
while True:
    timeStr = raw_input('Enter time of day ([D]ay / [N]ight): ')
    if timeStr != '':
        if timeStr[0].lower() == 'd':
            time = True
            break
        elif timeStr[0].lower() == 'n':
            time = False
            break
        else:
            print 'Invalid input.\n'
        
# Draw
scene(turtle.Turtle(), time) 
stopVar = raw_input('Press enter to quit.')
