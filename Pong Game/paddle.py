from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):

        self.goto(self.xcor(), self.ycor() + 40)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 40)
