from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(12):
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.up()
            snake.goto(snake.xcor() - 5 * i, 0)
            self.snake_body.append(snake)

    def extend(self):
        for i in range(4):
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.up()
            snake.goto(self.snake_body[-1].pos())
            self.snake_body.append(snake)

    def move(self):
        for snk in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snk - 1].xcor()
            new_y = self.snake_body[snk - 1].ycor()
            self.snake_body[snk].goto(new_x, new_y)

        self.head.forward(5)

        if self.head.xcor() > 280:
            self.head.goto(-280, self.head.ycor())
        elif self.head.xcor() < -280:
            self.head.goto(280, self.head.ycor())
        elif self.head.ycor() < -280:
            self.head.goto(self.head.xcor(), 254)
        elif self.head.ycor() > 254:
            self.head.goto(self.head.xcor(), -280)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
