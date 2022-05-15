# NATHAN SARIC - 05/31/2019
# This program uses functions to perform various tests, including lines, circles,
# arcs, and polylines, using Python Turtle Graphics.
# Lastly, the program creates a drawing of a chocolate ice cream cone with sprinkles.

from turtle import *
import math

# Set the appearance and speed of turtle 
def initializeTurtle():
    shape("turtle")
    speed(3)

# Function used to draw a line given starting and ending coordinates
def drawLine(lineStart, lineEnd, lineThickness=1, lineColour="black") :
    pensize(lineThickness)
    pencolor(lineColour)
    penup()
    goto(lineStart)
    pendown()
    goto(lineEnd)
    
# Function uesd to draw a circle given a starting coordinate and radius
def drawCircle(lineStart, radius, headingAngle=0, lineThickness=1, lineColour="black", fillColour="white") :
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    setheading(headingAngle)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()

# Function used to draw an arc given a starting coordinate, radius, arc angle, and heading angle 
def drawArc(lineStart, radius, arcAngle, lineThickness=1, headingAngle=0, lineColour="black", fillColour="white") :
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    pendown()
    begin_fill()
    setheading(headingAngle)
    circle(radius, extent=arcAngle)
    end_fill()

# Function that returns a list of coordinate points required to draw a square of a given size
def generateSquarePoints(i) :
    return [(i, 0), (i, i), (0, i), (0, 0)]

# Function used to draw a polyline given a starting coordinate and a list of all coordinates to be connected with a straight line
def drawPolyLine(lineStart, points, lineColour="black", lineThickness=1, fillColour="white") :
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    pendown()
    begin_fill()

    x, y = lineStart

    for point in points: # Loop used to convert 'squareShape' , 'biggerSquareShape' , and 'triangleShape' into coordinate points
        dx, dy = point
        goto(x + dx, y + dy)
    goto(lineStart)

    end_fill()
    penup()

# Function that tests the program's ability to draw lines
def testLines():
    lineStart = (0, 0)
    lineEnd = (-100, 100)
    drawLine(lineStart, lineEnd)
    
    lineStart = (200, 200)
    lineEnd = (-200, -200)
    drawLine(lineStart, lineEnd, lineThickness=4, lineColour="blue")

# Function that tests the program's ability to draw circles
def testCircles():
    start1 = (-200, 100)
    radius = 40
    drawCircle(start1, radius)
    start2 = (200, -100)
    radius = 60
    drawCircle(start2, radius, fillColour="red")
    drawLine(start1, start2, lineThickness=3)
    start3 = (-100, -200)
    radius = 80
    drawCircle(start3, radius, lineThickness=5)
    start4 = (0, 200)
    radius = 60
    drawCircle(start4, radius, lineColour="blue", lineThickness=4, fillColour="green")
    drawLine(start3, start4, lineThickness=3, lineColour="blue")

# Function that tests the program's ability to draw circles with different heading angles
def testCircles2():
    start = (0, 0)
    radius = 100
    drawCircle(start, radius, headingAngle=90, fillColour="green")
    drawCircle(start, radius, headingAngle=270, fillColour="red")

# Function that tests the program's ability to draw arcs
def testArcs():
    start = (0, 0)
    radius = 100
    drawArc(start, radius, arcAngle=180, lineThickness=4)
    drawArc(start, radius, arcAngle=180, lineThickness=4, headingAngle=90, lineColour="red")
    drawArc(start, radius, arcAngle=180, lineThickness=4, headingAngle=180, lineColour="blue")
    drawArc(start, radius, arcAngle=180, lineThickness=4, headingAngle=270, lineColour="green")
    start = (-180, -220)
    radius = 350
    drawArc(start, radius, arcAngle=60, headingAngle=330, lineColour="yellow", fillColour="yellow")

# Function that tests the program's ability to draw polylines (forming squares and triangles)
def testPolyLines():
    squareShape = [(50, 0), (50, 50), (0, 50), (0, 0)]
    drawPolyLine((200, 200), squareShape)
    drawPolyLine((-200, 200), squareShape, lineColour="green", lineThickness=3, fillColour="blue")
    biggerSquareShape = generateSquarePoints(100)
    drawPolyLine((-200, -200), biggerSquareShape, fillColour="red")
    triangleShape = [(200, 0), (100, 100), (0, 0)]
    drawPolyLine((100, -100), triangleShape, fillColour="green")

# Function that creates my own masterpiece! 
def drawMyArt() :
    biggerSquareShape = generateSquarePoints(100)
    drawPolyLine((-140, 105), biggerSquareShape, lineColour="dark goldenrod", lineThickness=3, fillColour="peru")
    drawCircle((0, 0), 100, lineThickness=3, lineColour="saddle brown", fillColour="sienna")
    fillcolor("blanched almond")
    begin_fill()
    drawLine((0, -200),(100, 50), lineThickness=3, lineColour="moccasin")
    drawLine((100, 50), (-100, 50), lineThickness=3, lineColour="moccasin")
    drawLine((-100, 50), (0, -200), lineThickness=3, lineColour="moccasin")
    end_fill()
    drawArc((30, 185), 30, arcAngle=180, headingAngle=90, lineColour="orange red", fillColour="tomato")
    drawLine((50, 150), (70, 130), lineThickness=6, lineColour="light slate blue")
    drawLine((-50, 150), (-70, 130), lineThickness=6, lineColour="light slate blue")
    drawLine((25, 150), (10, 130), lineThickness=6, lineColour="light slate blue")
    drawLine((-25, 150), (-10, 130), lineThickness=6, lineColour="light slate blue")
    hideturtle()

# Function used to run all tests consecutively by clearing the interpreter in between tests
def main():
    initializeTurtle()
    testLines()
    clear()
    testCircles()
    clear()
    testCircles2()
    clear()
    testArcs()
    clear()
    testPolyLines()
    clear()
    drawMyArt()

main()
