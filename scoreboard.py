from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.goto(-250, 260)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score - {self.score}", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)