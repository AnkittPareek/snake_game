from turtle import Screen
import time
from snake import Snake

screen = Screen()

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)

our_snake = Snake()
screen.listen()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    our_snake.move()

    if our_snake.squares[0].heading() == 0 or our_snake.squares[0].heading() == 180:
        screen.onkey(key="Up", fun=our_snake.turn_up)
        screen.onkey(key="Down", fun=our_snake.turn_down)
        screen.onkey(key="Left", fun=our_snake.do_nothing)
        screen.onkey(key="Right", fun=our_snake.do_nothing)
    else:
        screen.onkey(key="Left", fun=our_snake.turn_left)
        screen.onkey(key="Right", fun=our_snake.turn_right)
        screen.onkey(key="Up", fun=our_snake.do_nothing)
        screen.onkey(key="Down", fun=our_snake.do_nothing)


screen.exitonclick()
