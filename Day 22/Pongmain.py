from turtle import Turtle, Screen
from paddle import paddle
from Ball import ball
import time
from pongscoreboard import scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)



right_paddle = paddle((350,0))
left_paddle = paddle((-350, 0))
balls = ball()
score = scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down, "s")

time_sleep = 0.1
game_is_on = True
while game_is_on:
    
    time.sleep(time_sleep)
    screen.update()
    print(balls.position())
    balls.move()
    balls.paddle_contact(right_paddle)
    balls.paddle_contact(left_paddle)

    if balls.xcor() <= -400:
        score.score_increase_left()
        balls.refresh()
        time_sleep * 0.1
    elif balls.xcor() >= 400:
        score.score_increase_right()
        balls.refresh()
        time_sleep * 0.1




    
    























screen.exitonclick()