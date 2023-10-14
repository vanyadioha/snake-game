from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        # Initial snake body
        for i in range(3):
            snake_element = Turtle("square")
            snake_element.penup()
            snake_element.color("white")
            snake_element.goto(-20 * i, 0)
            self.snake.append(snake_element)

        self.snake_head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() == DOWN:
            return
        else:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def extend(self):
        snake_element = Turtle("square")
        snake_element.penup()
        snake_element.color("white")
        snake_element.goto(self.snake[-1].position())
        self.snake.append(snake_element)
