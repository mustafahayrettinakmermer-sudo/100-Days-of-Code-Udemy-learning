import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import scoreboard

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreboard()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.score_increase()

    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    
        
        






















screen.exitonclick()