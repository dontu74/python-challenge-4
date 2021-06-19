#Python Challenge # 4
# In this challenge I am working tutorial based on TokyoEdtech. Credits go to @TeokyoEdTech

import turtle

# in this session, i am creating a pop-up small screen using the build in method 'Screen()'
# i would like the window screen to be 950px x 750
wind = turtle.Screen()
wind.title("Let's play Pong")
wind.bgcolor("light blue")
wind.setup(width=900, height=750)
wind.tracer(0) # the tracer stops the window from updating and will speed up the game instead of lagging


