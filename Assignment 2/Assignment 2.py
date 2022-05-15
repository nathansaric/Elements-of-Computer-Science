# NATHAN SARIC - 05/24/2019 

# This program creates a dart board using Python Turtle Graphics

from turtle import *

# Global variables used as constants
RADIUS = 200

# Method used to draw 20 equal pie-shaped slices to form a circle
def pie_slice(RADIUS):
    # Set the appearance of turtle and configure line thickness and colour
    shape("turtle")
    pensize(3)
    pencolor("black")
    fillcolor("white smoke")
    speed(0)
    i = 0
    # Loops for 20 times (20 slices)
    while i <= 20 :   
        pendown()
        pencolor()
        begin_fill()
        circle(RADIUS, 18)  # Move turtle along the arc
        left(90)
        forward(RADIUS)     # Return turtle to the centre
        left(162)           # 180 degrees - 18 degrees
        forward(RADIUS)     # Move turtle to the edge of the circle
        end_fill()
        left(90)            # Reorient turtle to face the direction of the circle
        i += 1
        penup()
        circle(RADIUS, 18)  # Move turtle to the starting position for the next slice
        pendown()
        if fillcolor() == "white smoke" :
            fillcolor("dim gray")
        else :
            fillcolor("white smoke")

# Method used to draw the larger outer ring
def outer_ring_1():
    penup()
    right(90)
    forward(200)
    left(90)
    pie_slice(RADIUS)

outer_ring_1()

# Method used to draw the smaller outer ring
def outer_ring_2():
    penup()
    left(90)
    forward(20)
    right(90)
    pie_slice(RADIUS - 20)

outer_ring_2()

# Method used to draw the larger inner ring
def inner_ring_1():
    penup()
    left(90)
    forward(80)
    right(90)
    pie_slice(RADIUS - 100)

inner_ring_1()

# Method used to draw the smaller inner ring
def inner_ring_2():
    penup()
    left(90)
    forward(20)
    right(90)
    pie_slice(RADIUS - 120)

inner_ring_2()

# Method used to draw green bullseye ring
def green_bullseye():
    fillcolor("forest green")
    penup()
    left(90)
    forward(60)
    right(90)
    pendown()
    begin_fill()
    circle(20)
    end_fill()

green_bullseye()

# Method used to draw red bullseye ring
def red_bullseye():
    fillcolor("tomato")
    penup()
    left(90)
    forward(10)
    right(90)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    hideturtle()    # Hide turtle

red_bullseye()
