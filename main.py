from turtle import Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialise snake
snake = Snake()

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
# Don't write any code below this
screen.exitonclick()
