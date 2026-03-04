from turtle import Turtle
import random
from paddle import paddle


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = random.choice([10,-10])
        self.dy = random.choice([10,-10])

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        if new_y > 260 or new_y < -260:
            self.dy *= -1
        self.goto(new_x, new_y)

    def paddle_contact(self, paddle):
        if abs(self.xcor() - paddle.xcor()) < 20:
            if abs(self.ycor() - paddle.ycor()) < 50:
                self.dx *= -1

    def refresh(self):
        self.goto(0,0)
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        if new_y > 260 or new_y < -260:
            self.dy *= -1
        self.goto(new_x, new_y)
    

