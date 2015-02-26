#playing with attributes of my turtle
import turtle

input_bckgr = input("Chose the the background color.")
wn = turtle.Screen()
wn.bgcolor(input_bckgr)       

input_turtle_clr = input("Chose the color of the turtle.")
input_str_pen = input("Chose the width of your turtle's tail.")
input_int_pen = int(input_str_pen)
tess = turtle.Turtle()
tess.color(input_turtle_clr)              
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas


#Excercises

# Question 1 - print 'we like Python's turtle!" 100 times"
phrase = "We like Python's turtle!"

for i in range(100):
    print phrase

# Question 3 
for months in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
    print "One of the months of the year is", months 

#Question 4
for numbers in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print numbers, numbers**

#Question 5 - make a regular eq triangle, square, hexagon, and octagon
import turtle
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
for i in range(3):
    alex.forward(50)
    alex.left(120)

sean = turtle.Turtle()
sean.color("black")
for i in range(4):
    sean.forward(120)
    sean.left(90)

rick = turtle.Turtle()
rick.color("green")
for i in range(6):
    rick.forward(100)
    rick.left(60)

victor = turtle.Turtle()
victor.color("red")
for i in range(8):
    victor.forward(50)
    victor.left(45)

#Question 6, inputting info to make a polygon
import turtle
wn = turtle.Screen()

alex = turtle.Turtle()

str_side = input("How many sides?")
int_side = int(str_side)

str_len = input("What will be the length of each side?")
int_len = int(str_len)

str_color = input("Choose a color.")

str_fill = input("Choose a fill color")

alex.color(str_color)
#Couldn't get the fill color to show up
alex.fillcolor(str_fill)

for i in range(int_side):
    alex.forward(int_len)
    alex.left(360/int_side)

#Question 7 - random pirate drunk walk
import turtle
wn = turtle.Screen()

pirate = turtle.Turtle()
pirate.penup()
pirate.forward(60)
pirate.pendown()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)
    
print "The pirate's final heading was", pirate.heading() 
