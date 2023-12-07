#Author: Christine Yang_Dai
#Student no: 260990057

#This program draws aminimalist representation of a pannel
#from the horror manga Uzumaki by Junji Ito.

#Here is the reference: https://imgur.com/gallery/LHeoFGW
#I traced a minimalist version on photoshop.
#It will be constituted of three main parts:
#the hair on the left, the hair on the right and the spiral.

#The user can modify the dimension of the overall drawing
#(small, medium, large) and the color of the spiral.

import turtle
import random
from math import pi, sqrt, pow

def panel_limits(art_turtle, panel_width, panel_height):
    '''(void, num, num) -> void
    The function traces a rectangle with panel_width x panel_height dimension.
    '''
    art_turtle.penup()
    art_turtle.goto(-panel_width/2, panel_height/2)
    art_turtle.pendown()
    for i in range(2):
        art_turtle.forward(panel_width)
        art_turtle.right(90)
        art_turtle.forward(panel_height)
        art_turtle.right(90)
    
def draw_left_hair(art_turtle, panel_width, panel_height):
    '''(void, num, num) -> void
    The function draws a shape representing the left side of hair.
    '''
    art_turtle.fillcolor("black") #to fill the hair black
    art_turtle.begin_fill()
    
    #these value represent the coordinate of deliberatly chosen points to trace the hair
    #the character has a fringe that end in the mid section of the ppannel
    #I use fraction so that it works with all 3 dimensions of artwork
    yfringe_start = panel_height/2
    yfringe_end = -13/144 * panel_height
    xfringe_start = -5/32*panel_width
    
    yhair_start = yfringe_end
    yhair_end = -panel_height/2
    xhair_end = -sqrt((yhair_end + 25/36 * panel_height) / 0.05) - 9/40 * panel_width
    
    #the start of the drawing
    art_turtle.penup()
    art_turtle.goto(xfringe_start, yfringe_start)
    
    #I used fractions to trace the fringe and the hair
    for y_fringe in range(int(yfringe_start), int(yfringe_end), -1):
        x_fringe = -sqrt((y_fringe - yfringe_start) * -40) + xfringe_start
        art_turtle.goto(x_fringe, y_fringe)
        art_turtle.pendown()
    
    for y_hair in range(int(yhair_start), int(yhair_end), -1):
        x_hair = -sqrt((y_hair + 25/36 * panel_height) / 0.05) - 9/40 * panel_width
        art_turtle.goto(x_hair, y_hair)
        art_turtle.pendown()
    
    #to fill the rest of the hair, I am tracing the sides of the panel
    art_turtle.backward(panel_width/2 + xhair_end)
    art_turtle.left(90)
    art_turtle.forward(panel_height)
        
    art_turtle.end_fill() #end the color filling

def draw_right_hair(art_turtle, panel_width, panel_height):
    '''(void, num, num) -> void
    The function draws a shape representing the right side of hair.
    '''
    art_turtle.fillcolor("black") #to fill the hair black
    art_turtle.begin_fill()
    
    #same than before, defining the important coordinates
    xfringe_end = 23/80 * panel_width
    yfringe_end = -13/144 * panel_height
    yfringe_start = panel_height/2
    xfringe_start = -(pow(((yfringe_start - yfringe_end) * 20000/3), (1/3))) + xfringe_end
    
    yhair_end = -panel_height/2
    xhair_end = -sqrt((yhair_end + 25/36 * panel_height) / 0.05) + 31/80 * panel_width
    
    art_turtle.penup() #turtle starts to draw now
    art_turtle.goto(xfringe_start, yfringe_start)
    
    #again, using 2 fonctions for 2 pieces of hair
    for y_fringe in range(int(yfringe_start), int(yfringe_end), -1):
        x_fringe = -(pow(((y_fringe - yfringe_end) * 20000/3), (1/3))) + xfringe_end
        art_turtle.goto(x_fringe, y_fringe)
        art_turtle.pendown()
    
    for y_hair in range(int(yfringe_end), int(yhair_end), -1):
        x_hair = -sqrt((y_hair + 25/36 * panel_height) / 0.05) + 31/80 * panel_width
        art_turtle.goto(x_hair, y_hair)
        art_turtle.pendown()
    
    #same than before, tracing the panel to fill the shape
    art_turtle.right(90)
    art_turtle.forward(panel_width/2 - xhair_end)
    art_turtle.left(90)
    art_turtle.forward(panel_height)
    art_turtle.left(90)
    art_turtle.forward(panel_width/2 - xfringe_start)
    art_turtle.end_fill()

