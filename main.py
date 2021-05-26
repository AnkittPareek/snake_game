from turtle import Turtle, Screen
from random import *
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

start_position = [(0, 0), (-20, 0), (-40, 0)]

squares = []

for position in start_position:
    square = Turtle()
    square.penup()
    square.shape("square")
    square.color("white")
    square.goto(position)
    squares.append(square)


def turn_up():
    squares[0].setheading(90)


def turn_left():
    squares[0].setheading(180)


def turn_right():
    squares[0].setheading(0)


def turn_down():
    squares[0].setheading(270)


def do_nothing():
    pass


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for square_number in range(len(squares) - 1, 0, -1):
        new_x = squares[square_number - 1].xcor()
        new_y = squares[square_number - 1].ycor()
        squares[square_number].goto(new_x, new_y)

    squares[0].forward(20)

    screen.listen()
    if squares[0].heading() == 0 or squares[0].heading() == 180:
        screen.onkey(key="Up", fun=turn_up)
        screen.onkey(key="Down", fun=turn_down)
        screen.onkey(key="Left", fun=do_nothing)
        screen.onkey(key="Right", fun=do_nothing)
    else :
        screen.onkey(key="Left", fun=turn_left)
        screen.onkey(key="Right", fun=turn_right)
        screen.onkey(key="Up", fun=do_nothing)
        screen.onkey(key="Down", fun=do_nothing)

screen.exitonclick()
