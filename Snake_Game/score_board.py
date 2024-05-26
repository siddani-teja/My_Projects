from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 20, "normal")
COLOR = "green"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt", "r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.color(COLOR)
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}    high score : {self.highscore}", align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("score.txt", "w") as file:
            file.write(str(self.highscore))
        print(self.highscore)
        self.score = 0
        self.update_score()
