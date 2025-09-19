#TurtleGraphics.py
#Name:Nola Nelson
#Date:9/19/25
#Assignment:Lab4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
        
def fillCorner(nola, corner) :
    #draw big square
    drawSquare(nola, 100)
    
    if corner == 1:
        nola.begin_fill()
        drawSquare(nola, 50)
        nola.end_fill()
    elif corner == 2:
        nola.forward(50)
        nola.begin_fill()
        drawSquare(nola, 50)
        nola.end_fill()
    
    if corner == 1:
        nola.begin_fill()
        drawSquare(nola, 50)
        nola.end_fill()
    elif corner == 3:
        nola.right(90)
        nola.forward(50)
        nola.left(90)
        nola.begin_fill()
        drawSquare(nola, 50)
        nola.end_fill()
    
def squaresInSquares (Nola, numberSquares):
    size = 10
    for i in range(numberSquares):
        Nola.penup()
        Nola.goto(-size/2, size/2)
        Nola.right(90)
        Nola.goto(-size/2, size/2)
        Nola.left(90)
        Nola.pendown()
        drawSquare(Nola, size)
        size += 20
    
    



def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    
    #drawPolygon(myTurtle, 8) #draws an octogon
    
    #drawPolygon(myTurtle, 3) #draws a triangle

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
