from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.relocate_food()

    def relocate_food(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))

