from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self, snake):
        self.snake = snake
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for x in range(3):
            block = Turtle('square')
            block.color('white')
            block.penup()
            block.setpos(x * -20, 0)
            self.snake.append(block)

    def move(self):
        for block_no in range(len(self.snake) - 1, 0, -1):
            self.snake[block_no].goto(self.snake[block_no - 1].pos())
        self.snake[0].forward(MOVE_DISTANCE)

    def right(self):
        snake_head = self.snake[0]
        if snake_head.heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        snake_head = self.snake[0]
        if snake_head.heading() != 0:
            self.snake[0].setheading(180)

    def up(self):
        snake_head = self.snake[0]
        if snake_head.heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        snake_head = self.snake[0]
        if snake_head.heading() != 90:
            self.snake[0].setheading(270)

    def add_block(self):
        block = Turtle('square')
        block.color('white')
        block.penup()
        block.setpos(self.snake[-1].position())
        self.snake.append(block)
