from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, move=False, align="center" , font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, move=False, align="center" , font=("Courier", 80, "normal"))
        

    def score_increase_left(self):
        self.l_score += 1
        self.update_score()

    def score_increase_right(self):
        self.r_score += 1
        self.update_score()
        

