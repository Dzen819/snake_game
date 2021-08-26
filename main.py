from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score, Border
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score = Score()
bord = Border()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.02)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase()
        snake.extend()
    for seg in snake.snake_body:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 3:
            score.reset()
            snake.reset()


screen.exitonclick()