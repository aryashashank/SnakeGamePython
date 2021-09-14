import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake_list = []
snake = Snake(snake_list)
food = Food()
screen.update()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_and_display_score()
        snake.add_block()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for block in snake.snake[1:]:
        if snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.game_over()
    snake.move()

screen.exitonclick()
