from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")


class Scoreboard(Turtle):
    def __init__(self, place):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(place, 230)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.hideturtle()
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

