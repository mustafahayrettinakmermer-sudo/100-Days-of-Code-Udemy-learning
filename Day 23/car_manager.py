COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-240,-210,-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180,210,240]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.level_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.penup()
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.color(random.choice(COLORS))
            new_cars.goto(300, random.choice(LANES))
            new_cars.car_speed = random.randint(2,8)
            self.all_cars.append(new_cars)

            

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.level_speed + car.car_speed)

        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]
    
    