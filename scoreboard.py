from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.display_score()


    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!")

    def update_score(self):
        self.score += 1

    def update_and_display_score(self):
        self.update_score()
        self.display_score()
