from turtle import Turtle, Screen, colormode
import random

col = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), 
       (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), 
       (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), 
       (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), 
       (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), 
       (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), 
       (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), 
       (170, 191, 221), (114, 10, 8)]

# Setup turtle
tim = Turtle()
tim.hideturtle()
tim.penup()
colormode(255)
tim.speed("fastest")

# Position turtle at bottom-left
tim.setheading(225)   # face diagonally down-left
tim.forward(300)      # move out of center
tim.setheading(0)     # face east

dots_per_row = 10
dots_total_rows = 10
dot_size = 20
spacing = 50

# Draw the grid
for row in range(dots_total_rows):
    for col_idx in range(dots_per_row):
        tim.dot(dot_size, random.choice(col))
        tim.forward(spacing)
    # Move up for next row
    tim.backward(spacing * dots_per_row)
    tim.left(90)
    tim.forward(spacing)
    tim.right(90)

Screen().exitonclick()
