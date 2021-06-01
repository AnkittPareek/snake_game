from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
from walls import Builder

screen = Screen()

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)
our_snake = Snake()
our_food = Food()
bob = Builder()
score = Score()


def start():
    our_snake.head.home()
    our_food.clear()
    score.clear()
    screen.listen()
    screen.onkey(key="Up", fun=our_snake.turn_up)
    screen.onkey(key="Down", fun=our_snake.turn_down)
    screen.onkey(key="Left", fun=our_snake.turn_left)
    screen.onkey(key="Right", fun=our_snake.turn_right)

    game_is_on = True
    points = 0

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        our_snake.move()
        score.update()

        if our_snake.head.distance(our_food) < 15:
            our_food.refresh()
            our_snake.extend()
            score.refresh_score()
        if our_snake.head.xcor() < -280 or our_snake.head.xcor() > 280 \
                or our_snake.head.ycor() < -280 or our_snake.head.ycor() > 280:
            game_is_on = False
            score.game_over()
            our_snake.reset()
        for square in our_snake.squares[1:]:
            if our_snake.head.distance(square) < 10:
                game_is_on = False
                score.game_over()
                our_snake.reset()


start()
# choice = screen.textinput("You lost!!", "Do you want to try again? Y or N").lower()
#
# if choice == "y":
#     start()
screen.exitonclick()
