import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")


time_sleep = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_sleep)
    screen.update()

    car_manager.create_cars()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()
            

    if turtle.ycor() >= 250:           
            turtle.refresh() 
            score.score_increase()   
            time_sleep * 0.5
            
            
screen.exitonclick()

    
