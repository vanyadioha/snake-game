from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialise snake
snake = Snake()
food = Food()
score = ScoreBoard()

# KeyPress Listen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake Movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Collision with food
    if snake.snake_head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.drop_food()

    # detect wall collision
    if (
        snake.snake_head.xcor() > 280
        or snake.snake_head.xcor() < -280
        or snake.snake_head.ycor() > 280
        or snake.snake_head.ycor() < -280
    ):
        score.game_over()
        snake.game_over()
    # Detect body collision
    for body in snake.snake[1:]:
        if snake.snake_head.distance(body) < 10:
            score.game_over()
            snake.game_over()
# Don't write any code below this
screen.exitonclick()
