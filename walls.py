from turtle import Turtle



class Builder(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(20)
        self.color("white")
        self.penup()
        i = 305
        self.goto(i, i)
        self.pendown()
        self.goto(i, -i)
        self.goto(-i, -i)
        self.goto(-i, i)
        self.goto(i, i)
