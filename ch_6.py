# better way of writing this function so the global
# variable is not within the function
# instead a second local variable was added tot he function's
# parameters

def badsquare(x, p):
    y = x ** p
    return y

power = 2
result = badsquare(10, power)
print(result)


# Practice Questions
# 1
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(sz*2)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

for i in range(5):
    drawSquare(alex,20)

wn.exitonclick()

# First attempt at Q2
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def biggerSquares(t,length):
    """Turtle will draw sequentially bigger squares"""
    
    for i in range(8):
        drawSquare(t,length)
        t.penup()
        t.left(45)
        t.pendown()
        drawSquare(t, length*2)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")

    #for i in range(5):
    biggerSquares(alex,20)
    #drawSquare(alex, 20)
    wn.exitonclick()

main()

# 2nd attempt at Q2
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def biggerSquares(t,length):
    """Turtle will draw sequentially bigger squares"""
    
    for i in range(8):
        drawSquare(t,length)
        t.penup()
        t.right(135)
        t.forward(10)
        t.pendown()
        drawSquare(t, length*2)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")

    #for i in range(5):
    biggerSquares(alex,20)
    #drawSquare(alex, 20)
    wn.exitonclick()

main()

# 3rd attempt at Q2
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def biggerSquares(t,length):
    """Turtle will draw sequentially bigger squares"""
    
    drawSquare(t,length)
    
    for i in range(5):
        t.penup()
        t.right(135)
        t.forward(15)
        t.left(135)
        t.pendown()
        length = length + 20
        drawSquare(t, length)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")

    biggerSquares(alex,20)
    wn.exitonclick()

main()

# Q3
import turtle

def drawPoly(t, sd, sz):
    """"Turtle will draw Polygon"""
    t.penup()
    t.right(135)
    t.forward(100)
    t.left(135)
    t.pendown()
    
    for i in range(sd):
        t.forward(sz)
        t.left(360/sd)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("pink")

    drawPoly(tess, 8, 50)
    wn.exitonclick()

main()

# Q4
import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def manySquares(t, sz):
    
    for i in range(20):
        drawSquare(t, sz)
        t.left(360/20)

        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("pink")

    manySquares(tess, 90)
    wn.exitonclick()

main()



# Q5.a
import turtle

def drawMaze(t, sz):
    """Get turtle t to draw a maze """
    for i in range(22):
        t.right(90)
        t.forward(sz)
        t.right(90)
        sz = sz + 5
        t.forward(sz)

        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("pink")

    drawMaze(tess, 5)
    wn.exitonclick()

main()

# Q5.b
import turtle

def drawMaze2(t, sz):
    """Get turtle t to draw a maze """
    angle = 90
    
    for i in range(35):
        t.right(angle)
        t.forward(sz)
        t.right(angle + 3)
        sz = sz + 5
        t.forward(sz)

        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("pink")

    drawMaze2(tess, 5)
    wn.exitonclick()

main()


# Q6
import turtle

def drawPoly(t, sd, sz):
    """"Turtle will draw Polygon"""
    t.penup()
    t.right(135)
    t.forward(100)
    t.left(135)
    t.pendown()
    
    for i in range(sd):
        t.forward(sz)
        t.left(360/sd)
        
def drawEquitriangle(t, sz):
    drawPoly(t, 3, sz)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("pink")

    drawEquitriangle(tess, 50)
    wn.exitonclick()

main()









