import turtle
import random


# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("pink")

myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.speed(50)

def line(x1, y1, x2, y2, color, pensize):
  myturtle.penup()
  myturtle.goto(x1, y1)
  myturtle.color(color)
  myturtle.pensize(pensize)
  myturtle.pendown()
  myturtle.goto(x2, y2)
  myturtle.penup()
  
snow_colors = ["white", "blue", "silver", "light yellow", "light blue",  "purple", "grey", "magenta", 'green', 'orange', 'gold', 'red', 'red']

line(-190, -180, 190, -180, random.choice(snow_colors), 6)
line(-160, -150, 160, -150, random.choice(snow_colors), 6)
line(-130, -120, 130, -120, random.choice(snow_colors), 6)

# draw cake
myturtle.goto(-70,-110)
myturtle.begin_fill()
myturtle.pendown()
myturtle.color("yellow")
myturtle.goto(50,-110)
myturtle.left(90)
myturtle.forward(60)
myturtle.left(90)
myturtle.forward(125)
myturtle.left(90)
myturtle.forward(60)
myturtle.penup()
myturtle.end_fill()

#draw candles

def candle(x, color):
  myturtle.goto(x, -40)
  myturtle.color(color)
  myturtle.pendown()
  myturtle.pensize(3)
  myturtle.goto(x, -20)
  myturtle.penup()

candle(-60, random.choice(snow_colors))
candle(-40, random.choice(snow_colors))
candle(-20, random.choice(snow_colors))
candle( 0 , random.choice(snow_colors))
candle(20 , random.choice(snow_colors))
candle(40 , random.choice(snow_colors))


# print message
myturtle.goto(200, 30)
myturtle.color(random.choice(snow_colors))
myturtle.pendown()
#myturtle.write("Happy Birthday!", None, None, "45px bold")
myturtle.write("Happy Birthday!", font=("Arial",45,"normal"), align="right")


# send the turtle to the corner
myturtle.penup()
myturtle.goto(-250, 250)
myturtle.hideturtle()