def polygon(art_turtle, lenght, n_sides): #for later use for the spiral
    '''(void, num, num) -> void
    The function draws a polygon of n_sides with "lenght" lenght sides.
    '''
    angle = 360/n_sides
    for i in range(n_sides):
        art_turtle.forward(lenght)
        art_turtle.right(angle)
        
def circle(art_turtle, radius): #for later use for the spiral
    '''(void, num) -> void
    This function draws a circle with "radius" radius.
    '''
    polygon(art_turtle, ((2 * pi * radius) / 360), 360)
    
def circle_spiral(art_turtle, panel_width, panel_height, size_factor, color):
    '''(void, num, num, float, str) -> void
    This function draws a circle containing smaller circles leaning on a side. 
    '''
    #coordinate of where the spiral starts
    x = 1/16 * panel_width
    y = 3/16 * panel_height
    
    #turtle get in position
    art_turtle.penup()
    art_turtle.goto(x, y)
    art_turtle.left(90)
    art_turtle.pendown()
    
    #start to fill now
    art_turtle.fillcolor(color)
    art_turtle.begin_fill()
    
    #create a spiral with a radius in the range of the smallest circle to largest circle
    #with a random number(integer) of inner circles
    for radius in range (int(10*size_factor), int(120*size_factor), random.randint(int(10*size_factor), int(20*size_factor))):
        circle(art_turtle, radius)
        x += radius/10 #radius/10 is added to create an illusion of depth
        
        art_turtle.penup() #getting in position b/w each circle
        art_turtle.goto(x, y)
        art_turtle.pendown()
        
    art_turtle.end_fill() #end the color filling

def signature(art_turtle, size_factor):
    '''(void, float) -> void
    This function draws a 'C'.
    '''
    art_turtle.penup()
    art_turtle.goto(380, -300*size_factor)
    art_turtle.right(45)
    art_turtle.pendown()
    
    for i in range(260):
        art_turtle.forward(((2 * pi * 30) / 360))
        art_turtle.right(1)

def artwork():
    '''void -> void
    The function traces the artwork by calling the right functions.
    '''
    size = input("Enter the size (small, medium, large): ")
    
    size_range = ["small", "medium", "large"]
    
    while size not in size_range:
        print("Enter a valid size.")
        size = input("Enter the size (small, medium, large): ")
        
    uzumaki = turtle.Turtle()
    uzumaki.speed("fastest")
    uzumaki.hideturtle()

    if size == size_range[-1]:
        user_width = 800
        user_height = 432
        user_factor = 1.0
    elif size == size_range[0]:
        user_width = 400
        user_height = 216
        user_factor = 0.5
    else:
        user_width = 600
        user_height = 324
        user_factor = 0.75

    panel_limits(uzumaki, user_width, user_height)
    draw_left_hair(uzumaki, user_width, user_height)
    draw_right_hair(uzumaki, user_width, user_height)
    
    color_range = ["blue", "purple", "red"]
    user_color = input("Choose a color (blue, purple or red): ")
    while user_color not in color_range:
        print("Enter a valid color.")
        user_color = input("Choose a color (blue, purple or red): ")
    circle_spiral(uzumaki, user_width, user_height, user_factor, user_color)
    
    signature(uzumaki, user_factor)
