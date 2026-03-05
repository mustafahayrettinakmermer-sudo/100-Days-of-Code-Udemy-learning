FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.update_score()
        
        
        
    def update_score(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Score:{self.score}", move=False, align="center" , font=("Courier", 24, "normal"))

    def score_increase(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center" , font=("Courier", 24, "normal"))


