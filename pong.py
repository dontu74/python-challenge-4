#Python Challenge # 4
# In this challenge I am working tutorial based on TokyoEdtech. Credits go to @TeokyoEdTech

# import sys
# import os
# from tkinter import *
import turtle
import time

# in this session, i am creating a pop-up small screen using the build in method 'Screen()'
# i would like the window screen to be 950px x 750
wind = turtle.Screen()
wind.title("Let's play Pong")
# assigning a background color
wind.bgcolor("light blue")
wind.setup(width=800, height=600)
wind.tracer(0) # the tracer stops the window from updating and will speed up the game instead of lagging

# Adding paddle #1 to the game. Turtle = is a class from the "import turtle" library
paddle_1 = turtle.Turtle()
paddle_1.speed(0) # set the max speed (speed of animation - the turtle module)
paddle_1.shape("square") # set the paddle shape as square
paddle_1.color("navy") # assigning the color of the paddle 
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup() 
# paddle_1.sety(-350)
paddle_1.goto(-350,0)

# Adding paddle #2 to the game
paddle_2 = turtle.Turtle()
paddle_2.speed(0) # set the max speed (speed of animation - the turtle module)
paddle_2.shape("square") # set the paddle shape as square
paddle_2.color("navy") # assigning the color of the paddle 
paddle_2.shapesize(stretch_wid=5, stretch_len=1) # to stretch the paddle width, i use shapesize()
paddle_2.penup() 

paddle_2.goto(350,0)

# Adding a ball in the game
ball = turtle.Turtle()
ball.speed(0) # set the max speed (speed of animation - the turtle module)
ball.shape("circle") # set the paddle shape as square
ball.color("yellow") # assigning the color of the paddle 
ball.penup() 
ball.goto(0,0)

# Function - making the paddle move up and down
def pad_mov_up():
    y = paddle_1.ycor()
    y +=20 
    # add 20 px to the Y coordinate
    pad_mov_up.sety(y)
    # print("world")


def pad_mov_down():
    y = paddle_1.ycor()
    y -= 20 
    # add 20 px to the Y coordinate
    pad_mov_down.sety(y)
    # print("hello")

# Keyboard binding - listen for the user keyboard input
wind.listen()
wind.onkeypress(pad_mov_up,"p")
wind.onkeypress(pad_mov_down,"s")


# using while loop as a main game loop, every time the loop runs, the windows will get updated
while True:
    wind.update()

