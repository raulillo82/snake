from turtle import Turtle
from random import randint

EDGE = 40
SIDE = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-SIDE/2+EDGE, SIDE/2-EDGE),
                randint(-SIDE/2+EDGE, SIDE/2-EDGE))
