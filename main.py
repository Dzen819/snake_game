from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

snake_body = []
for i in range(3):
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.goto(snake.xcor() + 20*i, 0)
    snake_body.append(snake)








screen.exitonclick()