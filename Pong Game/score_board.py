from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))
