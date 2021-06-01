from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())

        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.update()

    def update(self):
        self.write(arg=f"Score = {self.points} High Score = {self.high_score}", font=FONT, align=ALIGNMENT)

    def refresh_score(self):
        self.clear()
        self.points += 1
        if self.points > self.high_score:
            self.high_score = self.points
        self.update()

    def game_over(self):
        self.home()
        self.color("red")
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))  
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=250)
        self.points = 0         
        # with open("data.txt", "w") as file:
        #     file.write(str(self.high_score))


