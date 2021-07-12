#Python Challenge # 4
# In this challenge I am working tutorial based on TokyoEdtech. Credits go to @TeokyoEdTech

import turtle
import winsound # for Windows use 'winsound, for linux/mac - use import os

# in this session, i am creating a pop-up small screen using the build in method 'Screen()'
# i would like the window screen to be 950px x 750
wind = turtle.Screen()
wind.title("Let's play Pong")
# assigning a background color
wind.bgcolor("light blue")
wind.setup(width=800, height=600)
wind.tracer(0) # the tracer stops the window from updating and will speed up the game instead of lagging

# Adding paddle #1 to the game. Turtle = is a class from the "import turtle" library
left_pad = turtle.Turtle()
left_pad.speed(0) # set the max speed (speed of animation - the turtle module)
left_pad.shape("square") # set the paddle shape as square
left_pad.color("navy") # assigning the color of the paddle 
left_pad.shapesize(stretch_wid=5, stretch_len=1)
left_pad.penup() 
# left_pad.sety(-350)
left_pad.goto(-350,0)

# Adding paddle #2 to the game
right_pad = turtle.Turtle()
right_pad.speed(0) # set the max speed (speed of animation - the turtle module)
right_pad.shape("square") # set the paddle shape as square
right_pad.color("navy") # assigning the color of the paddle 
right_pad.shapesize(stretch_wid=5, stretch_len=1) # to stretch the paddle width, i use shapesize()
right_pad.penup() 
right_pad.goto(350,0)

# Adding a ball in the game
ball = turtle.Turtle()
ball.speed(-1) # set the max speed (speed of animation - the turtle module)
ball.shape("circle") # set the paddle shape as square
ball.color("orange") # assigning the color of the paddle 
ball.penup() 
ball.goto(0,0)
ball.dx = 0.15 #set the ball to move up the x cor by 2 px
ball.dy = -0.15 #set the ball move up the y cor by 4 px

# Function - making the LEFT paddle move up and down
def left_pad_mov_up():
    y = left_pad.ycor() # ycor in Turtle library return the Y coordinate
    y +=20   # Add 20 px as it moves up
    # add 20 px to the Y coordinate
    left_pad.sety(y)
    # print("world")
    
def left_pad_mov_down():
    y = left_pad.ycor()
    y -= 20 
    left_pad.sety(y)

# Function - making the RIGHT paddle move up and down
def right_pad_mov_up():
    y = right_pad.ycor()
    y +=20 
    # add 20 px to the Y coordinate
    right_pad.sety(y)
    # print("world")

def right_pad_mov_down():
    y = right_pad.ycor()
    y -= 20 
    right_pad.sety(y)

# Display score on center of the screen as players are playing the game
pen = turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1:  0 Player 2:  0", align="center", font=("Comic Sans MS", 20, "normal"))

# Game Score
score_a = 0
score_b = 0

# Keyboard binding - listen for the user keyboard input
wind.listen()
wind.onkeypress(left_pad_mov_up,"w") # call the move up function as user press 'w' key (mainly for the left side player)
wind.onkeypress(left_pad_mov_down,"s") # call the move down function as user press 's' key ( mainly for the left side player)
wind.onkeypress(right_pad_mov_up,"Up") # call the move up function as user press the 'Up' arrow (mainly for the right side player)
wind.onkeypress(right_pad_mov_down,"Down") # call the move down function as user press the 'Down' arrow (mainly for the right side player)


# using while loop as a main game loop, every time the loop runs, the windows will get updated
while True:
    wind.update()

    # Make the ball move
    ball.setx(ball.xcor() +  ball.dx)
    ball.sety(ball.ycor() +  ball.dy)

    # Check the screen border - if the ball goes off the screen, it will reverse its direction by setting ball.dy *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction if the ball hits 290
     

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction if the ball hits 290
 
    # Right side of the screen
    if ball.xcor() > 390: 
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1  # if ball goes off the Right side of the screen, player 1 will get 1 point
        pen.clear() # to clear the screen of old score before updating new score
        pen.write("Player A:  {} Player B:  {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 20, "normal")) # to update the score 
       
    # Left side of the screen
    if ball.xcor() < -390: 
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1  # if ball goes off the Left side of the screen, player 2 will get 1 point
        pen.clear() # to clear the screen of old score before updating new score
        pen.write("Player A:  {} Player B:  {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 20, "normal")) # to update the score 

    # Paddle and ball hit
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < right_pad.ycor() + 40 and ball.ycor() > right_pad.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # for Windows - Asyncronous - play sound in the background or program will stop
        # os.system("afplay pong.wav&") for linux

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < left_pad.ycor() + 40 and ball.ycor() > left_pad.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # for Windows - Asyncronous - play sound in the background or program will stop
        # os.system("afplay pong.wav&") for linux

