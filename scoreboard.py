from turtle import Turtle

EDGE = 30
SIDE = 600
COLOR="white"
ALIGMENT="center"
FONT=("Courier", 20, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.score = 0
        self.goto(0, SIDE/2 - EDGE)
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
