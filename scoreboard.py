from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score} ", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.1, 30)
        self.up()
        self.goto(0, 265)
