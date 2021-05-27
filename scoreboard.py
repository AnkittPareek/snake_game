from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        self.points = 0
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update()

    def update(self):
        self.write(arg=f"Score = {self.points}", font=FONT, align=ALIGNMENT)

    def refresh_score(self):
        self.clear()
        self.points += 1
        self.update()

    def game_over(self):
        self.home()
        self.color("red")
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
        self.penup()
        self.sety(-50)
        self.write("Press Space to Start Again.", align=ALIGNMENT, font=FONT)
