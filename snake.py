from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20




class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head=self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(position)
            self.squares.append(square)
            square.shape("turtle")

    def turn_up(self):
        self.head.setheading(90)

    def turn_left(self):
        self.head.setheading(180)

    def turn_right(self):
        self.head.setheading(0)

    def turn_down(self):
        self.head.setheading(270)

    def do_nothing(self):
        pass

    def move(self):
        for square_number in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_number - 1].xcor()
            new_y = self.squares[square_number - 1].ycor()
            self.squares[square_number].goto(new_x, new_y)
            new_heading = self.squares[square_number - 1].heading()
            self.squares[square_number].setheading(new_heading)

        self.head.forward(MOVE_DISTANCE)
