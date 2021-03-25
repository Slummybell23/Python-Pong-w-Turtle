from food import Food
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.pensize(100)
        self.goto(0, 250)
        self.write((f"Score = {self.score}"),align="center", font=("Arial", 18, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write((f"Score = {self.score}"), align="center", font=("Arial", 18, "normal"))

    def gameover(self):
        self.home()
        self.write((f"GAME OVER"), align="center", font=("Arial", 12, "normal"))
